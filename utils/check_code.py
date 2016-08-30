#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import random
import os



class RandomChar():
    """用于随机生成汉字"""
    chengyu = dict()

    @classmethod
    def get_chengyu(cls):
        chengyu_path = os.path.join(os.path.dirname(__file__), 'chengyu.txt')
        with open(chengyu_path, 'r') as f:
            line_list = f.readlines()
            for line in line_list:
                row = line_list.index(line)
                cls.chengyu[row] = line
        return cls.chengyu
    @staticmethod
    def GB2312():
        num = random.randint(0, 220)
        if not RandomChar.chengyu:
            RandomChar.get_chengyu()

        chengyu = RandomChar.chengyu[num]
        chengyu = chengyu.strip()
        # print chengyu
        return chengyu.decode('utf-8')


class ImageChar():
    def __init__(self, fontColor = (0, 0, 0),
                 size=(100, 40),fontPath='STSONG.TTF' , bgColor=(255, 255, 255), fontSize=20):
        self.size = size
        self.fontPath = fontPath
        self.bgColor = bgColor
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = ImageFont.truetype(self.fontPath, self.fontSize)
        self.image = Image.new('RGB', size, bgColor)

    def rotate(self):
        self.image.rotate(random.randint(0, 30), expand=0)

    def drawText(self, pos, txt, fill):
        draw = ImageDraw.Draw(self.image)
        draw.text(pos, txt, font=self.font, fill=fill)
        del draw

    def randRGB(self):
        return (random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255))

    def randPoint(self):
        (width, height) = self.size
        return (random.randint(0, width), random.randint(0, height))

    def randLine(self, num):
        draw = ImageDraw.Draw(self.image)
        for i in range(0, num):
            draw.line([self.randPoint(), self.randPoint()], self.randRGB())
        del draw

    def randChinese(self, num=4):
        gap = 5
        start = 0
        chengyu = RandomChar().GB2312()
        for i in range(0, num):
            char = chengyu[i]
            # print char
            x = start + self.fontSize * i + random.randint(0, gap) + gap * i
            self.drawText((x, random.randint(-5, 5)),char, self.randRGB())
            self.rotate()
        self.randLine(5)
        return self.image, chengyu

    def save(self,path):
        self.image.save(path)
if __name__ == '__main__':

    l = ImageChar()
    l.randChinese(4)



