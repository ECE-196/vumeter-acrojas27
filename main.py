import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    # do the rest...
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    print(volume)
    
if volume >= 15000:
        leds[0].value = True
    else:
        leds[0].value = False

    if volume >= 18000:
        leds[1].value = True
    else:
        leds[1].value = False

    if volume >= 21000:
        leds[2].value = True
    else:
        leds[2].value = False

    if volume >= 24000:
        leds[3].value = True
    else:
        leds[3].value = False

    if volume >= 27000:
        leds[4].value = True
    else:
        leds[4].value = False

    if volume >= 30000:
        leds[5].value = True
    else:
        leds[5].value = False

    if volume >= 33000:
        leds[6].value = True
    else:
        leds[6].value = False

    if volume >= 36000:
        leds[7].value = True
    else:
        leds[7].value = False

    if volume >= 39000:
        leds[8].value = True
    else:
        leds[8].value = False

    if volume >= 42000:
        leds[9].value = True
    else:
        leds[9].value = False

    if volume >= 45000:
        leds[10].value = True
    else:
        leds[10].value = False

    sleep(0.1)
