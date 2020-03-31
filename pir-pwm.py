from gpiozero import PWMOutputDevice, DigitalOutputDevice, MotionSensor
import time

PWM_PIN_MOT1 = 25
IN1_PIN_MOT1 = 4
IN2_PIN_MOT1 = 17
sensor = 18

pwm_pin_mot1 = PWMOutputDevice(PWM_PIN_MOT1, True, 0, 1200)
cw_pin_mot1 = DigitalOutputDevice(IN1_PIN_MOT1, True, 0)
ccw_pin_mot1 = DigitalOutputDevice(IN2_PIN_MOT1, True, 0)
pir = MotionSensor(sensor)

# to do
# filter out motor dead band (0 - 20% throttle)
# inital lap trigger
# direction control
# timer
# distance calculator

# speed up/slow down delay between throttle values
steam = 0.1


def throttle_up():
    for throttle in range(0, 100, 1):
        pwm_percnt = throttle
        pwm_percnt = int(pwm_percnt)
        pwm_percnt = pwm_percnt / 100.0
        pwm_pin_mot1.value = pwm_percnt
        cw_pin_mot1.value = 1
        ccw_pin_mot1.value = 0
        print("throttle: " + str("{:.0f}".format(throttle)) + "%", end="\r")
        time.sleep(steam)


def full_throttle():
    pwm_pin_mot1.value = 1
    throttle = (pwm_pin_mot1.value * 100)
    cw_pin_mot1.value = 1
    ccw_pin_mot1.value = 0
    print("throttle: " + str("{:.0f}".format(throttle)) + "%", end="\n")


def throttle_down():
    for throttle in range(100, 0, -1):
        pwm_percnt = throttle
        pwm_percnt = int(pwm_percnt)
        pwm_percnt = pwm_percnt / 100.0
        pwm_pin_mot1.value = pwm_percnt
        cw_pin_mot1.value = 1
        ccw_pin_mot1.value = 0
        print("throttle: " + str("{:.0f}".format(throttle)) + "%", "\033[K", end="\r")
        time.sleep(steam)


def stop():
    pwm_pin_mot1.value = 0
    throttle = (pwm_pin_mot1.value * 100)
    print("throttle: " + str("{:.0f}".format(throttle)) + "%", end="\n")


total_laps = int(input("hello. i am the train. how many laps shall i do? "))
countdown = int(input("how many seconds shall i wait before starting? "))

countdown += 1
while countdown > 0:
    time.sleep(1)
    countdown -= 1
    print("starting in: " + str(countdown), "\033[K", end="\r")

completed_laps = 0
# print("completing " + str(total_laps) + " laps. choooo chooooooo", end = "\n")
print("completing " + str(total_laps) + " laps. mind the gap.", end="\n")
time.sleep(0.5)
start = time.time()
throttle_up()
full_throttle()

while True:
    if pir.motion_detected:
        if completed_laps < 1:
            print("starting lap counter...")
            time.sleep(0.5)
        completed_laps += 1
        print("lap " + str(completed_laps) + " of " + str(total_laps), end="\r")
        time.sleep(6)

    if completed_laps >= total_laps:
        # print(str(total_laps) + " laps completed. stopping.", end = "\n")
        print(str(total_laps) + " laps completed. braking...", end="\n")
        time.sleep(0.5)
        throttle_down()
        stop()
        elapsed = (time.time() - start)
        print("time taken: " + str("{:.0f}".format(elapsed)) + " seconds.")
        time.sleep(0.5)
        print("goodbye.")
        time.sleep(1)
        exit()
