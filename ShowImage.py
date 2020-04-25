#!/usr/bin/env python

from manimlib.imports import *
from PIL import Image, ImageFilter, ImageGrab


class A(Scene):
    def construct(self):
        img = ImageMobject("C:/Users/SHAO/Desktop/dsadsd.png").scale(1/1000)
        self.add(img)
        self.play(img.scale,  2000, rate=2)
        self.wait()
