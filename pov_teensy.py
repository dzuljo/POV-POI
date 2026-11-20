import os
import glob
import subprocess

ARDUINO_CLI = "/opt/homebrew/bin/arduino-cli"
SKETCH_DIR = "/Users/dzuljo/Documents/Arduino/PovPoiAPP"
BUILD_DIR = "/Users/dzuljo/Documents/Arduino/PovPoiAPP/build"
FQBN = "teensy:avr:teensy31"

def find_teensy_tool(tool_name):
    pattern = os.path.expanduser(f"~/Library/Arduino15/packages/teensy/tools/teensy-tools/*/{tool_name}")
    matches = sorted(glob.glob(pattern))
    return matches[-1] if matches else None

def compile_and_upload(status_callback=None):
    def log(msg):
        if status_callback:
            status_callback(msg)

    os.makedirs(BUILD_DIR, exist_ok=True)
    log("Компајлирање за Teensy 3.2...")

    compile_cmd = [
        ARDUINO_CLI, "compile",
        "--fqbn", FQBN,
        "--output-dir", BUILD_DIR,
        SKETCH_DIR
    ]
    res = subprocess.run(compile_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        return False, f"Грешка при компајлирање:\n{res.stderr}"

    hex_path = os.path.join(BUILD_DIR, "PovPoiAPP.ino.hex")
    if not os.path.exists(hex_path):
        return False, "Не е пронајден .hex фајлот по компајлирањето."

    post_compile = find_teensy_tool("teensy_post_compile")
    if not post_compile:
        return False, "Не е пронајден teensy_post_compile во ~/Library/Arduino15/."

    tools_dir = os.path.dirname(post_compile)
    log("Испраќање во Teensy Loader...")

    upload_cmd = [
        post_compile,
        "-file=PovPoiAPP.ino",
        f"-path={BUILD_DIR}",
        f"-tools={tools_dir}",
        "-board=TEENSY31",
        "-reboot"
    ]
    up_res = subprocess.run(upload_cmd, capture_output=True, text=True)
    if up_res.returncode != 0:
        return False, f"Грешка при Teensy Upload:\n{up_res.stderr}"

    return True, "Успешно вбризгано во Teensy 3.2! (Притисни го копчето на Teensy ако не почне само)."
