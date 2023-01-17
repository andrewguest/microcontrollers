# MicroPython

### Firmware download:
* Raspberry Pi Pico (rp2-pico)
  - https://micropython.org/download/rp2-pico/
* Raspberry Pi Pico W (rp2-pico-w)
  - https://micropython.org/download/rp2-pico-w/

### Special instructions for flashing this type of board:
* If a version of MicroPython is already installed on the board:
  - Execute `machine.bootloader()` at the MicroPython REPL.
* If MicroPython is **NOT** installed on the board:
  - Hold down the **BOOTSEL** button while plugging in the USB cable to the board.


### Flash instructions
1) Enter bootloader mode using any special instructions listed above.
2) Copy the **.uf2** firmware file you downloaded, using the link above, to the USB mass storage device that now appears.
3) Once the programming of the new firmware is complete, the device will automatically reset and be ready to use.
4) You can now copy **.py** file to the device.
   1) `boot.py` is executed once and is generally used to setup the device.
   2) `main.py` is executed repeatedly and generally contains the main code of the project.

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
![](images/raspberry_pi_pico_pinout.png)