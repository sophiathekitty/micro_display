import digitalio
import board

from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
from PIL import Image, ImageDraw, ImageFont

from TextShadow import TextShadow

import urllib.request
import json

class Tasks:
    def __init__(self):
        self.confirm_button = False
        self.skip_button = False
        self.Load()
        self.text = TextShadow(82, 24, 36)
    def Load(self):
        with urllib.request.urlopen("http://localhost/api/tasks") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.tasks = []
            if(data['tasks'] != None):
                for task in data['tasks']:
                    self.tasks.append(Task(task))
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

        #with urllib.request.urlopen("http://localhost/api/settings") as json_url:
        #    buf = json_url.read()
        #    data = json.loads(buf.decode('utf-8'))
        #    if(data['settings']['TopButton'] and data['settings']['TopButton'] == "Up"):
        #        if self.confirm_button and not self.skip_button:
        #            self.CompleteTask()
        #        self.confirm_button = False
        #    if(data['settings']['BottomButton'] and data['settings']['BottomButton'] == "up"):
        #        if self.skip_button and not self.confirm_button:
        #            self.SkipTask()
        #        self.skip_button = False
        #    if(data['settings']['TopButton'] and data['settings']['TopButton'] == "Down"):
        #        self.confirm_button = True
        #    if(data['settings']['BottomButton'] and data['settings']['BottomButton'] == "Down"):
        #        self.skip_button = True
    def HasTasks(self):
        self.Load()
        return len(self.tasks) > 0
    def CompleteTask(self):
        if len(self.tasks) == 0:
            return
        task = self.tasks[0]
        print("http://localhost/api/tasks?complete="+task.id)
        with urllib.request.urlopen("http://localhost/api/tasks?complete="+task.id) as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
    def SkipTask(self):
        if len(self.tasks) == 0:
            return
        task = self.tasks[0]
        print("http://localhost/api/tasks?skip="+task.id)
        with urllib.request.urlopen("http://localhost/api/tasks?skip="+task.id) as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
    # show the notifications
    def Draw(self):
        if len(self.tasks) == 0:
            return Image.open("nulltask.jpg")
        if(self.confirm_button):
            im = Image.open("task_complete.jpg")
        elif(self.skip_button):
            im = Image.open("task_complete.jpg")
        else:
            im = Image.open("task.jpg")

        draw = ImageDraw.Draw(im)
        x = 50
        y = 40
        task = self.tasks[0]
        self.text.DrawTextMed(draw,task.name,"#FFFFFF",x,y)
        return im



class Task:
    def __init__(self, json):
        self.id = json['id']
        self.name = json['name']
        self.assigned_to = json['assigned_to']
