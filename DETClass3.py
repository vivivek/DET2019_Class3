#welcome to DET2019 Class 3! We'll be working
#with Raspberry Pi and Python3 to control servo's
#and introduce three basic concepts into your toolkit
#these lines import the key libraries we need for this
#script - in order to control the crickit and keep track
#of time!

import time
from adafruit_crickit import crickit

def motor_wait():
#this function moves the servo to original angle, 0
#and increments its position by two 90 degree steps
#before rotating back to 0 degrees. Courtesy Adam Hutz!
#crickit.servo_1.angle sets the angle of your stepper motor
#time.sleep() asks the processor to wait before executing
       
    print("Moving servo #1: motor_wait()")
    crickit.servo_1.angle = 0      # right
    time.sleep(1)
    crickit.servo_1.angle = 90     # middle
    time.sleep(1)
    crickit.servo_1.angle = 180    # left
    time.sleep(1)
    crickit.servo_1.angle = 90     # middle
    time.sleep(1)
    crickit.servo_1.angle = 0     # right

def motor_conditional():
    #conditionals in python are easy! and, with crickit - fun.
    #this function checks whether the capacitive touch field
    #number one on the crickit board has been activated.
    #if it is, the motor rotates by 180 degrees.
    #if not, you get a message telling you as much :)

    crickit.touch_1.value
    print("Press the Capactive Touch button 1: motor_conditional()")
    time.sleep(3)
    print(crickit.touch_1.value)
    
    if crickit.touch_1.value:
        crickit.servo_1.angle = 180      # right
        time.sleep(2)
        crickit.servo_1.angle = 0 
    else:
        print("No button push detected.")
        
def motor_while():
    #in this while loop, two conditions need to be met:
    #the capacitive button must be pressed, and the motor must
    #not have reached 180 degrees in turning. As long as these
    #conditions are satisfied, the motor turns, incremented by
    #3 degrees every tenth of a second. 
    
    crickit.touch_1.value
    print("Hold the Capactive Touch button to keep running the motor: motor_while()")
    time.sleep(3)
        
    motor_angle = 1
    
    while crickit.touch_1.value and motor_angle < 180:
        crickit.servo_1.angle = motor_angle
        motor_angle += 3
        time.sleep(0.1)

def motor_for():
    #in this for loop, the motor steps by 30 degrees
    #five times.
    #range(x,y,z) specifies the bounds on the for loop,
    #with x being the initial value, y being the final value
    #not to be exceeded, and z being the increment.
    
    print("For Loop Engaged!: motor_for()")
        
    motor_angle = 1
    
    for x in range (0, 181, 30):
        crickit.servo_1.angle = x
        time.sleep(0.5)

def main():
    # runs code by default!   
  
    print("Hello! DET2019 Servo Test: Starting!")  #print something nice!
    crickit.servo_1.angle = 0                      #set motor to angle '0'
#    motor_wait()
#    motor_conditional()
#    motor_while()
#    motor_for()


# the below 'if' statement helps python distinguish the main function.
if __name__ == '__main__':
    main()