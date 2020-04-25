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


class F(Scene):
    def construct(self):
        text2 = TextMobject("二阶贝塞尔曲线").set_color(YELLOW).move_to(UP)
        text = TextMobject("$(1-k)^2P_0+2k(1-k)P_1+k^2P_2$")
        self.play(Write(text), FadeInFromDown(text2))
        self.wait(2)
        self.play(Unwrite(text), FadeOutAndShiftDown(text2))
        self.wait()


class G(Scene):
    def construct(self):
        text2 = TextMobject("摆线").set_color(YELLOW).move_to(UP)
        text = TexMobject(
            "\\begin{cases}x=a(\\theta-\sin\\theta)\\\\y=a(1-\cos\\theta)\end{cases}")
        self.play(Write(text), FadeInFromDown(text2))
        self.wait(2)
        self.play(Unwrite(text), FadeOutAndShiftDown(text2))
        self.wait()


class H(Scene):
    def construct(self):
        text2 = TextMobject("分岔").set_color(YELLOW).move_to(UP)
        text = TexMobject("X_{n+1}=\\sin(\\mu X_n)")
        self.play(Write(text), FadeInFromDown(text2))
        self.wait(2)
        self.play(Unwrite(text), FadeOutAndShiftDown(text2))
        self.wait()


class R(Scene):
    def construct(self):
        text2 = TextMobject("分形").set_color(YELLOW).move_to(UP)
        text = TextMobject(
            "$z_{n+1}=z_n^2+c$\\\\$M = \\{ c \\in \\mathbb{C} : \\exists s \\in \\mathbb{R}, \\forall n \\in \\mathbb{N}, |z_n| \\leq s \}$")
        self.play(Write(text), FadeInFromDown(text2))
        self.wait(2)
        self.play(Unwrite(text), FadeOutAndShiftDown(text2))
        self.wait()


class I(Scene):
    def construct(self):
        text2 = TextMobject("函数的切线").set_color(YELLOW).move_to(UP)
        text = TexMobject("y=f'(x_0)(x-x_0)+f(x_0)")
        self.play(Write(text), FadeInFromDown(text2))
        self.wait(2)
        self.play(Unwrite(text), FadeOutAndShiftDown(text2))
        self.wait()


class J(Scene):
    def construct(self):
        text2 = TextMobject("黎曼积分").set_color(YELLOW).move_to(UP)
        text = TexMobject(
            "\\int_{a}^{b}f(x)\\mathrm{d}x=\\lim_{n \\to \\infty}{\\sum_{i=1}^{n}{f[a+\\frac{i}{n}(b-a)]\\frac{b-a}{n}}}")
        self.play(Write(text), FadeInFromDown(text2))
        self.wait(2)
        self.play(Unwrite(text), FadeOutAndShiftDown(text2))
        self.wait()


class K(Scene):
    def construct(self):
        text2 = TextMobject("混沌").set_color(YELLOW).move_to(UP)
        text = TexMobject("z^{z^{z^{\\cdot^{\\cdot^{\\cdot}}}}}")
        self.play(Write(text), FadeInFromDown(text2))
        self.wait(2)
        self.play(Unwrite(text), FadeOutAndShiftDown(text2))
        self.wait()


class M(Scene):
    def construct(self):
        text2 = TextMobject("爱心").set_color(YELLOW).move_to(UP)
        text = TexMobject("(x^2+y^2-1)^3<x^2y^3")
        self.play(Write(text), FadeInFromDown(text2))
        self.wait(2)
        self.play(Unwrite(text), FadeOutAndShiftDown(text2))
        self.wait()


class N(Scene):
    def construct(self):
        text = TextMobject("数学=美丽").scale(2)
        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text))
        self.wait()


class L(Scene):
    def construct(self):
        text2 = TextMobject("@烧风")
        text = TextMobject("动画：plotter \& manim 剪辑：blender")
        self.play(Write(text2))
        self.wait()
        self.play(Unwrite(text2))
        self.play(Write(text))
        self.wait()
        self.play(Unwrite(text))

        self.wait()


def debugTex(self, tex):
    for i, j in zip(range(len(tex[0])), tex[0]):
        tex_id = TextMobject(str(i)).scale(0.4).set_color(YELLOW).move_to(j)
        self.add(tex_id)
