# Flash instructions

Erase the flash storage of the device: `esptool --port <device port> erase_flash`


Write the new firmware to the device: `esptool.py --port <device port> --baud 460800 write_flash -fm dio --flash_size=detect 0 <micropython firmware filename>.bin`

---

# Board pinout
![](images/wemos_d1_mini_pinout.png)