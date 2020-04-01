#!/usr/bin/env python

from manimlib.imports import *
import cmath

class A(Scene):
    def construct(self):
        dots = []
        for i in range(100):
            for j in range(100):
                c = cmath.sin(0.1*i+0.1*j*1j) - 2
                d = (c.real**2+c.imag**2)*0.5
                sc = cmath.tanh(abs(d))
                
                dots.append(Square(color=RED, opacity=sc,  side_length=0.01)
                            .move_to(i*0.1*RIGHT+j*0.1*UP))
        gps = VGroup(*dots).move_to(ORIGIN)
        self.add(gps)
        self.wait()

class SurfacesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        