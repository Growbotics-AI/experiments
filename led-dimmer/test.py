import L298NHBridgePCA9685 as HBridge
import time

channel_left = 1 
channel_right = 1

while (channel_left >= 0): 
   print("Brigthness:" + str(channel_left*100) + "%")
   channel_left = channel_left - 0.01
   channel_right = channel_right - 0.01
   HBridge.setMotorLeft(channel_left)
   HBridge.setMotorRight(channel_right)
   time.sleep(0.1)

HBridge.setMotorLeft(0)
HBridge.setMotorRight(0)
HBridge.exit ()
