from colour import Color
import urllib.request
import json
from time import localtime, strftime

class ColorLerp:
    def __init__(self):
        self.default_color = '#ffffff'

        self.hum_min = '#b1c577'
        self.hum_max = '#054a7f'

        self.wind_min = '#dcf8e7'
        self.wind_max = '#372402'

        self.temp_0 = '#8900d3'
        self.temp_1 = '#8900d3'
        self.temp_2 = '#6300e9'
        self.temp_3 = '#4600fd'
        self.temp_4 = '#4814f9'
        self.temp_5 = '#4a80f4'
        self.temp_6 = '#4cb6f2'
        self.temp_7 = '#e1db51'
        self.temp_8 = '#dec21d'
        self.temp_9 = '#e5921c'
        self.temp_10 = '#f32a1a'
        self.temp_11 = '#aa0000'

        self.fourTwenty = '#008000'
        self.sevenTen = '#daa520'
        self.fourOhFour = '#adff2f'

        self.am = '#ffffcc'
        self.pm = '#ccffff'
        self.oneTwoThreeFour = '#663399'
        self.elevenEleven = '#6495ed'
        self.fourFiveSix = '#f4a460'
        self.oneOneOne = '#d87093'
        self.Load()
    def Load(self):
        with urllib.request.urlopen("http://localhost/api/colors/?pallet=true") as json_url:
            buf = json_url.read()
            data = json.loads(buf.decode('utf-8'))
            self.default_color = data['pallet']['general']['display']['default']

            self.hum_min = data['pallet']['weather']['humidity']["0"]
            self.hum_max = data['pallet']['weather']['humidity']["1"]

            self.wind_min = data['pallet']['weather']['wind']["0"]
            self.wind_max = data['pallet']['weather']['wind']["1"]

            self.temp_0 = data['pallet']['weather']['temperature']["0"]
            self.temp_1 = data['pallet']['weather']['temperature']["1"]
            self.temp_2 = data['pallet']['weather']['temperature']["2"]
            self.temp_3 = data['pallet']['weather']['temperature']["3"]
            self.temp_4 = data['pallet']['weather']['temperature']["4"]
            self.temp_5 = data['pallet']['weather']['temperature']["5"]
            self.temp_6 = data['pallet']['weather']['temperature']["6"]
            self.temp_7 = data['pallet']['weather']['temperature']["7"]
            self.temp_8 = data['pallet']['weather']['temperature']["8"]
            self.temp_9 = data['pallet']['weather']['temperature']["9"]
            self.temp_10 = data['pallet']['weather']['temperature']["10"]
            self.temp_11 = data['pallet']['weather']['temperature']["11"]

            self.fourTwenty = data['pallet']['stoner']['fourTwenty']
            self.sevenTen = data['pallet']['stoner']['sevenTen']
            self.fourOhFour = data['pallet']['stoner']['fourOhFour']

            self.am = data['pallet']['clock']['am']
            self.pm = data['pallet']['clock']['pm']
            self.oneTwoThreeFour = data['pallet']['clock']['oneTwoThreeFour']
            self.elevenEleven = data['pallet']['clock']['elevenEleven']
            self.fourFiveSix = data['pallet']['clock']['fourFiveSix']
            self.oneoneone = data['pallet']['clock']['oneOneOne']
            
            self.sativa = data['pallet']['strains']['sativa']
            self.sativaHybrid = data['pallet']['strains']['sativaHybrid']
            self.hybrid = data['pallet']['strains']['hybrid']
            self.indicaHybrid = data['pallet']['strains']['indicaHybrid']
            self.indica = data['pallet']['strains']['indica']


    def DateColor(self,date_txt):
        self.Load()
        f = self.default_color
        if(date_txt == "4/04"):
            f = self.fourOhFour
        if(date_txt == "4/20"):
            f = self.fourTwenty
        if(date_txt == "7/10"):
            f = self.sevenTen
        return f
    def TimeColor(self,time_txt,a):
        self.Load()
        f = self.default_color
        if(a == "AM"):
            f = self.am
        if(a == "PM"):
            f = self.pm
        if(time_txt == "4:04"):
            f = self.fourOhFour
        if(time_txt == "4:20"):
            f = self.fourTwenty
        if(time_txt == "7:10"):
            f = self.sevenTen
        if(time_txt == "12:34"):
            f = self.oneTwoThreeFour
        if(time_txt == "11:11"):
            f = self.elevenEleven
        if(time_txt == "1:23" or time_txt == "2:34" or time_txt == "3:45" or time_txt == "4:56"):
            f = self.fourFiveSix
        if(time_txt == "1:11" or time_txt == "2:22" or time_txt == "3:33" or time_txt == "4:44" or time_txt == "5:55"):
            f = self.oneOneOne
        return f
    # temperature color
    def TempColor(self,temp):
        self.Load()
        t = int(temp/10)
        s = temp - (t*10)
        f1 = self.default_color
        if(t < 0):
            f = self.temp_0
        elif(t == 0):
            f = self.ColorLerp(self.temp_0, self.temp_1, s)
        elif(t == 1):
            f = self.ColorLerp(self.temp_1, self.temp_2, s)
        elif(t == 2):
            f = self.ColorLerp(self.temp_2, self.temp_3, s)
        elif(t == 3):
            f = self.ColorLerp(self.temp_3, self.temp_4, s)
        elif(t == 4):
            f = self.ColorLerp(self.temp_4, self.temp_5, s)
        elif(t == 5):
            f = self.ColorLerp(self.temp_5, self.temp_6, s)
        elif(t == 6):
            f = self.ColorLerp(self.temp_6, self.temp_7, s)
        elif(t == 7):
            f = self.ColorLerp(self.temp_7, self.temp_8, s)
        elif(t == 8):
            f = self.ColorLerp(self.temp_8, self.temp_9, s)
        elif(t == 9):
            f = self.ColorLerp(self.temp_9, self.temp_10, s)
        elif(t == 10):
            f = self.ColorLerp(self.temp_10, self.temp_11, s)
        elif(t > 10):
            f = self.temp_11
        return f
    
    # humidity color
    def HumColor(self,hum):
        self.Load()
        hum = round(hum)
        if(hum < 0):
            hum = 0
        if(hum > 100):
            hum = 100
        return self.ColorLerp(self.hum_min, self.hum_max, hum, 100)
    
    # wind color
    def WindColor(self,wind):
        self.Load()
        wind = round(wind)
        if(wind < 0):
            wind = 0
        if(wind > 50):
            wind = 50
        return self.ColorLerp(self.wind_min, self.wind_max,wind,50)
    # color lerp
    def ColorLerp(self,color1,color2,step,count = 10):
        count += 1
        c1 = Color(color1)
        c2 = Color(color2)
        colors = list(c1.range_to(c2,count))
        step = int(step)
        i = 0

        if int(step) < len(colors):
            return colors[int(step)].hex_l
        for color in colors:
            if i == int(step):
                return color.hex_l
        print ("return color 1?!")
        return color1