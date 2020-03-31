from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep

PWM_PIN_MOT1 = 25
IN1_PIN_MOT1 = 4
IN2_PIN_MOT1 = 17

# PWMOutputDevice takes  BCM_PIN number
# Active High
# intial value
# PWM Frequency
# and Pin_factory which can be ignored

pwm_pin_mot1 = PWMOutputDevice(PWM_PIN_MOT1, True, 0, 1200)

# DigitalOutputDevice take
# Pin Nuumber
# Active High
# Initial Value

cw_pin_mot1 = DigitalOutputDevice(IN1_PIN_MOT1, True, 0)

ccw_pin_mot1 = DigitalOutputDevice(IN2_PIN_MOT1, True, 0)


def RotateMotorCW():
    print('Enter Motor speed 0 to 100 percent')
    pwm_percnt = input()
    pwm_percnt = int(pwm_percnt)
    pwm_percnt = pwm_percnt / 100.0
    pwm_pin_mot1.value = pwm_percnt
    cw_pin_mot1.value = 1
    ccw_pin_mot1.value = 0


def RotateMotorCCW():
    print('Enter Motor speed 0 to 100 percent')
    pwm_percnt = input()
    pwm_percnt = int(pwm_percnt)
    pwm_percnt = pwm_percnt / 100.0
    pwm_pin_mot1.value = pwm_percnt
    cw_pin_mot1.value = 0
    ccw_pin_mot1.value = 1


def StopMotor():
    cw_pin_mot1.value = 0
    ccw_pin_mot1.value = 0
    pwm_pin_mot1.value = 0


def main():
    try:
        while True:
            RotateMotorCW()
            sleep(4)
            RotateMotorCCW()
    except KeyboardInterrupt:
        print('Interrupted')
    StopMotor()


if __name__ == "__main__":
    main()
