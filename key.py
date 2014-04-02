#!/usr/bin/python

import Adafruit_BBIO.PWM as PWM
from Tkinter import *

""" Motor class to control the PWM signals """
class Motor:
   # pwm at P8_13, P9_14, and P9_16, P9_21, P9_42
   motor1 = "P8_13"
   motor2 = "P9_14"
   motor3 = "P9_42"
   duty_stop = 9
   duty_forward = 12 # 12 max
   duty_back = 6     # 6 min

   def __init__(self):
      """ get everything going """
      # (motor, duty, frequency, polarity)
      print 'Signals Started'
      PWM.start(Motor.motor1, Motor.duty_stop, 60.0)
      PWM.start(Motor.motor2, Motor.duty_stop, 60.0)
      PWM.start(Motor.motor3, Motor.duty_stop, 60.0)

   def shutdown(self):
      """ stop motors and PWM signals """
      print 'Signals Stopped'
      PWM.stop(Motor.motor1) # stop the motor
      PWM.stop(Motor.motor2)
      PWM.stop(Motor.motor3)
      PWM.cleanup() # stop all pwm

   def stop(self):
      """ stop the motors but not the signals """
      print 'stop'
      PWM.set_duty_cycle(Motor.motor1, Motor.duty_stop)
      PWM.set_duty_cycle(Motor.motor2, Motor.duty_stop)
      PWM.set_duty_cycle(Motor.motor3, Motor.duty_stop)

   def go_forward(self):
      print 'forward'
      PWM.set_duty_cycle(Motor.motor1, Motor.duty_forward)
      PWM.set_duty_cycle(Motor.motor2, Motor.duty_forward)

   def go_backward(self):
      print 'backward'
      PWM.set_duty_cycle(Motor.motor1, Motor.duty_back)
      PWM.set_duty_cycle(Motor.motor2, Motor.duty_back)

   def go_left(self):
      print 'left'
      PWM.set_duty_cycle(Motor.motor1, Motor.duty_forward)
      PWM.set_duty_cycle(Motor.motor2, Motor.duty_back)

   def go_right(self):
      print 'right'
      PWM.set_duty_cycle(Motor.motor1, Motor.duty_back)
      PWM.set_duty_cycle(Motor.motor2, Motor.duty_forward)

   def go_up(self):
      print 'up'
      PWM.set_duty_cycle(Motor.motor3, Motor.duty_forward)

   def go_down(self):
      print 'down'
      PWM.set_duty_cycle(Motor.motor3, Motor.duty_back)

motor = Motor()
root = Tk()
root.title("Underwater ROV Control Center")
root.geometry("100x25")

def key(event):
   if event.keysym == "Up":           # Forward  - Up key
      motor.go_forward()
      label["text"] = "Forward"
   elif event.keysym == "Down":       # Backward - Down key
      motor.go_backward()
      label["text"] = "Backward"
   elif event.keysym == "Left":       # Left     - Left key
      motor.go_left()
      label["text"] = event.keysym
   elif event.keysym == "Right":      # Right    - Right key
      motor.go_right()
      label["text"] = event.keysym
   elif event.keysym == "Shift_L":    # UP       - Shift_L
      motor.go_up()
      label["text"] = "Up"
   elif event.keysym == "Control_L":  # Down     - Control_L
      motor.go_down()
      label["text"] = "Down"
   elif event.keysym == "space":      # Stop     - space
      motor.stop()
      label["text"] = "Stop"
   elif event.keysym == "Escape":     # Shutdown - Escape
      motor.shutdown()
      label["text"] = "Shutdown"
   elif event.keysym == "i":          # init     - i
      motor.__init__()
      label["text"] = "Ready"

def stopit(event):
   if event.keysym != "Escape":
      motor.stop()
      label["text"] = "Stop"

frame = Frame(root, width=100, height=100)
frame.bind_all("<Key>", key)
frame.bind_all("<KeyRelease>", stopit)
frame.pack()

label = Label(frame, text = "Ready")
label.pack()

root.mainloop()

print '### shutdown ###'
PWM.cleanup() # stop all signals
