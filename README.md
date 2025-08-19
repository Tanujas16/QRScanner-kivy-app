# QR Code Scanner & Generator

A simple Kivy application to scan QR codes using your webcam and generate QR codes from text input.

## Features

- Live webcam QR code scanning (using OpenCV and pyzbar)
- Generate QR codes from text input (using qrcode)
- Save generated QR codes as PNG images

## Requirements

- Python 3.x
- Kivy
- OpenCV (`opencv-python`)
- pyzbar
- qrcode

## Installation

```sh
pip install kivy opencv-python pyzbar qrcode
```

## Usage

```sh
python main.py
```

## Notes

- Make sure your webcam is connected.
- Generated QR codes are saved as `my_qr.png` in the current directory.
