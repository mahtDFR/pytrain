from gpiozero import Motor
from gpiozero.tools import sin_values, cos_values, clamped, scaled
from signal import pause
from time import sleep

d1 = 4
d2 = 17

motor = Motor(d1, d2)
motor.source = clamped(sin_values(10000), 0, 1)
print("choo choo!")
pause()
