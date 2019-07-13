import requests
import threading

class WeatherServer(threading.Thread):
    temp = 0
    
    def run(self):
            url = "http://api.openweathermap.org/data/2.5/weather?q=stafford,uk&units=metric&APPID=9e0c2dc0b19e2e83e58cecc273d68cea"
            print("{} started!".format(self.getName()))              # "Thread-x started!"
            print("Getting temp")              # "Thread-x started!"
            r = requests.get(url)
            weatherData = r.json()
            self.temp = weatherData["main"]["temp"]