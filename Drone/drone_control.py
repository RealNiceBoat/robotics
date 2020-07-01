from tello_api import Tello
import time
tello = Tello()

#tello._sendcommand('ap <SSID> <password>') # connect to wifi, but I'm not sure how exactly this works yet

tello._sendcommand('takeoff')
tello.startvideo() # enables video stream
tello.start_pad_det() # enables mission pad detection
time.sleep(5)
tello._sendcommand('go 0 25 50 50 m2') # movement, coordinates are with reference to the mission pad

tello.exit() # this includes land, it will go straight down when landing as far as I can tell so move it back to the mission pad
