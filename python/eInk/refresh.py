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




# find the old values
with urllib.request.urlopen("http://localhost/api/settings/?name=eInk_date") as json_url:
    buf = json_url.read()
    old_date = json.loads(buf.decode('utf-8'))
    print(old_date)
# find the old values
with urllib.request.urlopen("http://localhost/api/settings/?name=eInk_weather_icon") as json_url:
    buf = json_url.read()
    old_weather_icon = json.loads(buf.decode('utf-8'))
    print(old_weather_icon)
# find the old values
with urllib.request.urlopen("http://localhost/api/settings/?name=eInk_forecast_icon") as json_url:
    buf = json_url.read()
    old_forecast_icon = json.loads(buf.decode('utf-8'))
    print(old_forecast_icon)
# find the old values
with urllib.request.urlopen("http://localhost/api/settings/?name=eInk_recipe") as json_url:
    buf = json_url.read()
    old_recipe = json.loads(buf.decode('utf-8'))
    if old_recipe :
        old_recipe = old_recipe.replace("&apos;","'")
    print(old_recipe)
# find the old values
with urllib.request.urlopen("http://localhost/api/settings/?name=eInk_side") as json_url:
    buf = json_url.read()
    old_side = json.loads(buf.decode('utf-8'))
    print(old_side)



# figure out the day of week
week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
week_num=datetime.datetime.today().weekday()
day_of_week = week_days[week_num]

# figure out what's for dinner
recipe = ""
side = ""
with urllib.request.urlopen("http://localhost/extensions/MealPlanner/api/meal/") as json_url:
    buf = json_url.read()
    data = json.loads(buf.decode('utf-8'))
    recipe = data['today']['recipe']['name']
    side_id = data['today']['side_id']
    if(data['today']['side_id'] != "0"):
        side = data['today']['side']['name']
recipe = recipe.replace("&apos;","'")
side = side.replace("&apos;","'")

with urllib.request.urlopen("http://localhost/plugins/NullWeather/api/weather/live") as json_url:
    buf = json_url.read()
    data = json.loads(buf.decode('utf-8'))
    icon = data['weather']['icon']

with urllib.request.urlopen("http://localhost/plugins/NullWeather/api/forecast/simple") as json_url:
    buf = json_url.read()
    forecast = json.loads(buf.decode('utf-8'))



print(day_of_week)
print(icon)
print(forecast)
print(recipe)
print(side_id)
if old_weather_icon != icon:
    print("icon is different")
if old_forecast_icon != forecast:
    print("forecast is different")
if old_date != day_of_week:
    print("day is different")
if old_recipe != recipe:
    print("recipe is different")
if old_side != side_id:
    print("side is different")
# see if the data has changed
if(old_weather_icon != icon or old_forecast_icon != forecast or old_date != day_of_week or old_recipe != recipe or old_side != side_id):
    # if anything has changed refresh
    weather_icon = Image.open("../../plugins/NullWeather/img/eInk/"+icon+".png")
    weather_mask = inkyphat.create_mask(weather_icon)
    if(forecast != "clear"):
        forecast_icon = Image.open("../../plugins/NullWeather/img/eInk/"+forecast+".png")
        #forecast_icon_mask = Image.open("../../plugins/NullWeather/img/eInk/"+forecast+"-mask.png")
        forecast_mask = inkyphat.create_mask(forecast_icon)
    font_file = inkyphat.fonts.FredokaOne
    inkyphat.rectangle((0,0,212,24),inkyphat.BLACK)

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
    if forecast != "clear":
        inkyphat.paste(forecast_icon, (132, 0), forecast_mask)
    if weather_icon is not None:
        inkyphat.paste(weather_icon, (150, -4), weather_mask)
    else:
        font = inkyphat.ImageFont.truetype(font_file, 24)
        inkyphat.text((150, 0), "?", inkyphat.RED, font=font)


    inkyphat.show()

    # find the old values
    with urllib.request.urlopen("http://localhost/api/settings/?name=eInk_date&value="+day_of_week) as json_url:
        buf = json_url.read()
        old_date = json.loads(buf.decode('utf-8'))
        print(old_date)
    # find the old values
    with urllib.request.urlopen("http://localhost/api/settings/?name=eInk_weather_icon&value="+icon) as json_url:
        buf = json_url.read()
        old_weather_icon = json.loads(buf.decode('utf-8'))
        print(old_weather_icon)
    with urllib.request.urlopen("http://localhost/api/settings/?name=eInk_forecast_icon&value="+forecast) as json_url:
        buf = json_url.read()
        old_forecast_icon = json.loads(buf.decode('utf-8'))
        print(old_forecast_icon)
    # find the old values
    recipe = recipe.replace(" ","%20")
    with urllib.request.urlopen("http://localhost/api/settings/?name=eInk_recipe&value="+recipe) as json_url:
        buf = json_url.read()
        old_recipe = json.loads(buf.decode('utf-8'))
        print(old_recipe)
    # find the old values
    with urllib.request.urlopen("http://localhost/api/settings/?name=eInk_side&value="+side_id) as json_url:
        buf = json_url.read()
        old_side = json.loads(buf.decode('utf-8'))
        print(old_side)