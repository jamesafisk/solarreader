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

running = 1
black = 0, 0, 0
size = width, height = 480, 320
screen = pg.display.set_mode(size)
box = pg.image.load("whitebox.png")
boxrect = box.get_rect()

def main():

        mythread = WeatherServer.WeatherServer(name = "Thread-Weather getter")  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()

        inverterThread = read_solar.InverterCallBack(name = "inverter comms")
        inverterThread.start()

        temp = 0
        showstatus = True
        startTimeForStatus = time.time()
        startTimeForTempUpdate = time.time()
        pg.font.init()
        font = pg.font.SysFont("comicsansms", 32)
        clock = pg.time.Clock()

        # set the center of the rectangular object. 
        while running:
                for event in pg.event.get():
                        if event.type == pg.MOUSEBUTTONUP:
                                None

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
                        
                temp = mythread.temp
                stringtooutput = str(int(temp)) + '\u2103'
                        
                text = font.render(stringtooutput, True, (255, 255, 255), (0,0,0)) 
                screen.blit(text,(430,5))
                pg.display.flip()
                clock.tick(60)

if __name__ == '__main__':main()