from manim import *

class UIComparison(Scene):
    def construct(self):
        before = Text("Before").scale(1.2).shift(LEFT * 3)
        after = Text("After").scale(1.2).shift(RIGHT * 3)

        old_ui = Rectangle(width=3, height=2).set_fill(RED, opacity=0.5).next_to(before, DOWN)
        new_ui = Rectangle(width=3, height=2).set_fill(GREEN, opacity=0.5).next_to(after, DOWN)

        self.play(Write(before), Write(after))
        self.play(Create(old_ui), Create(new_ui))
        self.wait()

        self.play(Transform(old_ui, new_ui), before.animate.set_opacity(0.5), after.animate.set_opacity(1))
        self.wait()
