from gpiozero import Motor, MotionSensor

d1 = 4
d2 = 17
sensor = 18

pir = MotionSensor(sensor)
motor = Motor(d1, d2)

while True:
    pir.when_motion = motor.forward
    pir.when_no_motion = motor.stop

pause()
