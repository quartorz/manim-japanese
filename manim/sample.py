# -*- encoding: utf-8 -*-

from manim import *
import manim_japanese

class Sample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-1.1, 1.1],
        )
        s = axes.plot(lambda x: np.sin(x), color=PINK)
        s_label = MathTex(r'y = \sin x', color=PINK).next_to(s, UP + RIGHT, buff=-1, aligned_edge=RIGHT)
        c = axes.plot(lambda x: np.cos(x), color=BLUE)
        c_label = MathTex(r'y = \cos x', color=BLUE).next_to(s, DOWN + RIGHT, buff=-1, aligned_edge=RIGHT)

        self.play(Create(axes))
        self.play(Create(s), Write(s_label))
        self.play(Create(c), Write(c_label))

        self.wait()