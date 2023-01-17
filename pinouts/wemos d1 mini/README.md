# MicroPython

### Firmware download:
- https://micropython.org/download/esp8266/

### Special instructions for flashing this type of board:
N/A

### Flash instructions
1) Erase the flash storage of the device:
   1) `esptool --port <device port> erase_flash`
2) Write the new firmware to the device:
   1) `esptool.py --port <device port> --baud 460800 write_flash -fm dio --flash_size=detect 0 <micropython firmware filename>.bin`

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
![](images/wemos_d1_mini_pinout.png)
