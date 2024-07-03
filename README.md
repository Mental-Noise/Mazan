# Mazan

Mazan is a Rapsberry pico based MIDI-USB Interface.

It can:
- receive MIDI commands from a MIDI device and send them to your computer via USB
- receive MIDI commabds from your computer via USB and send them to a MIDI device

## Hardware

This project is based on the Adafruit MIDI featherwing, you can either use that module or build it yourself following this guide.

To do it yourself, you'll need:
- 1x Raspberry pico (or RP2040-zero for smaller factor)
- 1x H11L1 optcoupler
- 2x MIDI DIN 5 pins connector or stereo jack or both
- 2x 2.2kΩ resistor
- 1x 470Ω resistor
- 1x 220Ω resistor
- 1x 30Ω resistor
- 1x 10Ω resistor
- 2x LED
- 1x 1N4148 diode

Schematics coming soon...

## Software

### Cleanup your raspberry pico

Download [FlashNuke](https://github.com/dwelch67/raspberrypi-pico/blob/main/flash_nuke.uf2).  
Connect your raspberry pico to your computer while holding the `boot` button pressed.  
Copy/paste the file named `flash_nuke.uf2` on the raspberry pico drive, it will automatically eject and re-mount.

### Install CircuitPython

Download the latest version of [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/) (v9.0.5 at time of writing) and extract the zip content.  
Connect your raspberry pico to your computer while holding the `boot` button pressed.  
Copy/paste the CircuitPython firmware (file named `adafruit-circuitpython-raspberry_pi_pico-en_US-9.0.5.uf2` in my case) on the raspberry pico drive, it will automatically eject and re-mount.

### Add the software

Copy the code from [code.py](./code.py) in this repository.  
Open the file named `code.py` on your raspberry pico and replace its content with the code you just copied.  
Reset the raspberry pico.  
You're done.
