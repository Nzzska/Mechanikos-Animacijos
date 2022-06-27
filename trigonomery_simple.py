from manim import *

class RotatingTriangle(Scene):
    def construct(self):
        triangle = Polygon(
            np.array([-1., -1., 0.]),
            np.array([1., -1., 0.]),
            np.array([1., 1., 0.])
        )
        vertices = triangle.get_vertices()
        angle = Angle(
             line1=Line(start=vertices[0], end=vertices[1]),
             line2=Line(start=vertices[0], end=vertices[2]),
             color=YELLOW
        )

        alp = Tex("$\\alpha$", color=YELLOW).next_to(angle)
        alp.add_updater(lambda m: m.next_to(angle))
        
        a = Tex('a').next_to(triangle, RIGHT)
        b = Tex('b').next_to(triangle, DOWN)
        c = Tex('c').next_to(triangle, UP)

        sin = Tex('$ \\sin{\\alpha} = \\frac{a}{c}$', color=YELLOW).shift(2*RIGHT + UP)
        cos = Tex('$ \\cos{\\alpha} = \\frac{b}{c}$', color=GREEN).shift(2*RIGHT)
        tg = Tex('$ \\tan{\\alpha} = \\frac{a}{b}$', color=RED).shift(2*RIGHT+DOWN)

        trig_funcs = VGroup(sin, cos, tg)

        triangle_group = VGroup(
            triangle, a, b, c, angle
        ).add_updater(
            lambda m, dt: m.rotate(dt)
        ).shift(3*LEFT)

        self.add(
            triangle_group,
            alp,
            trig_funcs
        )

        self.wait(10)