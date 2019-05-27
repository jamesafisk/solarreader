import sys
import threading
import time
import pygame
import requests
import decimal

running = 1
black = 0, 0, 0
size = width, height = 480, 320
screen = pygame.display.set_mode(size)
box = pygame.image.load("whitebox.png")
boxrect = box.get_rect()
class WeatherServer(threading.Thread):
        temp = 0
        def run(self):
                url = "http://api.openweathermap.org/data/2.5/weather?q=stafford,uk&units=metric&APPID=9e0c2dc0b19e2e83e58cecc273d68cea"
                print("{} started!".format(self.getName()))              # "Thread-x started!"
                print("Getting temp")              # "Thread-x started!"
                r = requests.get(url)
                weatherData = r.json()
                self.temp = weatherData["main"]["temp"]

                print ("The current temp is {}".format(weatherData["main"]["temp"]))

def main():

        mythread = WeatherServer(name = "Thread-Weather getter")  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()

        temp = 16
        showstatus = True
        startTimeForStatus = time.time()
        startTimeForTempUpdate = time.time()
        pygame.font.init()
        font = pygame.font.SysFont("comicsansms", 24)
        clock = pygame.time.Clock()

        # set the center of the rectangular object. 
        while running:
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
                stringtooutput = str(int(temp)) + '\u00b0'
                text = font.render(stringtooutput, True, (255, 255, 255), (0,0,0)) 
                screen.blit(text,(435,5))
                pygame.display.flip()
                clock.tick(60)
if __name__ == '__main__':main()