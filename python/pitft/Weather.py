import digitalio
import board

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont

from ColorLerp import ColorLerp
from TextShadow import TextShadow

import urllib.request
import json

class Weather:
    def __init__(self):
        self.Load()
        self.text = TextShadow()
        self.color_lerp = ColorLerp()
    def Load(self):
        with urllib.request.urlopen("http://localhost/plugins/NullWeather/api/weather") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            if(data['weather']['icon'] and data['weather']['icon'] != ""):
                self.icon = data['weather']['icon']
                self.temp = float(data['weather']['temp'])
                self.hum= float(data['weather']['humidity'])
                self.wind= float(data['weather']['wind_speed'])
                self.main = data['weather']['main']
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
    # draw functions
    def Draw(self):
        return self.DrawTemperature()
    def Draw2(self):
        return self.DrawHumidity()
    def Draw3(self):
        return self.DrawWind()
    def Draw4(self):
        return self.DrawWeather()
    def Draw5(self):
        return self.DrawWeather()
    #weather display
    def DrawWeather(self):
        self.Load()
        im_weather = self.WeatherImage()
        draw_weather = ImageDraw.Draw(im_weather)
        x = 4
        self.text.DrawBigText(draw_weather,self.main,self.color_lerp.TempColor(self.temp),x,30)
        return im_weather
    # temperature display
    def DrawTemperature(self):
        self.Load()
        im_weather = self.WeatherImage()
        draw_weather = ImageDraw.Draw(im_weather)
        x = 90
        if(self.temp >= 100):
            x = 30
        self.text.DrawBigText(draw_weather,str(round(self.temp))+"°",self.color_lerp.TempColor(self.temp),x,30)
        return im_weather
    # humidity display
    def DrawHumidity(self):
        self.Load()
        im_weather = self.WeatherImage()
        draw_weather = ImageDraw.Draw(im_weather)
        x = 40
        self.text.DrawBigText(draw_weather,str(round(self.hum))+"%",self.color_lerp.HumColor(self.hum),x,30)
        return im_weather
    # wind display
    def DrawWind(self):
        self.Load()
        im_weather = self.WeatherImage()
        draw_weather = ImageDraw.Draw(im_weather)
        x = 60
        self.text.DrawBigText(draw_weather,str(round(self.wind)),self.color_lerp.WindColor(self.wind),x,30)
        return im_weather
    # weather icon background image
    def WeatherImage(self):
        buttons = ""
        if(self.buttons):
            buttons = "_buttons"
        icon_path = "/var/www/html/python/pitft/weather/"+self.icon+buttons+".jpg"
        return Image.open(icon_path)
