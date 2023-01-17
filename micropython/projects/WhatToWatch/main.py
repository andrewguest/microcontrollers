import esp32
import random
from machine import Pin, SPI
from time import sleep

from ili9341 import Display, color565
from xglcd_font import XglcdFont


# Setup pins and SPI display
picker_button = Pin(27, Pin.IN, Pin.PULL_DOWN)  # GPIO27 will normally read "0"
spi = SPI(1, sck=Pin(18), mosi=Pin(23))
display = Display(spi, dc=Pin(2), cs=Pin(15), rst=Pin(4), rotation=180)

# Load the font files for the SPI display
print("Loading fonts...")
print("Loading broadway")
broadway = XglcdFont("fonts/Broadway17x15.c", 17, 15)
print("Loading unispace")
unispace = XglcdFont("fonts/Unispace12x24.c", 12, 24)


def button_interrupt(pin):
    print("Button pressed")


# Setup interrupt for when the button is pressed
# Execute when GPIO27 starts rising from "0" to "1"
picker_button.irq(button_interrupt, Pin.IRQ_RISING)


def test_display():
    """Test code."""

    display.draw_text(
        40,
        255,
        "Push the button and",
        unispace,
        color565(52, 201, 235),
        landscape=True,
    )
    display.draw_text(
        90,
        255,
        "I'll pick something",
        unispace,
        color565(52, 201, 235),
        landscape=True,
    )
    display.draw_text(
        140,
        255,
        "for you to watch",
        unispace,
        color565(52, 201, 235),
        landscape=True,
    )

    # display.draw_text(
    #     120,
    #     255,
    #     "<Movie title here>",
    #     broadway,
    #     color565(255, 195, 0),
    #     landscape=True,
    # )

    sleep(300)
    display.cleanup()
    display.off()


while True:
    print("Random number: " + str(random.randrange(1, 100)))
    print("Button's value: " + str(picker_button.value()))
    sleep(2)
