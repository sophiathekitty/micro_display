import digitalio
import board

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont

import urllib.request
import json

from ColorLerp import ColorLerp
from TextShadow import TextShadow

from time import localtime, strftime
#import datetime

class Clock:
    def __init__(self):
        self.Load()
        self.color_lerp = ColorLerp()
        self.text = TextShadow()
    def Load(self):
        self.buttons = False
        with urllib.request.urlopen("http://localhost/api/settings?name=TopButton&default=Up") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            if(data == "Down"):
                self.buttons = True
        with urllib.request.urlopen("http://localhost/api/settings?name=BottomButton&default=Up") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            if(data == "Down"):
                self.buttons = True
            
            #if(data['settings']['day_of_week'] and data['settings']['day_of_week'] != ""):
                #self.day_of_week = data['settings']['day_of_week']
            
        with urllib.request.urlopen("http://localhost/api/settings?name=sunrise_txt&default=06:00") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.sunrise = data
        with urllib.request.urlopen("http://localhost/api/settings?name=sunset_txt&default=18:00") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.sunset = data
    #
    # time of day functions
    #
    def IsDay(self):
        print("is day?")
        srht, srmt = self.sunrise.split(",")
        srh = int(srht)+1
        srm = int(srmt)
        ssht, ssmt = self.sunset.split(",")
        ssh = int(ssht)-1
        ssm = int(ssmt)
        h = int(strftime("%-H", localtime()))
        m = int(strftime("%-M", localtime()))
        print(h+" > "+srh+" and "+h+" < "+ssh)
        if(h > srh and h < ssh):
            return True
        print(h+" == "+srh+" and "+m+" > "+srm)
        if(h == srh and m > srm):
            return True
        print(h+" == "+ssh+" and "+m+" < "+srm)
        if(h == ssh and m < srm ):
            return True
        return False
    def IsMorning(self):
        sht, smt = self.sunrise.split(":")
        sh = int(sht)
        sm = int(smt)
        h = int(strftime("%-H", localtime()))
        m = int(strftime("%-M", localtime()))
        if(h > sh-1 and h < sh+1):
            return True
        if(h == sh-1 and m > sm):
            return True
        if(h == sh and m < sm ):
            return True
        return False
    def IsEvening(self):
        print ("is evening?")
        sht, smt = self.sunset.split(":")
        sh = int(sht)
        sm = int(smt)
        h = int(strftime("%-H", localtime()))
        m = int(strftime("%-M", localtime()))
        print(h+" > "+(sh-1)+" and "+h+" < "+(sh+1))
        if(h > sh-1 and h < sh+1):
            return True
        print(h+" == "+(sh-1)+" and "+m+" > "+sm)
        if(h == sh-1 and m > sm):
            return True
        print(h+" == "+sh+" and "+m+" < "+sm)
        if(h == sh and m < sm ):
            return True
        return False
    #
    # Draw Functions
    #
    def Draw(self):
        return self.DrawTime()
    def Draw2(self):
        return self.DrawDate()
    def Draw3(self):
        return self.DrawSunrise()
    def Draw4(self):
        return self.DrawTime()
    def Draw5(self):
        return self.DrawTime()
    #
    # Get Images
    #
    def GetClockImage(self):
        if(self.buttons):
            icon_path = "clock/night_buttons.jpg"
            if(self.IsMorning()):
                icon_path = "clock/morning_buttons.jpg"
            if(self.IsEvening()):
                icon_path = "clock/evening_buttons.jpg"
            if(self.IsDay()):
                icon_path = "clock/day_buttons.jpg"
        else:
            icon_path = "clock/night.jpg"
            if(self.IsDay()):
                icon_path = "clock/day.jpg"
            if(self.IsMorning()):
                icon_path = "clock/morning.jpg"
            if(self.IsEvening()):
                icon_path = "clock/evening.jpg"
        return Image.open(icon_path)
    # Sunrise image
    def GetSunriseImage(self):
        if(self.buttons):
            icon_path = "clock/sunrise_buttons.jpg"
        else:
            icon_path = "clock/sunrise.jpg"
        return Image.open(icon_path)
    #
    # Draw Time
    #
    def DrawTime(self):
        self.Load()
        im_clock = self.GetClockImage()
        draw_clock = ImageDraw.Draw(im_clock)
        
        # figure ou the time
        h = int(strftime("%I", localtime()))
        m = int(strftime("%M", localtime()))
        a = strftime("%p", localtime())
        date_txt = strftime("%m/%d", localtime())
        time_txt = strftime("%I:%M", localtime())
        if(h < 10):
            if(m < 10):
                time_txt = "{}:0{}".format(h,m)
            else:
                time_txt = "{}:{}".format(h,m)
        # if time is special change color
        f = self.color_lerp.TimeColor(time_txt,a)
        x = 20
        y = 40
        self.text.DrawTextSmall(draw_clock, strftime("%A", localtime()), self.color_lerp.DateColor(date_txt), 4, 4)
        self.text.DrawTextBig(draw_clock, time_txt, f, self.TimeX(time_txt), y)
        return im_clock
    #
    # Draw Date
    #
    def DrawDate(self):
        self.Load()
        im_clock = self.GetClockImage()
        draw_clock = ImageDraw.Draw(im_clock)
        f = "#ffffff"
        
        # figure ou the time
        date_txt = strftime("%m/%d", localtime())
        if(date_txt == "4/04"):
            f = "#adff2f"
        if(date_txt == "4/20"):
            f = "#008000"
        if(date_txt == "7/10"):
            f = "#daa520"
        # if time is special change color
        x = 20
        y = 30
        self.text.DrawTextBig(draw_clock, date_txt, self.color_lerp.DateColor(date_txt), x, y)
        return im_clock
    #
    # Draw Sunrise
    #
    def DrawSunrise(self):
        self.Load()
        im_clock = self.GetSunriseImage()
        draw_clock = ImageDraw.Draw(im_clock)
        f_rise = self.color_lerp.TimeColor(self.sunrise,"AM")
        f_set = self.color_lerp.TimeColor(self.sunset,"PM")
        
        # figure ou the time
        
        # if time is special change color
        x = 55
        self.text.DrawTextMed(draw_clock,self.sunrise,f_rise,x,10)
        self.text.DrawTextMed(draw_clock,self.sunset,f_rise,x,80)
        return im_clock

    def TimeX(self,time_txt):
        x = 20
        thin = 1
        for i in time_txt: 
            if i == '1': 
                thin += 1
        wide = len(time_txt)-1-thin
        x = 120 - (wide*40) - (thin*10)
        return x
