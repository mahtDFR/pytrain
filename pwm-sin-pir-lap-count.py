from gpiozero import Motor, MotionSensor
from signal import pause
from time import sleep
from gpiozero.tools import sin_values, cos_values, clamped, scaled

d1 = 4
d2 = 17
sensor = 18

pir = MotionSensor(sensor)
motor = Motor(d1, d2)

lapcount = 1
motor.source = clamped(sin_values(7000), 0, 1)
# motor.source = sin_values(7000)
print("chooooo chooooooo")
pir.wait_for_motion()

while True:
    if pir.motion_detected:
        print("train passed " + str(lapcount) + " time(s)", flush=True)
        lapcount += 1
        sleep(5)

pause()
