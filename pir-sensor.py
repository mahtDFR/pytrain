from gpiozero import Motor, MotionSensor
from signal import pause
from time import sleep

d1 = 4
d2 = 17
sensor = 18
laplimit = 1

pir = MotionSensor(sensor)
motor = Motor(d1, d2)

lapcount = 1
motor.forward(1)
print(str(laplimit) + " laps remaining. waiting for train to pass. choo choo!")
pir.wait_for_motion()

while True:
    if pir.motion_detected:
        print("train passed " + str(lapcount) + " time(s)")
        print(str(laplimit) + " laps remaining")
        lapcount += 1
        laplimit -= 1
        sleep(6)
        if laplimit == 0:
            print("train passed " + str(lapcount) + " times. reversing")
            motor.reverse()
            # print("exiting...")
            # exit()
