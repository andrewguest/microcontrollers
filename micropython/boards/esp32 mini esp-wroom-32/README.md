# Flash instructions

Erase flash:
`esptool.py --chip esp32 --port <serial port> erase_flash`

Flash Micropython firmware:
`esptool.py --chip esp32 --port <serial port> --baud 460800 write_flash -z 0x1000 <micropython firmware filename>.bin`

---

# Board pinout
![](images/D1_mini_ESP32_pinout.webp)