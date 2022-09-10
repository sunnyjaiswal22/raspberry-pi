from gpiozero import Motor
from time import sleep

#9: Back left forward
#10: Back Right forward
#11: Back left reverse
#12: Back Right reverse
#16: Front Left Forward
#17: Front Left Reverse
#13: Front Right Reverse
#18: Front Right Forward

motor = Motor(forward=18, backward=0)

print('Starting robot')

motor.forward()
sleep(3)
