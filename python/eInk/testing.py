#!/usr/bin/env python

from PIL import Image, ImageFont

import urllib.request
import json
import sys
import datetime

import inkyphat


colour = "red"

try:
    inkyphat.set_colour(colour)
except ValueError:
    print('Invalid colour "{}" for V{}\n'.format(colour, inkyphat.get_version()))
    if inkyphat.get_version() == 2:
        sys.exit(1)
    print('Defaulting to "red"')


# figure out the day of week
week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
week_num=datetime.datetime.today().weekday()
print(week_days[week_num])


# figure out what's for dinner
recipe = "Baked Salmon"
side = "Roasted Brussels Sprouts"


with urllib.request.urlopen("http://localhost/plugins/NullWeather/api/weather/live") as json_url:
    buf = json_url.read()
    data = json.loads(buf.decode('utf-8'))
    print(data['weather']['icon'])
    icon = data['weather']['icon']

weather_icon = Image.open("../../plugins/NullWeather/img/eInk/"+icon+".png")
#weather_mask_img = Image.open("../../plugins/NullWeather/img/eInk/02d-mask.png")
weather_mask = inkyphat.create_mask(weather_icon)

font_file = inkyphat.fonts.FredokaOne
#inkyphat.arc((0, 0, 212, 104), 0, 180, 2)
inkyphat.rectangle((0,0,212,24),inkyphat.BLACK)
#inkyphat.rectangle((0,0,212,104),inkyphat.BLACK)
#inkyphat.rectangle((0,20,212,80),inkyphat.WHITE)

top = 0
left = 0
offset_left = 0

font = inkyphat.ImageFont.truetype(font_file, 16)
width, height = font.getsize(week_days[week_num])
inkyphat.text((3, 1), week_days[week_num], inkyphat.WHITE, font=font)


font_size = 28
font = inkyphat.ImageFont.truetype(font_file, font_size)
width, height = font.getsize(recipe)
while width > 202:
    font_size -= 1
    font = inkyphat.ImageFont.truetype(font_file, font_size)
    width, height = font.getsize(recipe)
if(side != ""):
    inkyphat.text((5, 80-height), recipe, inkyphat.RED, font=font)
else:
    inkyphat.text((5, 104-10-height), recipe, inkyphat.RED, font=font)
    
if(side != ""):
    font = inkyphat.ImageFont.truetype(font_file, 10)
    with_width, height = font.getsize("w/")
    inkyphat.text((0, 88), "w/", inkyphat.BLACK, font=font)
    
    font_size = 16
    font = inkyphat.ImageFont.truetype(font_file, font_size)
    width, height = font.getsize(side)
    while with_width+width+5 > 212:
        font_size -= 1
        font = inkyphat.ImageFont.truetype(font_file, font_size)
        width, height = font.getsize(side)

    inkyphat.text((with_width, 82), side, inkyphat.BLACK, font=font)
# Draw the current weather icon over the backdrop
if weather_icon is not None:
    inkyphat.paste(weather_icon, (150, -4), weather_mask)
else:
    font = inkyphat.ImageFont.truetype(font_file, 24)
    inkyphat.text((150, 0), "?", inkyphat.RED, font=font)


inkyphat.show()