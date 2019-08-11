# -*- coding: utf-8 -*-
import os
import sys
import threading
import time
import pygame as pg
import requests
import decimal
import socket, binascii, datetime
import logging
import WeatherServer
import read_solar
import logging
import logging.handlers
from datetime import datetime

os.putenv('SDL_FBDEV', '/dev/fb1')

running = 1
black = 0, 0, 0
size = width, height = 480, 320
screen = pg.display.set_mode(size)
box = pg.image.load("whitebox.png")
boxrect = box.get_rect()
pg.mouse.set_visible(False)

class MainClass():
        light = (50, 50, 50)
        def init_logger(self):
                level = logging.DEBUG
                logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',level=level)

                Rthandler = logging.handlers.RotatingFileHandler('solarreader.log', maxBytes=100*1024*1024,backupCount=10)
                Rthandler.setLevel(level)
                formatter = logging.Formatter('%(asctime)-12s [%(levelname)s] %(message)s')  
                Rthandler.setFormatter(formatter)
                logging.getLogger('').addHandler(Rthandler)

        def mainloop(self):
                self.init_logger()
                currentLight = self.light
                logging.debug('started main')
                running=1
                mythread = WeatherServer.WeatherServer(name = "Thread-Weather getter")  # ...Instantiate a thread and pass a unique ID to it
                mythread.daemon = True
                mythread.start()

                inverterThread = read_solar.InverterCallBack(name = "inverter comms")
                inverterThread.daemon = True
                inverterThread.start()

                temp = 0
                showstatus = True
                
                startTimeForStatus = time.time()

                pg.font.init()
                font = pg.font.SysFont("comicsansms", 64)
                clock = pg.time.Clock()

                # set the center of the rectangular object. 
                while running:
                        for event in pg.event.get():
                                if event.type == pg.MOUSEBUTTONUP:
                                        None
                                if event.type == pg.KEYDOWN:
                                        logging.debug('keydown detected')
                                        running=0

                        screen.fill(black)
                        if (showstatus):
                                screen.blit(box, boxrect)

                        elapsedTimeForStatus = time.time() - startTimeForStatus
                        
                        if (elapsedTimeForStatus > 1):
                                showstatus = not showstatus
                                startTimeForStatus = time.time()
                                
                        temp = mythread.temp
                        stringtooutput = str(int(temp)) + u'\N{DEGREE SIGN}'
                                
                        text = font.render(stringtooutput, True, currentLight, (0,0,0)) 
                        screen.blit(text,(410,268))
                        
                        inverterWatt = font.render(str(inverterThread.watt_now), True, currentLight, (0,0,0))
                        screen.blit(inverterWatt, (480/2, 380/2))
                        
                        now = datetime.now()
                        timeoutput = font.render(now.strftime("%H:%M:%S"), True, currentLight, (0,0,0))
                        screen.blit(timeoutput, (315, 5))
                        pg.display.flip()
                        clock.tick(25)
                        
                pg.quit()
                sys.exit

if __name__ == '__main__': 
        m = MainClass()
        m.mainloop()
