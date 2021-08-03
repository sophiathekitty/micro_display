import time
import datetime
from Weather import Weather
from Clock import Clock

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont

import urllib.request
import json

class Slideshow:
    def __init__(self):
        self.index = 0
        self.slide_index = 0
        self.delay = 50
        self.delay_step = 0
        self.sunrise = 9
        self.sunset = 22
        self.snooze = 100
        self.snooze_step = 0
        self.state = "unknown"
        self.slides = []
    def Load(self):
        with urllib.request.urlopen("http://localhost/api/settings/?name=slideshow_delay&default=30") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.delay = int(data)
        with urllib.request.urlopen("http://localhost/api/settings/?name=slideshow_snooze&default=100") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.snooze = int(data)
        with urllib.request.urlopen("http://localhost/api/settings/?name=slideshow_sunrise&default=6") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.sunrise = int(data)
        with urllib.request.urlopen("http://localhost/api/settings/?name=slideshow_sunset&default=18") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.sunset = int(data)
        with urllib.request.urlopen("http://localhost/api/settings/?name=current_section_index&default=0") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.index = int(data)
        with urllib.request.urlopen("http://localhost/api/settings/?name=current_slide_index&default=0") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.slide_index = int(data)
        with urllib.request.urlopen("http://localhost/api/settings/?name=room_id&default=1") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.room_id = data
            #print(self.room_id)
            with urllib.request.urlopen("http://localhost/api/rooms/?room_id={}".format(self.room_id)) as json_url:
                buf = json_url.read()
                data = json.loads(buf.decode('utf-8'))
                #print(data['room']['lights_on_in_room'] )
                if(data['room']['lights_on_in_room'] == "1"):
                    self.state = "day"
                if(data['room']['lights_on_in_room'] == "0"):
                    self.state = "night"
        #print (self.state)

        if(len(self.slides) > self.index):
            self.slides[self.index].index = self.slide_index
    def LoadSlides(self):
        self.slides = []
        with urllib.request.urlopen("http://localhost/api/slides?verbose=true") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            for slide in data['sections']:
                if(slide['name'] == "Clock"):
                    self.AddSlide(Clock(),3)
                if(slide['name'] == "Weather"):
                    #weather = Weather()
                    self.AddSlide(Weather(),4)
                print(str(len(self.slides)) + ". " + slide['name'])
    def AddSlide(self, slide, sections = 3):
        self.slides.append(Slide(slide,sections))
    def Next(self):
        #print("Slideshow Next (before) {}".format(self.index))
        self.index += 1
        self.slide_index = 0
        if(self.index >= len(self.slides)):
            self.index = 0
        with urllib.request.urlopen("http://localhost/api/settings?name=current_section_index&value={}".format(self.index)) as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
        with urllib.request.urlopen("http://localhost/api/settings?name=current_slide_index&value={}".format(self.slide_index)) as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
        self.slides[self.index].index = self.slide_index
        self.delay_step = 0
        #print("Slideshow Next (after) {}".format(self.index))
    def Draw(self):
        self.Load()
        self.delay_step += 1
        #print("Slideshow Delay Step {} / {}".format(self.delay_step,self.delay))
        if(self.delay_step > self.delay and self.index > 0):
            self.Next()
        if(self.delay_step > (self.delay * 2) and self.index == 0):
            self.Next()
        # make sure we're in range
        if(self.index >= len(self.slides)):
            self.index = 0
        # and then make sure we actually have slides
        if(len(self.slides) > self.index):
            self.slides[self.index].index = self.slide_index
            return self.slides[self.index].Draw()
        return self.DrawEmpty()
    def DrawEmpty(self):
        icon_path = "null.jpg"
        return Image.open(icon_path)
        
    def DayTime(self):
        #print(self.state)
        if(self.state == "day"):
            return True
        if(self.state == "night"):
            return False
        #print("didn't return?")
        n = datetime.datetime.now()
        h = n.hour
        if(self.sunrise < self.sunset):
            if(h >= self.sunrise and h < self.sunset):
                return True
        elif(h >= self.sunrise or h < self.sunset):
            return True
        return False
    def Snoozed(self):
        if(self.DayTime()):
            return False
        self.snooze_step += 1
        print("snoozing")
        if(self.snooze_step > self.snooze):
            return True
    def Wake(self):
        self.delay_step = 0
        self.snooze_step = 0
class Slide:
    def __init__(self,itm,sections = 1):
        self.itm = itm
        self.sections = sections
        self.index = 0
    def Next(self):
        self.index += 1
        if(self.index >= self.sections):
            self.index = 0
        with urllib.request.urlopen("http://localhost/api/settings?name=current_slide_index&value={}".format(self.index)) as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
    def Draw(self):
        if(self.index > self.sections):
            self.index = 0
        #print("Draw Section Slide: {}".format(self.index))
        if(self.index <= 0):
            return self.itm.Draw()
        elif(self.index == 1):
            return self.itm.Draw2()
        elif(self.index == 2):
            return self.itm.Draw3()
        elif(self.index == 3):
            return self.itm.Draw4()
        elif(self.index >= 4):
            return self.itm.Draw5()
        return self.itm.Draw()