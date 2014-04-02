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
      self.stop()
      print 'forward'
      PWM.set_duty_cycle(Motor.motor1, Motor.duty_forward)
      PWM.set_duty_cycle(Motor.motor2, Motor.duty_forward)

   def go_backward(self):
      self.stop()
      print 'backward'
      PWM.set_duty_cycle(Motor.motor1, Motor.duty_back)
      PWM.set_duty_cycle(Motor.motor2, Motor.duty_back)

   def go_left(self):
      self.stop()
      print 'left'
      PWM.set_duty_cycle(Motor.motor1, Motor.duty_forward)
      PWM.set_duty_cycle(Motor.motor2, Motor.duty_back)

   def go_right(self):
      self.stop()
      print 'right'
      PWM.set_duty_cycle(Motor.motor1, Motor.duty_back)
      PWM.set_duty_cycle(Motor.motor2, Motor.duty_forward)

   def go_up(self):
      self.stop()
      print 'up'
      PWM.set_duty_cycle(Motor.motor3, Motor.duty_forward)

   def go_down(self):
      self.stop()
      print 'down'
      PWM.set_duty_cycle(Motor.motor3, Motor.duty_back)


class GUI(Frame):
   """ A GUI application """
   motor = Motor()

   def __init__(self, master):
      """ initialize the frame """
      Frame.__init__(self, master)
      self.pack()
      self.create_widgets()

   def create_widgets(self):
      """ Create Label """
      self.label = Label(self, text = "Ready")
      self.label.grid(row = 3, column = 2)
      self.space = Label(self, text = " ")
      self.space.grid(row = 5, column = 4)

      """ Create buttons """
      self.button1 = Button(self, text = "LEFT", width = 10)    # left
      self.button1["command"] = self.left_clicked
      self.button1.grid(row = 3, column = 1)

      self.button2 = Button(self, text = "RIGHT", width = 10)   # right
      self.button2["command"] = self.right_clicked
      self.button2.grid(row = 3, column = 3)

      self.button3 = Button(self, text = "FORWARD", width = 10) # forward
      self.button3["command"] = self.forward_clicked
      self.button3.grid(row = 2, column = 2)

      self.button4 = Button(self, text = "BACK", width = 10)    # back
      self.button4["command"] = self.back_clicked
      self.button4.grid(row = 4, column = 2)

      self.button5 = Button(self, text = "UP", width = 10)      # up
      self.button5["command"] = self.up_clicked
      self.button5.grid(row = 2, column = 5)

      self.button6 = Button(self, text = "STOP", width = 10)    # stop
      self.button6["command"] = self.stop_clicked
      self.button6.grid(row = 3, column = 5)

      self.button7 = Button(self, text = "DOWN", width = 10)    # down
      self.button7["command"] = self.down_clicked
      self.button7.grid(row = 4, column = 5)

      self.button8 = Button(self, text = "INIT", width = 45) # Initialize
      self.button8["command"] = self.init_clicked
      self.button8.grid(row = 6, column = 1, columnspan = 5)

      self.button9 = Button(self, text = "KILL", width = 45) # shutdown
      self.button9["command"] = self.shutdown_clicked
      self.button9.grid(row = 7, column = 1, columnspan = 5)

   def up_clicked(self):
      self.label["text"] = "UP"
      GUI.motor.go_up()

   def down_clicked(self):
      self.label["text"] = "DOWN"
      GUI.motor.go_down()

   def left_clicked(self):
      self.label["text"] = "LEFT"
      GUI.motor.go_left()

   def right_clicked(self):
      self.label["text"] = "RIGHT"
      GUI.motor.go_right()

   def forward_clicked(self):
      self.label["text"] = "FORWARD"
      GUI.motor.go_forward()

   def back_clicked(self):
      self.label["text"] = "BACK"
      GUI.motor.go_backward()

   def stop_clicked(self):
      self.label["text"] = "STOP"
      GUI.motor.stop()

   def init_clicked(self):
      self.label["text"] = "STARTED"
      GUI.motor.__init__()

   def shutdown_clicked(self):
      self.label["text"] = "SHUTDOWN"
      GUI.motor.shutdown()

root = Tk()
root.title("Underwater ROV Control Center")
#root.geometry("500x240")

app = GUI(root)

root.mainloop() # the eternal loop

print '### shutdown ###'
PWM.cleanup() # stop all signals
