#!/usr/bin/env python

from manimlib.imports import *

class A(Scene):
    def construct(self):
        fs = 15 #视频帧率
        y = 1.1

        for i in range(10000):
            dot = Dot().scale(0.3)
            x = 5*i/10000
            y = x*y*(1-y)
            dot.set_x(x-4)
            dot.set_y(y)
            self.add(dot)
            self.wait(1/fs)

class D(Scene):
    def construct(self):
       axes = Axes(x_min=-0.1,y_min=-0.1)
       self.add(axes)
       self.wait()
