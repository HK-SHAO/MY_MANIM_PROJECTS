#!/usr/bin/env python

from manimlib.imports import *


class A(Scene):
    def construct(self):
        how = TextMobject("如何求解")
        tex1 = TexMobject("\\sin x", "=2", color=YELLOW)

        self.play(Write(how))
        self.play(how.to_corner, UL, Write(tex1))
        self.play(tex1.scale, 2.5)
        self.wait()
        self.play(FadeOut(how),
                  tex1.scale, 0.4,
                  tex1.to_corner, UL)

        tex2 = TextMobject("$e^{ix}=\\cos x+i\\sin x$\\\\",
                           "$e^{-ix}=\\cos x-i\\sin x$")
        tex3 = TexMobject("e^{ix}-e^{-ix}", "=", "2i\\sin x")
        tex31 = TexMobject("2i\\sin x", "=", "e^{ix}-e^{-ix}")
        tex4 = TexMobject("\\sin x", "=\\frac{e^{ix}-e^{-ix}}{2i}")
        tex5 = TexMobject("\\sin x= \\frac{e^{ix}-e^{-ix}}{2i}", "=2")

        tipt1 = TextMobject("使用欧拉公式").scale(0.5).to_corner(DR)
        self.play(Write(tipt1))
        self.play(Write(tex2[0]))
        tipt11 = TextMobject("将$x$换为$-x$").scale(0.5).to_corner(DR)
        self.wait()
        self.play(ReplacementTransform(tex2[0].copy(), tex2[1]),
                  ReplacementTransform(tipt1, tipt11))
        tipt2 = TextMobject("两式相减").scale(0.5).to_corner(DR)
        self.wait()
        self.remove(tex2)
        self.play(ReplacementTransform(tex2[0][0:3], tex3[0][0:3]),
                  ReplacementTransform(tex2[1][0:4], tex3[0][4:8]),
                  tex2[0][9:14].move_to, tex3[2][1:6],
                  tex2[0][3].move_to, tex3[1],
                  tex2[1][4].move_to, tex3[1],
                  tex2[1][10:15].move_to, tex3[2][1:6],
                  Transform(VGroup(tex2[0][-6], tex2[1][-6]), tex3[2][0]),
                  FadeOut(tex2[0][4:8]),
                  FadeOut(tex2[1][5:9]),
                  FadeIn(tex3[0][3]),
                  ReplacementTransform(tipt11, tipt2))
        self.wait()
        self.clear()
        self.add(tex1.to_corner(UL))
        tipt3 = TextMobject("分离$\\sin x$").scale(0.5).to_corner(DR)
        self.play(tex3[0].move_to, tex31[2],
                  tex3[1].move_to, tex31[1],
                  tex3[2].move_to, tex31[0],
                  ReplacementTransform(tipt2, tipt3))

        self.play(tex3[2][0:2].move_to, tex4[1][10:12],
                  tex3[1].move_to, tex4[1][0],
                  tex3[2][2:6].move_to, tex4[0],
                  FadeIn(tex4[1][9]),
                  ReplacementTransform(tex3[0], tex4[1][1:9]))
        self.wait()
        self.clear()
        self.add(tex1.to_corner(UL), tipt3)

        t1c = tex1[1].copy()
        t10c = tex1[0].copy()
        self.play(tex4.move_to, tex5[0],
                  Transform(t10c, tex5[0][0:4]),
                  t1c.move_to, tex5[1],
                  t1c.set_color, WHITE)
        self.wait()

        tipt4 = TextMobject("去分母").scale(0.5).to_corner(DR)
        tex2 = TexMobject("\\sin x=", "\\frac{e^{ix}-e^{-ix}}{2i}=2")
        tex3 = TexMobject("e^{ix}-e^{-ix}", "=", "4i")
        self.clear()
        self.add(tex1.to_corner(UL), tex2)
        self.play(ReplacementTransform(tex2[1][0:8], tex3[0]),
                  FadeOut(tex2[0]),
                  Transform(tex2[1][11:13], tex3[1]),
                  FadeOut(tex2[1][8]),
                  Transform(tex2[1][9:11], tex3[2]),
                  ReplacementTransform(tipt3, tipt4))
        self.wait()
        self.clear()
        g1 = VGroup(tex1, TexMobject("t=e^{ix}"))
        g1.arrange(DOWN).to_corner(UL)

        tex3 = TexMobject("e^{ix}-e^{-ix}", "=4i")
        self.add(tex1, tex3)
        tex4 = TexMobject("t=e^{ix}").move_to(DOWN)
        tex5 = TexMobject("t-t^{-1}=4i")
        tipt5 = TextMobject("令").scale(0.5).to_corner(DR)
        self.play(Write(tex4), ReplacementTransform(tipt4, tipt5))
        self.wait()

        tipt6 = TextMobject("换元").scale(0.5).to_corner(DR)
        self.play(FadeOut(tex3[0][0:3]),
                  ReplacementTransform(tex3[0][3], tex5[0][1]),
                  FadeOut(tex3[0][4:8]),
                  ReplacementTransform(tex4[0][0].copy(), tex5[0][0]),
                  ReplacementTransform(tex4[0][0].copy(), tex5[0][2:5]),
                  ReplacementTransform(tex3[1], tex5[0][5:8]),
                  ReplacementTransform(tipt5, tipt6))

        tex6 = TexMobject("t^2-4it-1=0")
        tex7 = TexMobject("t=(2\\pm\\sqrt3)i").move_to(DOWN)
        tex8 = TexMobject(
            "x={-b \\pm \\sqrt{b^2-4ac} \\over 2a}").to_corner(DOWN)

        tipt7 = TextMobject("使用求根公式").scale(0.5).to_corner(DR)
        self.play(tex4.move_to, g1[1])
        self.wait()
        tipt61 = TextMobject("整理成二次方程").scale(0.5).to_corner(DR)
        self.play(ReplacementTransform(tex5, tex6),
                  ReplacementTransform(tipt6, tipt61))
        self.wait()
        self.play(Write(tex8), ReplacementTransform(tipt61, tipt7))
        self.wait()
        tipt8 = TextMobject("解得").scale(0.5).to_corner(DR)
        self.play(ReplacementTransform(tex8, tex7),
                  ReplacementTransform(tipt7, tipt8))

        self.wait()


