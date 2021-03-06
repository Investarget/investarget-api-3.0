#coding=utf-8
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random


# 随机颜色1:
from invest.settings import APILOG_PATH


def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def rndColor3():
    colorset = [(247, 58, 97), (87, 96, 105), (173, 195, 192), (243, 244, 246), (185, 227, 217)]
    return colorset[random.randint(0,4)]


def makeAvatar(name):
    width = 100
    height = 100
    font = ImageFont.truetype(APILOG_PATH['fontPath'], size=50)
    backcolor = rndColor3()
    image = Image.new('RGB', (width, height), backcolor)
    (letterWidth, letterHeight) = font.getsize(name)
    textY0 = (width - letterHeight - 14) / 2
    textY0 = int(textY0)
    textX0 = int((height - letterWidth) / 2)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    # for x in range(width):
    #     for y in range(height):
    #         draw.point((x, y), fill=backcolor)
    # 输出文字:
    draw.text((textX0, textY0), name, font=font, fill=(255,255,255))
    from third.views.qiniufile import qiniuuploadfile
    image.save(APILOG_PATH['userAvatarPath'], 'jpeg')
    success, url, key = qiniuuploadfile(APILOG_PATH['userAvatarPath'], 'image')
    if success:
        return key
    else:
        return None