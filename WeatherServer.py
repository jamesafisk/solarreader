import requests
import threading
import logging
import logging.handlers
import sys
import time

class WeatherServer(threading.Thread):
    temp = 0
    
    def run(self):
        while True:            
            logging.debug('started weather reader')
            try:
                logging.debug('Getting new temp reading.')
                url = "http://api.openweathermap.org/data/2.5/weather?q=stafford,uk&units=metric&APPID=9e0c2dc0b19e2e83e58cecc273d68cea"
                logging.debug('Getting temp')
                r = requests.get(url)
                weatherData = r.json()
                self.temp = weatherData["main"]["temp"]
                time.sleep(60)
            except:
                logging.error("There was an error getting temp.")