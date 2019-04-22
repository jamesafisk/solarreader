import sys
import threading
import time
import pygame
import requests

#def init_solar():
#    pygame.init()
#    size = width, height = 320, 240
#    speed = [2, 2]
#    black = 0, 0, 0##

#    screen = pygame.display.set_mode(size)

#    ball = pygame.image.load("images.jpg")
#    ballrect = ball.get_rect()

#def gameLoop():
#    while 1:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT: sys.exit()
#                ballrect = ballrect.move(speed)

#            if ballrect.left < 0 or ballrect.right > width:
#                speed[0] = -speed[0]
#            if ballrect.top < 0 or ballrect.bottom > height:
#                speed[1] = -speed[1]

#        screen.fill(black)
#        screen.blit(ball, ballrect)
#        pygame.display.flip()

class WeatherServer(threading.Thread):

        def run(self):
                url = "http://api.openweathermap.org/data/2.5/weather?q=stafford,uk&units=metric&APPID=9e0c2dc0b19e2e83e58cecc273d68cea"
                print("{} started!".format(self.getName()))              # "Thread-x started!"
                print("Getting temp")              # "Thread-x started!"
                r = requests.get(url)
                weatherData = r.json()
                self.temp = weatherData["main"]["temp"]

                print ("The current temp is {}".format(weatherData["main"]["temp"]))
                print ("Finished getting temp")
                print("{} finished!".format(self.getName()))             # "Thread-x finished!"

def main():
        mythread = WeatherServer(name = "Thread-Weather getter")  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread, invoke the run method
        mythread.join()
        print ("The current temp is outsite the thread is {}".format(mythread.temp))
        print ("Main thread ended")
if __name__ == '__main__':main()