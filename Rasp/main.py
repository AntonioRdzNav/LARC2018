import cv2
import sys
sys.path.insert(0, './lib/')
from serial_comunication import Serial
from cam import Cam
from tkinter import Screen
from algorithm import Algorithm

cam1 = Cam(0)
cam2 = Cam(1)

screen = Screen()
screen.drawText()

brain = Algorithm(screen.getContainers())

print "starting..."
serial = Serial(screen)
serial.start()   #

serial.read()   #
cam1.shoot()    #
cam2.shoot()    #
screen.drawContainers(cam1.getImage(), 3)
screen.drawContainers(cam2.getImage(), 2)
first = brain.firstPick()  #
screen.popContainer(first[0]) #
serial.send(serial.convert(first))#
brain.setPriority()

first_time = True

def main():
	c = serial.read()

	if c == 'R' or c == 'S':
		brain.setPriority()
		c = 'R1' if c == 'R' else 'R2'

	brain.set_last_color(c)

	if(first_time and c == 'G'):
		serial.send('S')
		serial.read()
		cam1.shoot()
		cam2.shoot()
		screen.drawContainers(cam1.getImage(), 1)
		screen.drawContainers(cam2.getImage(), 0)
		second = brain.secondPick()
		screen.popContainer(second[0])
		serial.send(serial.convert(second))
		brain.setPriority()
		first_time = False
	else:
		res = brain.solve()
		screen.popContainer(res[0])
		serial.send(serial.convert(res))

	screen.run(5,main)

screen.run(0, main)
screen.mainloop()

cam1.release()
cam2.release()
cv2.destroyAllWindows()