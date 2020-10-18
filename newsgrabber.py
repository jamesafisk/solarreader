#!/usr/bin/python3
import requests
import threading
import logging
import logging.handlers
import sys
import time

class ScrollText(object):

    def run(self):
        while True:            
            logging.debug('starting news feed reader')
            try:
                logging.debug('Getting news feed.')
                url = "http://http://feeds.bbci.co.uk/news/uk/rss.xml"
                logging.debug('unpacking news feed')
                r = requests.get(url)
                newsfeeddata = r.json()
                time.sleep(300) # every 5 minutes
            except:
                logging.error("There was an error getting temp.")
