#!/usr/bin/env python

from manimlib.imports import *

class A(Scene):
    def construct(self):
        how = TextMobject("如何求解").to_corner(UL)
        tex1 = TexMobject("\\sin x=2", color=YELLOW)
        self.play(Write(how))
        self.play(Write(tex1))
        self.play(tex1.scale, 2.5)
        self.wait()
        self.play(FadeOut(how), tex1.scale, 0.4, tex1.move_to, how)

        tex = [TexMobject("e^{ix}=\\cos x+i\\sin x"),
                TexMobject("e^{-ix}=\\cos x-i\\sin x"),
                TexMobject("e^{ix}-e^{-ix}=2i\\sin x"),
                TexMobject("\\sin x = \\frac{e^{ix}-e^{-ix}}{2i}"),
                TexMobject("\\sin x = \\frac{e^{ix}-e^{-ix}}{2i}=2"),
                TexMobject("e^{ix}-e^{-ix}=4i"),
                TexMobject("t=e^{ix}"),
                TexMobject("t-\\frac{1}{t}=4i"),
                TexMobject("t^2-4it-1=0"),
                TexMobject("t=(2\\pm\\sqrt3)i"),
                TexMobject("e^{ix}=(2\\pm\\sqrt3)i"),
                TexMobject("\\mu=ix"),
                TexMobject("e^\\mu=e^{ix}=\\cos x+i\\sin x=i"),
                TexMobject("\\cos x=0\\ \&\\ \\sin x=1"),
                TexMobject("x=(\\frac{4k+1}{2})\\pi,k\\in \\mathbb{Z}"),
                TexMobject("\\ln i=\\mu=i\\pi(\\frac{4k+1}{2})"),
                TexMobject("ix=\\ln(2\\pm\\sqrt3)+\\ln i=\\ln(2\\pm\\sqrt3)+i\\pi(\\frac{4k+1}{2})"),
                TexMobject("x=(\\frac{4k+1}{2})\\pi-i \\ln(2\\pm\\sqrt3),k\\in \\mathbb{Z}")]

        tex[1].scale(1.1)
        tex[0].move_to(1.1*UP).set_color(GRAY)
        tex[2].move_to(1.1*DOWN).set_color(GRAY)

        self.play(Write(tex[0]), Write(tex[1]), Write(tex[2]))
        for i in range(3, len(tex)):
            tex[i].move_to(tex[i-1]).set_color(GRAY)
            self.play(FadeInFromDown(tex[i]),
                    tex[i-1].move_to, tex[i-2],
                    tex[i-1].scale, 1.1,
                    tex[i-1].set_color, WHITE,
                    tex[i-2].move_to, tex[i-3],
                    tex[i-2].set_color, GRAY,
                    tex[i-2].scale, 1/1.1,
                    FadeOutAndShiftUp(tex[i-3]))
        
        self.play(tex[-3].move_to, 2.2*UP,
                tex[-2].move_to, 1.1*UP,
                tex[-2].scale, 1/1.1,
                tex[-2].set_color, GRAY,
                tex[-1].set_color, YELLOW,
                tex[-1].move_to, 0,
                tex[-1].scale, 1.1)

        self.play(FadeOutAndShiftUp(tex[-3]), FadeOutAndShiftUp(tex[-2]))

        self.wait()
