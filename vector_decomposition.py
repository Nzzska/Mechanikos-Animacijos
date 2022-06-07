from manim import *

class VectorDecomposition(Scene):
    def construct(self):

        x_len = ValueTracker(2)
        y_len = ValueTracker(1)

        ax = Axes(
            x_range=[-4, 4, 2],
            y_range=[-4, 4, 2],
            axis_config={"include_numbers": True},

        )

        #Vectors part

        vec = Vector(
            np.array([
                x_len.get_value(), 
                y_len.get_value(), 
                0.
            ]),
            color=RED
        ).add_updater(
            lambda m: m.become(
                Vector(
                    np.array([
                        x_len.get_value(),
                        y_len.get_value(),
                        0.
                    ]),
                    color=RED
                )
            )
        )

        x_component = Vector(
            np.array([x_len.get_value(), 0, 0.]),
            color=GREEN
        ).add_updater(
            lambda m: m.become(
                Vector(
                    np.array([x_len.get_value(), 0, 0.]),
                    color=GREEN
                )
            )
        )
        y_component = Vector(
            np.array([0., y_len.get_value(), 0.]),
            color=GREEN
        ).add_updater(
            lambda m: m.become(
                Vector(
                    np.array([0., y_len.get_value(), 0.]),
                    color=GREEN
                )
            )
        )

        #Lines
        vec_to_y = DashedLine(
            start=np.array(
                [x_len.get_value(), y_len.get_value(), 0.]
            ),
            end=np.array([0., y_len.get_value(), 0.])
        ).add_updater(
            lambda m: m.become(
                DashedLine(
                    start=np.array(
                        [x_len.get_value(), y_len.get_value(), 0.]
                    ),
                    end=np.array([0., y_len.get_value(), 0.])
                )
            )
        )

        vec_to_x = DashedLine(
            start=np.array(
                [x_len.get_value(), y_len.get_value(), 0.]
            ),
            end=np.array([x_len.get_value(), 0., 0.])
        ).add_updater(
            lambda m: m.become(
                DashedLine(
                    start=np.array(
                        [x_len.get_value(), y_len.get_value(), 0.]
                    ),
                    end=np.array([x_len.get_value(), 0., 0.])
                )
            )
        )
        
        #angle
        line_along_x = Line(
            start=np.array([0., 0., 0.]),
            end=np.array([1., 0., 0.])
        )

        angle = Angle(line_along_x, vec, color=RED)
        angle.add_updater(
            lambda m: m.become(
                Angle(line_along_x, vec, color=RED)
            )
        )

        #labels
        vec_label = Tex("$\\vec{V}$", color=RED).next_to(vec)
        vec_label.add_updater(
            lambda m: m.next_to(vec)
        )
        angle_label = Tex("$\\alpha$").scale(0.75).next_to(angle, UP)
        angle_label.set(color=RED)
        angle_label.add_updater(lambda m: m.next_to(angle))
        x_comp_label = Tex("$\\vec{V_x}$", color=GREEN).next_to(x_component, DOWN)
        x_comp_label.add_updater(
            lambda m: m.next_to(x_component, DOWN)
        )
        y_comp_label = Tex("$\\vec{V_y}$", color=GREEN).next_to(y_component, UP)
        y_comp_label.add_updater(
            lambda m: m.next_to(y_component, UP)
        )
        labels = VGroup(
            vec_label,
            angle_label,
            x_comp_label,
            y_comp_label
        )
        
        #Equations
        x_comp_equation = Tex(
            "$V_x = V cos(\\alpha)$",
            color=GREEN
        ).shift(4*LEFT + 3*UP)
        y_comp_equation = Tex(
            "$V_y = V sin(\\alpha)$",
            color=GREEN
        ).shift(4*LEFT + 2*UP)

        atmintine = Tex(
            """\n
                !! Jeigu simbolis yra su rodiklytė, kaip $\\vec{V}$, \n
                tai reiškia, vektorių. Jeigu rodyklės nėra $V$ \n
                kalba eina apie vektoriaus ilgį (skaliarinis dydis) !!
            """, color=RED
        ).scale(0.5).shift(3*RIGHT+2*DOWN)

        #animations
        self.play(
            FadeIn(ax)
        )
        self.play(
            Write(vec),
        )
        self.play(
            FadeIn(vec_to_x),
            FadeIn(vec_to_y),
            Write(x_component),
            Write(y_component),
            Write(angle)
        )
        self.play(
            Write(labels)
        )
        self.play(
            FadeIn(x_comp_equation),
            FadeIn(y_comp_equation)
        )
        self.play(
            x_len.animate().set_value(-1),
            y_len.animate().set_value(2)
        )
        self.play(
            Write(atmintine)
        )
        self.wait(3)