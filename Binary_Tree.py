from manim import *

class BinaryTree(Scene):
    def construct(self):
        root = Text("10").move_to(UP * 2)
        left = Text("5").next_to(root, LEFT, buff=1)
        right = Text("15").next_to(root, RIGHT, buff=1)
        left_left = Text("2").next_to(left, LEFT, buff=0.8)
        left_right = Text("7").next_to(left, RIGHT, buff=0.8)

        nodes = VGroup(root, left, right, left_left, left_right)
        edges = VGroup(
            Line(root.get_bottom(), left.get_top()),
            Line(root.get_bottom(), right.get_top()),
            Line(left.get_bottom(), left_left.get_top()),
            Line(left.get_bottom(), left_right.get_top())
        )

        self.play(*[Write(node) for node in nodes])
        self.play(*[Create(edge) for edge in edges])
        self.wait()

        for node in [root, left, left_left, left_right, right]:
            self.play(node.animate.set_color(YELLOW), run_time=0.5)
            self.wait(0.2)

        self.wait()
