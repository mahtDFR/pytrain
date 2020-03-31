from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

PWM_PIN_MOT1 = 25
IN1_PIN_MOT1 = 4
IN2_PIN_MOT1 = 17

pwm_pin_mot1 = PWMOutputDevice(PWM_PIN_MOT1, True, 0, 1200)
cw_pin_mot1 = DigitalOutputDevice(IN1_PIN_MOT1, True, 0)
ccw_pin_mot1 = DigitalOutputDevice(IN2_PIN_MOT1, True, 0)

# to do
# filter out motor dead zone (0 - 20%)

# time to stay at full throttle
full_throttle_time = 30

# speed up/slow down delay between throttle values
steam = 0.1


# define directions
def throttle_up_d1():
    for throttle in range(0, 100, 1):
        print("throttle d1: " + str("{:.2f}".format(throttle)) + "%")
        pwm_percnt = throttle
        pwm_percnt = int(pwm_percnt)
        pwm_percnt = pwm_percnt / 100.0
        pwm_pin_mot1.value = pwm_percnt
        cw_pin_mot1.value = 1
        ccw_pin_mot1.value = 0
        sleep(steam)


def throttle_up_d2():
    for throttle in range(0, 100, 1):
        pwm_percnt = throttle
        pwm_percnt = int(pwm_percnt)
        pwm_percnt = pwm_percnt / 100.0
        pwm_pin_mot1.value = pwm_percnt
        cw_pin_mot1.value = 0
        ccw_pin_mot1.value = 1
        print("throttle d2: " + str("{:.2f}".format(throttle)) + "%")
        sleep(steam)


def full_throttle_d1():
    pwm_pin_mot1.value = 1
    throttle = (pwm_pin_mot1.value * 100)
    cw_pin_mot1.value = 1
    ccw_pin_mot1.value = 0
    print("throttle d1: " + str("{:.2f}".format(throttle)) + "%")
    sleep(full_throttle_time)


def full_throttle_d2():
    pwm_pin_mot1.value = 1
    throttle = (pwm_pin_mot1.value * 100)
    cw_pin_mot1.value = 0
    ccw_pin_mot1.value = 1
    print("throttle d2: " + str("{:.2f}".format(throttle)) + "%")
    sleep(full_throttle_time)


def throttle_down_d1():
    for throttle in range(100, 0, -1):
        pwm_percnt = throttle
        pwm_percnt = int(pwm_percnt)
        pwm_percnt = pwm_percnt / 100.0
        pwm_pin_mot1.value = pwm_percnt
        cw_pin_mot1.value = 1
        ccw_pin_mot1.value = 0
        print("throttle d1: " + str("{:.2f}".format(throttle)) + "%")
        sleep(steam)


def throttle_down_d2():
    for throttle in range(100, 0, -1):
        pwm_percnt = throttle
        pwm_percnt = int(pwm_percnt)
        pwm_percnt = pwm_percnt / 100.0
        pwm_pin_mot1.value = pwm_percnt
        cw_pin_mot1.value = 0
        ccw_pin_mot1.value = 1
        print("throttle d2: " + str("{:.2f}".format(throttle)) + "%")
        sleep(steam)


def stop():
    pwm_pin_mot1.value = 0
    throttle = (pwm_pin_mot1.value * 100)
    print("throttle: " + str("{:.2f}".format(throttle)) + "%")


# main loop

i = 1
while i <= 3:
    throttle_up_d1()
    full_throttle_d1()
    throttle_down_d1()
    print(i)
    i += 1

# sleep(0.5)
# throttle_up_d2()
# full_throttle_d2()
# throttle_down_d2()
stop()
exit()
