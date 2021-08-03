import digitalio
import board

import urllib.request
import json

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont
from Garden import Garden
from Clock import Clock
from Weather import Weather
from Slideshow import Slideshow
from Stoner import Stoner
from Tasks import Tasks

# Configuration for CS and DC pins for Raspberry Pi
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None
BAUDRATE = 64000000  # The pi can be very fast!
# Create the ST7789 display:
display = st7789.ST7789(
    board.SPI(),
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)
# setup backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

display_index = 0
display_switch = 10

im_green = Image.open("null.jpg")
im_blue = Image.open("oblivion.jpg")
im_red = Image.open("malice.jpg")

top_btn = False
bottom_btn = False
menu_btn = False

top_saved = False
bottom_saved = False

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
font_weather = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 82)

# Get drawing object to draw on image.
#tent = Garden(7,"Vegetation Tent","veg")
#closet = Garden(8,"Flower Closet","flower")
#clock = Clock()
#weather = Weather()

slides = Slideshow()
#slides.AddSlide(clock,4)
#slides.AddSlide(weather,4)
#slides.AddSlide(closet,2)
#slides.AddSlide(tent,3)
slides.LoadSlides()
stoner = Stoner()
tasks = Tasks()

# Main loop:
while True:
    #display the image on the screen
    if(stoner.StonerTime() > 0):
        display.image(stoner.Draw(),90)
        backlight.value = True  # turn on backlight
    elif(tasks.HasTasks() and not slides.Snoozed()):
        display.image(tasks.Draw(),90)
        backlight.value = True  # turn on backlight
    elif(slides.Snoozed()):
        slides.Load()
        if(backlight.value):
            slides.LoadSlides()
        backlight.value = False
    else:
        #print("Draw slide {} . {}".format(slides.index,slides.slide_index))
        display.image(slides.Draw(),90)
        backlight.value = True  # turn on backlight
    # handle button inputs
    top_btn = False
    bottom_btn = False
    if buttonA.value and buttonB.value:
        menu_btn = True
    else:
        menu_btn = False
    if buttonB.value and not buttonA.value:  # just button A pressed
        #display.fill(color565(255, 0, 0))  # red
        #display.image(im_red,90)
        #display_index += 1
        #display_switch = 100
        slides.Wake()
        top_btn = True
        print ("top button pressed?")
    if buttonA.value and not buttonB.value:  # just button B pressed
        #display.fill(color565(0, 0, 255))  # blue
        #display.image(im_blue,90)
        #display_switch -= 10
        bottom_btn = True
        slides.Wake()
        #slides.Next()
        print ("top button pressed?")
    if not buttonA.value and not buttonB.value:  # none pressed
        #display.fill(color565(0, 255, 0))  # green
        #display.image(im_green,90)
        #display_index += 1
        top_btn = False
        bottom_btn = False
        print ("no button pressed")
    #display_switch -= 1
    #if(display_switch < 0):
    #    display_switch = 50
    #    display_index += 1
    #loop around
    #if display_index > 2:
    #    display_index = 0
    #print ("{} != {}".format(top_btn,top_saved))
    if top_btn != top_saved:
        print("top button state change")
        # save top button state
        btn_val = "Up"
        if top_btn:
            btn_val = "Down"
        with urllib.request.urlopen("http://localhost/api/settings?id=TopButton&value={}".format(btn_val)) as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            top_saved = top_btn
        if not top_btn:
            slides.Next()
            print("button change slide {}.{}".format(slides.index,slides.slide_index))
    #print ("{} != {}".format(bottom_btn,bottom_saved))
    if bottom_btn != bottom_saved:
        print("bottom button state change")
        # save bottom button state
        btn_val = "Up"
        if bottom_btn:
            btn_val = "Down"
        with urllib.request.urlopen("http://localhost/api/settings?id=BottomButton&value={}".format(btn_val)) as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            bottom_saved = bottom_btn
        if not bottom_btn and slides.index < len(slides.slides):
            slides.slides[slides.index].Next()
            print("button change slide {}.{}".format(slides.index,slides.slides[slides.index].index))

