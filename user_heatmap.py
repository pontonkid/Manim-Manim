from manim import *

class UserActivityHeatmap(Scene):
    def construct(self):
        grid = VGroup(*[
            Square(side_length=0.8).set_fill(WHITE, opacity=0.2).set_stroke(BLACK)
            for _ in range(16)
        ])
        grid.arrange_in_grid(4, 4, buff=0.1)

        self.play(*[Create(square) for square in grid])
        self.wait()

        for square in grid:
            self.play(square.animate.set_fill(RED, opacity=0.8), run_time=0.3)
            self.wait(0.1)

        self.wait()
