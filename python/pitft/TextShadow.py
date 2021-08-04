from PIL import Image, ImageDraw, ImageFont

class TextShadow:
    def __init__(self, big_size = 82, small_size = 24, med_size = 62):
        self.font_big = ImageFont.truetype("/var/www/html/python/pitft/fonts/ViceCitySans.otf", big_size)
        self.font_med = ImageFont.truetype("/var/www/html/python/pitft/fonts/ViceCitySans.otf", med_size)
        self.font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", small_size)
    
    #
    # Draw Big Text
    #
    def DrawBigText(self, draw_obj,txt,f,x,y):
        self.DrawTextBig(draw_obj,txt,f,x,y)
    def DrawTextBig(self, draw_obj,txt,f,x,y):
        draw_obj.text((x-2,y-2), txt, font=self.font_big, fill="#000000")
        draw_obj.text((x+6,y+6), txt, font=self.font_big, fill="#000000")
        draw_obj.text((x-1,y-1), txt, font=self.font_big, fill="#999999")
        draw_obj.text((x+1,y+2), txt, font=self.font_big, fill="#666666")
        draw_obj.text((x,y), txt, font=self.font_big, fill=f)
    #
    # Draw Medium Text
    #
    def DrawMedText(self, draw_obj,txt,f,x,y):
        self.DrawTextMed(draw_obj,txt,f,x,y)
    def DrawTextMed(self, draw_obj,txt,f,x,y):
        draw_obj.text((x-2,y-2), txt, font=self.font_med, fill="#000000")
        draw_obj.text((x+6,y+6), txt, font=self.font_med, fill="#000000")
        draw_obj.text((x-1,y-1), txt, font=self.font_med, fill="#999999")
        draw_obj.text((x+1,y+2), txt, font=self.font_med, fill="#666666")
        draw_obj.text((x,y), txt, font=self.font_med, fill=f)
    #
    # Draw Small Text
    #
    def DrawSmallText(self, draw_obj,txt,f,x,y):
        self.DrawTextSmall(draw_obj,txt,f,x,y)
    def DrawTextSmall(self, draw_obj,txt,f,x,y):
        draw_obj.text((x-1,y-1), txt, font=self.font, fill="#000000")
        draw_obj.text((x+4,y+4), txt, font=self.font, fill="#000000")
        draw_obj.text((x-1,y-1), txt, font=self.font, fill="#999999")
        draw_obj.text((x+1,y+1), txt, font=self.font, fill="#666666")
        draw_obj.text((x,y), txt, font=self.font, fill=f)
