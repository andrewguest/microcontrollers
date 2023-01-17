from machine import Pin
import time


def button_callback(pin):
    """Function that will be executed when the interrupt is triggered

    Args:
        pin (machine.Pin): The Pin object that triggered the interrupt
    """

    global BUTTON_STATE  # Create a global variable to help handle debounce
    button.irq(handler=None)  # Turn off the handler while it's executing

    if (button.value() == 1) and (BUTTON_STATE == 0):
        # Handle button debounce by checking the button's current value and the global variable
        # This function should only execute once with these cheecks in place
        BUTTON_STATE = 1
        print("Button was pressed!")
    elif (button.value() == 0) and (BUTTON_STATE == 1):
        # Return the BUTTON_STATE to a "0" value after it's been pressed
        BUTTON_STATE = 0

    button.irq(handler=button_callback)  # Re-enable the handler


# 0 - Physical GPIO pin that the button is connected to (GPI0 in this case)
# Pin.IN - Set pin as input
# Pin.PULL_DOWN - Enable an internal pull-down resistor on the pin.

# Pull-down resistors are resistors which are used to ensure that a wire is pulled to a LOW logic level (0)
#   in the absense of an input signal.
# With a pull-down resistor, the input pin will read a low state when the button is NOT pressed.
button = Pin(0, Pin.IN, Pin.PULL_DOWN)


# trigger - What state the button needs to be in to trigger the handler function to be called.
# handler - The function to call when an interrupt is detected
# IRQ_RISING - If the voltage is in a RISING state.

# Since the button pin is setup with a PULL_DOWN resistor and will normally read "0", pressing the button
#   will causing the voltage to start dropping from "0" to "1" (RISING).

# This means the interrupt function will be triggered as soon as the button is pressed, since
#   the voltage will start to rise immediately. Setting this to IRQ_FALLING would have the effect
#   of only triggering the interrupt function when the button has been pressed and released, since
#   the voltage would have RISEN and then started to FALL again.
button.irq(handler=button_callback, trigger=Pin.IRQ_RISING)


BUTTON_STATE = button.value()  # Preset the global variable

while True:
    # Do some other tasks here
    time.sleep(1)
