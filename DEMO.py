#!/usr/bin/env python

from manimlib.imports import *

class A(Scene):
    def construct(self):
        tex1 = TexMobject("e^{ix}-e^{-ix}", "=", "2i\\sin x")
        self.play(Write(tex1))
        self.play(Unwrite(tex1))

        self.wait()

class B(Scene):
    def construct(self):
        tex1 = TexMobject("e^{ix}-e^{-ix}", "=", "2i\\sin x")
        tex2 = TexMobject("2i\\sin x", "=", "e^{ix}-e^{-ix}")
        tex3 = TexMobject("\\sin x =", "\\frac{e^{ix}-e^{-ix}}{2i}")

        self.play(Write(tex1))
        self.play(tex1[0].move_to, tex2[2],
                    tex1[1].move_to, tex2[1],
                    tex1[2].move_to, tex2[0])
        self.play(ReplacementTransform(tex1, tex3))
        
        self.wait()

class C(Scene):
    def construct(self):
        tex = TexMobject("\\sin x =\\frac{e^{ix}-e^{-ix}}{2i}")
        self.add(tex)
        debugTex(self, tex)
        self.wait()

def CTexMobject(str):
    print('test')


class D(Scene):
    def construct(self):
        how = TextMobject("如何求解").scale(3)
        tex1 = TexMobject("\\sin x", "=2", color=YELLOW).scale(5)
        g1 = VGroup(how, tex1)
        g1.arrange(DOWN)
        self.add(g1)
        
        self.wait()

class E(Scene):
    def construct(self):
        text = TextMobject("@烧风")
        self.play(Write(text))
        self.play(Uncreate(text))
        self.wait()

def debugTex(self, tex):
    for i,j in zip(range(len(tex[0])), tex[0]):
        tex_id = TextMobject(str(i)).scale(0.4).set_color(YELLOW).move_to(j)
        self.add(tex_id)