# script to control a model train
# matt jani 2020

# to do
# fix curses diagonal text output
# integrate twitter control gimmick
# if already stopped, dont stop again on quit

import curses
from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

PWM_PIN_MOT1 = 25
IN1_PIN_MOT1 = 4
IN2_PIN_MOT1 = 17

pwm_pin_mot1 = PWMOutputDevice(PWM_PIN_MOT1, True, 0, 1200)
cw_pin_mot1 = DigitalOutputDevice(IN1_PIN_MOT1, True, 0)
ccw_pin_mot1 = DigitalOutputDevice(IN2_PIN_MOT1, True, 0)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

steam = 0.15
full_throttle_time = 3


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
    print("throttle d1: " + str(throttle) + "%")
    sleep(full_throttle_time)  # this needs to loop forever until a keypress. for now will set a finite time


def full_throttle_d2():
    pwm_pin_mot1.value = 1
    throttle = (pwm_pin_mot1.value * 100)
    cw_pin_mot1.value = 0
    ccw_pin_mot1.value = 1
    print("throttle d2: " + str(throttle) + "%")
    sleep(full_throttle_time)  # this needs to loop forever until a keypress. for now will set a finite time


def throttle_down_d1():
    for throttle in range(100, 0, -1):
        pwm_percnt = throttle
        pwm_percnt = int(pwm_percnt)
        pwm_percnt = pwm_percnt / 100.0
        pwm_pin_mot1.value = pwm_percnt
        cw_pin_mot1.value = 1
        ccw_pin_mot1.value = 0
        print("throttle d2: " + str("{:.2f}".format(throttle)) + "%")
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


try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            stop()  # need to get direction state, and motion state
            time.sleep(0.5)
            print("goodbye")
            time.sleep(0.5)
            break

        elif char == curses.KEY_UP:
            throttle_up_d1()
            full_throttle_d1()

        elif char == curses.KEY_DOWN:
            throttle_up_d2()
            full_throttle_d2()

        elif char == ord('s'):
            throttle_down_d1()  # need to work out how to get direction state, will default to 1 for now
            stop()

finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak();
    screen.keypad(0);
    curses.echo()
    curses.endwin()
