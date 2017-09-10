
#coding:utf-8
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
"""
创建四位数的验证码
"""
#产生随机验证码内容
def rndTxt():
    txt = []
    txt.append(random.randint(97,123))      #大写字母
    txt.append(random.randint(65,90))       #小写字母
    txt.append(random.randint(48,57))       #数字
    return chr(txt[random.randint(0,2)])

#随机颜色(背景)
def rndColor1():
    return (random.randint(64, 200), random.randint(64, 200), random.randint(64, 200))

#随机颜色（字体）
def rndColor2():
    return (random.randint(0, 127), random.randint(0, 127), random.randint(0, 127))

#240x60:
width = 180
height = 30
img = Image.new('RGB',(width,height),(0,0,0))
img.save("code0.jpg")
font = ImageFont.truetype(u'Arial.ttf',30)
draw = ImageDraw.Draw(img)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor1())
img.save("code1.jpg")
#输出文字
for txt in range(6):
    draw.text((30*txt+0,0),rndTxt(),font=font,fill=rndColor2())
#模糊化处理
#img = img.filter(ImageFilter.BLUR)
img.save("code.jpg")