class B(Scene):
    def construct(self):
        tex1 = TexMobject("\\sin x", "=2", color=YELLOW)

        g1 = VGroup(tex1, TexMobject("t=e^{ix}"))
        g1.arrange(DOWN).to_corner(UL)
        tex4 = TexMobject("t=", "e^{ix}").move_to(g1[1])
        tex6 = TexMobject("t^2-4it-1=0")
        tex7 = TexMobject("t", "=(2\\pm\\sqrt3)i").move_to(DOWN)
        tipt8 = TextMobject("解得").scale(0.5).to_corner(DR)
        self.add(tex1, tex4, tex6, tex7, tipt8)
        tex8 = TexMobject("e^{ix}", "=(2\\pm\\sqrt3)i")
        tipt9 = TextMobject("即").scale(0.5).to_corner(DR)
        self.play(FadeOut(tex7[0][0]),
                  FadeOut(tex6),
                  tex7[1].move_to, tex8[1],
                  tex4[1].copy().move_to, tex8[0],
                  ReplacementTransform(tipt8, tipt9))

        self.clear()
        tex1 = TexMobject("\\sin x", "=2", color=YELLOW)
        g1 = VGroup(tex1, TexMobject("t=e^{ix}"))
        g1.arrange(DOWN).to_corner(UL)
        tex4 = TexMobject("t=", "e^{ix}").move_to(g1[1])
        tex8 = TexMobject("e^{ix}", "=", "(2\\pm\\sqrt3)i")
        tipt9 = TextMobject("即").scale(0.5).to_corner(DR)
        self.add(tex1, tex4, tex8, tipt9)
        tex9 = TexMobject("{\\rm Ln}(e^{ix})", "=",
                          "{\\rm Ln}[(2\\pm\\sqrt3)i]")
        tipt10 = TextMobject("两边同时取对数").scale(0.5).to_corner(DR)
        self.wait()
        self.play(tex8[0].move_to, tex9[0][3:6],
                  tex8[1].move_to, tex9[1],
                  tex8[2].move_to, tex9[2][3:11],
                  ReplacementTransform(tipt9, tipt10))
        self.play(FadeIn(tex9))
        self.remove(tex8)
        tex10 = TexMobject("ix=\\ln(2\\pm\\sqrt3)+{\\rm Ln}\\ i")
        tipt11 = TextMobject("化简").scale(0.5).to_corner(DR)
        self.wait()
        self.play(FadeOut(tex9[0][0:4]),
                  FadeOut(tex9[0][6]),
                  ReplacementTransform(tex9[0][4:6], tex10[0][0:2]),
                  ReplacementTransform(tex9[2][0:2].copy(), tex10[0][-3:-1]),
                  ReplacementTransform(tex9[1], tex10[0][2]),
                  ReplacementTransform(tex9[2][0:2], tex10[0][3:5]),
                  ReplacementTransform(tex9[2][3:10], tex10[0][5:12]),
                  ReplacementTransform(tex9[2][-2], tex10[0][-1]),
                  ReplacementTransform(
                      VGroup(tex9[2][2], tex9[2][11]), tex10[0][-4]),
                  ReplacementTransform(tipt10, tipt11))
        self.wait()
        self.play(FadeOut(g1), FadeOut(tipt11),
                  FadeOut(tex4), tex10.to_corner, UP)
        self.clear()
        tex10 = TexMobject("ix=\\ln(2\\pm\\sqrt3)+{\\rm Ln}\\ i").to_corner(UP)
        self.add(tex10)
        text1 = TextMobject("似乎离成功只剩下一步了\\\\但是${\\rm Ln}\\ i$等于什么呢？")
        self.play(Write(text1))
        self.wait()
        self.wait()
        text2 = TextMobject(
            "令\\ $i\\theta={\\rm Ln}\\ i$\\\\利用欧拉公式\\ $e^{i\\theta}=\\cos \\theta+i\\sin \\theta$\\\\可以得到")
        self.play(FadeOut(text1))
        self.play(Write(text2))
        self.wait()
        self.wait()
        self.play(FadeOut(text2))
        tex3 = TexMobject("\\cos \\theta+i\\sin \\theta=e^{\\rm{Ln \\ i}}=i")
        tex4 = TexMobject("\\cos\\theta=0\\ \\&\\ \\sin\\theta=1")
        tex5 = TexMobject("\\theta=(\\frac{4k+1}{2})\\pi,k\\in \\mathbb{Z}")
        tex6 = TexMobject(
            "{\\rm Ln}\\ i=i\\theta=i(\\frac{4k+1}{2})\\pi").set_color(YELLOW)
        gp = VGroup(tex3, tex4, tex5, tex6).arrange(DOWN)
        self.play(Write(tex3))
        self.play(Write(tex4))
        self.play(Write(tex5))
        self.play(Write(tex6))
        self.wait()
        self.wait()
        self.wait()
        tex7 = TexMobject("ix=\\ln(2\\pm\\sqrt3)+", "i(\\frac{4k+1}{2})\\pi")
        self.play(FadeOut(tex3), FadeOut(tex4), FadeOut(tex5),
                  FadeOut(tex10[0][13:]),
                  FadeOut(tex6[0][0:7]),
                  ReplacementTransform(tex10[0][0:13], tex7[0]),
                  ReplacementTransform(tex6[0][7:], tex7[1]))
        self.clear()
        tex7 = TexMobject("ix", "=", "\\ln(2\\pm\\sqrt3)",
                          "+", "i(\\frac{4k+1}{2})\\pi")
        tex8 = TexMobject(
            "ix", "=", "i(\\frac{4k+1}{2})\\pi", "+", "\\ln(2\\pm\\sqrt3)")
        self.play(tex7[0].move_to, tex8[0],
                  tex7[1].move_to, tex8[1],
                  tex7[2].move_to, tex8[4],
                  tex7[3].move_to, tex8[3],
                  tex7[4].move_to, tex8[2])
        tex9 = TexMobject("x", "=", "(\\frac{4k+1}{2})\\pi", "-i",
                          "\\ln(2\\pm\\sqrt3)", ",k\\in \\mathbb{Z}").set_color(YELLOW)
        self.play(FadeOut(tex7[0][0]), FadeOut(tex7[4][0]),
                  ReplacementTransform(tex7[3], tex9[3]),
                  ReplacementTransform(tex7[2], tex9[4]),
                  ReplacementTransform(tex7[1], tex9[1]),
                  ReplacementTransform(tex7[4][1:], tex9[2]),
                  ReplacementTransform(tex7[0][1], tex9[0]))
        self.play(Write(tex9[-1]), Write(tex1))
        self.wait()
        self.wait()
        self.wait()
        self.play(FadeOut(tex9), FadeOut(tex1))


