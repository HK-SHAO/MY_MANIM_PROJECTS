#!/usr/bin/env python

from manimlib.imports import *
import numpy

# 随时间变化的波
class A(Scene):
    def construct(self):
        #start, end = 5000000, 5100000 #剪切音频
        with open('mind1.wav', 'rb') as f:
            f.seek(88, 0)
            S = numpy.fromfile(f, '<i2', -1)
            #S = S[start:end]
        length = len(S)

        fs = 60 #视频帧率
        fw = 44100 #wav采样率
        f = int(fs*length/fw) #帧数
        n = int(fw/fs) #每帧的采样数

        lines = [Line() for i in range(n-1)]
        self.add(*lines)

        for i in range(f):
            for j in range(n-1):
                x1 = int(length*(n*i+j)/(f*n))
                y1 = S[x1]/10000
                x2 = int(length*(n*i+(j+1))/(f*n))
                y2 = S[x2]/10000

                x1 = (j/n-0.5)*12
                x2 = ((j+1)/n-0.5)*12

                n1 = np.array((x1,y1,0))
                n2 = np.array((x2,y2,0))
                lines[j].put_start_and_end_on(n1, n2)
            self.wait(1/fs)

# 双声道的波
class C(Scene):
    def construct(self):
        with open('left.wav', 'rb') as f:
            f.seek(88, 0)
            S = numpy.fromfile(f, '<i2', -1)

        with open('right.wav', 'rb') as f:
            f.seek(88, 0)
            S2 = numpy.fromfile(f, '<i2', -1)
        length = len(S)

        fs = 60 #视频帧率
        fw = 44100 #wav采样率
        f = int(fs*length/fw) #帧数
        n = int(fw/fs) #每帧的采样数

        dots = [Dot().scale(0.3) for i in range(n)]
        self.add(*dots)

        for i in range(f):
            for j in range(n):
                x = int(length*(n*i+j)/(f*n))
                y1 = S[x]/10000
                y2 = S2[x]/10000

                dots[j].set_x(y1)
                dots[j].set_y(y2)
            self.wait(1/fs)

class D(Scene):
    def construct(self):
       l = Line()
       self.add(l)
       self.play(ReplacementTransform(l, Line().scale(0.5)), run_time=2)
       self.wait()