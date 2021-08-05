from step import Stepper

MOTOR_STEPS = (2048)
PIN_MOTOR_1 = (27)
PIN_MOTOR_2 = (26)
PIN_MOTOR_3 = (25)
PIN_MOTOR_4 = (23)

my_motor = Stepper(MOTOR_STEPS, PIN_MOTOR_1,
                   PIN_MOTOR_2, PIN_MOTOR_3, PIN_MOTOR_4)

for i in range(50, 150, 1):
    my_motor.set_speed(i/10)
    my_motor.step(16)

for i in range(150, 50, -1):
    my_motor.set_speed(i/10)
    my_motor.step(-16)

# # my_motor.step(512)
# for _ in range(5):
#     my_motor.step(2048*3)
#     my_motor.step(-2048*3)
