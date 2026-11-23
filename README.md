# POV Poi Studio (Teensy 3.2)

Desktop Python application (macOS) for designing, simulating, and uploading Persistence of Vision (POV) light shows to **Teensy 3.2** POV Poi controllers (72x APA102 LEDs).

## Features

- **3-Program Timeline Editor:** Manage up to 3 independent programs with multi-select (`Shift` / `Cmd`), scrub bar, black pause slots, and live Flash memory usage meter (~200 KB limit).
- **Real-Time Polar Simulator:** Live donut-ring preview (`R1 Ratio`, `Spin RPS`, `FPS`) and LED strip visualizer.
- **Image & Animation Tools:**
  - Visual Crop with **Auto-Trim**
  - Built-in **POV Text Generator** (1 or 2 lines, macOS fonts, gradients)
  - GIF frame extraction & **Decimate GIF Frames**
  - `Rotate 90°`, `Mirror H`, `Flip V`, `Color Tint`, `Gamma`, `Brightness`, and `Remove Background`
- **4-Bit Indexed Palette Compression & C Header Export:** Compiles slices into compact 16-color indexed palettes (`sliki.h`) for Teensy `PROGMEM`.
- **1-Click Arduino CLI Compile & Upload:** Automatically compiles and flashes firmware directly to Teensy 3.2 via USB.

## Project Structure

```text
PoiProekt/
├── konvertor.py              # Main CustomTkinter GUI & timeline editor
├── pov_engine.py             # Image processing, 16-color quantization & sliki.h generator
├── pov_polar.py              # Real-time polar & LED strip simulation renderer
├── pov_text.py               # 1 & 2-line POV text generator dialog
├── pov_teensy.py             # Teensy 3.2 compile & upload integration
├── Start_POV_Studio.command  # Quick launch script
└── requirements.txt          # Python dependencies
```

## Installation & Usage

```bash
pip3 install -r requirements.txt
python3 konvertor.py
```