class C(Scene):
    def construct(self):
        text1 = TextMobject("$\sin x=2$\\\\", """$e^{ix}=\\cos x+i\\sin x$\\\\
$e^{-ix}=\\cos x-i\\sin x$\\\\
$e^{ix}-e^{-ix}=2i\\sin x$\\\\
$\\sin x = \\frac{e^{ix}-e^{-ix}}{2i}$\\\\
$\\frac{e^{ix}-e^{-ix}}{2i}=2$\\\\
$e^{ix}-e^{-ix}=4i$\\\\
$t=e^{ix}$\\\\
$t-\\frac{1}{t}=4i$\\\\
$t^2-4it-1=0$\\\\
$t=(2\\pm\\sqrt3)i$\\\\
$e^{ix}=(2\\pm\\sqrt3)i$\\\\
${\\rm Ln}(e^{ix})={\\rm Ln}[(2\\pm\\sqrt3)i]$""").scale(0.8).to_corner(LEFT)

        text2 = TextMobject("""
$ix=\\ln(2\\pm\\sqrt3)+{\\rm Ln}\\ i$\\\\
$i\\theta={\\rm Ln}\\ i$\\\\
$e^{i\\theta}=\\cos \\theta+i\\sin \\theta$\\\\
$\\cos \\theta+i\\sin \\theta=e^{\\rm{Ln \\ i}}=i$\\\\
$\\begin{cases}\\cos \\theta=0\\\\\\sin \\theta=1\\end{cases}$\\\\
$\\cos\\theta=0\\ \\&\\ \\sin\\theta=1$\\\\
$\\theta=(\\frac{4k+1}{2})\\pi,k\\in \\mathbb{Z}$\\\\
${\\rm Ln}\\ i=i\\theta=i\\pi(\\frac{4k+1}{2})$\\\\
$ix=\\ln(2\\pm\\sqrt3)+i\\pi(\\frac{4k+1}{2})$\\\\""",
                            "$x=(\\frac{4k+1}{2})\\pi-i\\ln(2\\pm\\sqrt3),k\\in \\mathbb{Z}$").scale(0.8).to_corner(RIGHT)

        text1[0].set_color(YELLOW)
        text2[-1].set_color(YELLOW)

        self.play(FadeIn(text1))
        self.play(FadeIn(text2))
        self.wait()
        self.wait()
        self.wait()
        self.wait()
        self.play(FadeOut(text1), FadeOut(text2))


class D(Scene):
    def construct(self):
        text = TextMobject("建议根据自己情况暂停或者二倍速")
        self.play(Write(text))
        self.wait()
        self.play(Uncreate(text))
