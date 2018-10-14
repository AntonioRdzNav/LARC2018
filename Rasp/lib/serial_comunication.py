import serial
import time

class Serial:
    def __init__(self, screen):
        try:
            self.arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=0, writeTimeout=0)
            time.sleep(3)
            self.screen = screen
        except serial.SerialException:
            print 'Bad port, check labeling'
            while True:
                pass

    def send(self, char):
        self.arduino.write(char)

    def read(self):
        while(self.arduino.inWaiting() <= 0):
            pass
        return self.arduino.read()

    def first_read(self):
        start_time = time.time()
        while(self.arduino.inWaiting() <= 0):
            if time.time() - start_time > 5:
                print "Time limit!"
                return '*'
            pass
        return self.arduino.read()

    def convert(self, pair):
        return chr(ord(str(pair[0])) + (ord(pair[1]) - 65) * 3)

    def start(self):
        self.send('T')
        if self.first_read() != '*':
            print "Serial communication enabled!"
        else:
            self.screen.errorMessage("Serial communication has failed")
            self.screen.mainloop()




