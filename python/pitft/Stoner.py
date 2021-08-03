import time
import datetime
import digitalio
import board

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont

import urllib.request
import json


class Stoner:
    def __init__(self):
        self.font_big = ImageFont.truetype("fonts/ViceCitySans.otf", 98)
        self.font_small = ImageFont.truetype("fonts/ViceCitySans.otf", 44)
        self.colorIndex = 0
        self.colors = ["#f26441","#f27f41","#f29441","#f2ae41","#f2dd41","#ecf241","#ccf241","#a8f241","#85f241","#6df241","#44f241","#64f241","#7ff241","#94f241","#c0f241","#e3f241","#f2da41","#f2b441","#f2a041","#f27441"]
        self.color2Index = round(len(self.colors) / 2)
        self.mode = "none"
    def Load(self):
        with urllib.request.urlopen("http://localhost/api/settings/?name=stoner_mode&default=none") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.mode = data

    def StonerTime(self):
        self.Load()
        n = datetime.datetime.now()
        h = n.hour
        m = n.minute
        if((h == 4 or h == 16) and m == 20 and (self.mode == "both" or self.mode == "420")):
            return 420
        if((h == 7 or h == 19) and m == 10 and (self.mode == "both" or self.mode == "710")):
            return 710
        return 0
    def Draw(self):
        if(self.StonerTime() == 420):
            return self.Draw420()
        if(self.StonerTime() == 710):
            return self.Draw710()
        return Image.open("bud.jpg")
        
    def Draw420(self):
        im = Image.open("bud.jpg")
        draw = ImageDraw.Draw(im)
        x = 20
        y = 10
        self.colorIndex += 1
        self.color2Index -= 1
        if(self.colorIndex >= len(self.colors)):
            self.colorIndex = 0
        if(self.color2Index < 0):
            self.color2Index = len(self.colors) - 1
        draw.text((x-2,y-2), "420", font=self.font_big, fill="#000000")
        draw.text((x+4,y+4), "420", font=self.font_big, fill="#000000")
        draw.text((x,y), "420", font=self.font_big, fill=self.colors[self.colorIndex])
        x = 40
        y = 85
        draw.text((x-2,y-2), "Blaze It!!", font=self.font_small, fill="#000000")
        draw.text((x+4,y+4), "Blaze It!!", font=self.font_small, fill="#000000")
        draw.text((x,y), "Blaze It!!", font=self.font_small, fill=self.colors[self.color2Index])
        return im
    def Draw710(self):
        im = Image.open("wax.jpg")
        draw = ImageDraw.Draw(im)
        x = 50
        y = 10
        self.colorIndex += 1
        self.color2Index -= 1
        if(self.colorIndex >= len(self.colors)):
            self.colorIndex = 0
        if(self.color2Index < 0):
            self.color2Index = len(self.colors) - 1
        draw.text((x-2,y-2), "710", font=self.font_big, fill="#000000")
        draw.text((x+4,y+4), "710", font=self.font_big, fill="#000000")
        draw.text((x,y), "710", font=self.font_big, fill=self.colors[self.colorIndex])
        x = 50
        y = 85
        draw.text((x-2,y-2), "Dab It!!", font=self.font_small, fill="#000000")
        draw.text((x+4,y+4), "Dab It!!", font=self.font_small, fill="#000000")
        draw.text((x,y), "Dab It!!", font=self.font_small, fill=self.colors[self.color2Index])
        return im
