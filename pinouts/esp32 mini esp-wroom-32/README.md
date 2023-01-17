# MicroPython

### Firmware download:
- https://micropython.org/download/esp32/

### Special instructions for flashing this type of board:
N/A

### Flash instructions
1) Erase the flash storage of the device:
   1) `esptool --chip esp32 --port <device port> erase_flash`
2) Write the new firmware to the device:
   1) `esptool.py --chip esp32 --port <serial port> --baud 460800 write_flash -z 0x1000 <micropython firmware filename>.bin`

---

# PlatformIO

### Firmware download:

### Special instructions for flashing this type of board:


### Flash instructions

---

# Arduino

### Firmware download:

### Special instructions for flashing this type of board:

### Flash instructions

---

# Board pinout
![](images/D1_mini_ESP32_pinout.webp)
