import sys
import threading
import time
import pygame as pg
import requests
import decimal
import socket, binascii, datetime
import logging

running = 1
black = 0, 0, 0
size = width, height = 480, 320
screen = pg.display.set_mode(size)
box = pg.image.load("whitebox.png")
boxrect = box.get_rect()

HOST = ''                                 # Hostname or ip address of interface, leave blank for all
PORT = 56743                              # listening on port 9999 

class WeatherServer(threading.Thread):
        temp = 0
        def run(self):
                url = "http://api.openweathermap.org/data/2.5/weather?q=stafford,uk&units=metric&APPID=9e0c2dc0b19e2e83e58cecc273d68cea"
                print("{} started!".format(self.getName()))              # "Thread-x started!"
                print("Getting temp")              # "Thread-x started!"
                r = requests.get(url)
                weatherData = r.json()
                self.temp = weatherData["main"]["temp"]


class InverterCallBack(threading.Thread):
        def run(self):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # create socket on required port
                sock.bind((HOST, PORT))

                while True:        # loop forever
                        sock.listen(1)                            # listen on port
                        conn, addr = sock.accept()                # wait for inverter connection
                        rawdata = conn.recv(1000)                # read incoming data
                        hexdata = binascii.hexlify(rawdata)        # convert data to hex
                        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
                        logging.debug('Current data is : ' + str(hexdata))

def main():

        mythread = WeatherServer(name = "Thread-Weather getter")  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()

        inverterThread = InverterCallBack(name = "inverter comms")
        inverterThread.start()

        temp = 16
        showstatus = True
        startTimeForStatus = time.time()
        startTimeForTempUpdate = time.time()
        pg.font.init()
        font = pg.font.SysFont("comicsansms", 24)
        clock = pg.time.Clock()

        # set the center of the rectangular object. 
        while running:
                for event in pg.event.get():
                        if event.type == pg.MOUSEBUTTONUP:
                                None 
                        if event.type == 

                screen.fill(black)
                if (showstatus):
                        screen.blit(box, boxrect)

                elapsedTimeForStatus = time.time() - startTimeForStatus
                elapsedTimeForTemp = time.time() - startTimeForTempUpdate
                if (elapsedTimeForStatus > 2):
                        showstatus = not showstatus
                        startTimeForStatus = time.time()
                if (elapsedTimeForTemp > 3600):
                        startTimeForTempUpdate = time.time()
                        mythread.start()
                        InverterCallBack
                temp = mythread.temp
                stringtooutput = str(int(temp)) + '\u00b0'
                text = font.render(stringtooutput, True, (255, 255, 255), (0,0,0)) 
                screen.blit(text,(435,5))
                pg.display.flip()
                clock.tick(60)

if __name__ == '__main__':main()