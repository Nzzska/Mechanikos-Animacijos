from manim import *

class EquationSolutions(Scene):
    def writeOutEquations(self, equations_dictionary):
        i = UP * 3
        for eq in equations_dictionary:
            self.add(equations_dictionary[eq].shift(i))
            i = i + DOWN
    def construct(self):
        equations = {
            'F_lor':Tex('$F_L=qvB\\sin{\\alpha}$'),
            'q_flor':Tex('$ q=\\frac{F_L}{vb\\sin{\\alpha}}$', color=GREEN),
            's':Tex('$s=s_0+v_0t+\\frac{at^2}{2}$'),
            's_disc':Tex('$D = v_0^2 - 4(s_0-s)\\frac{a}{2}$', color=BLUE),
            't_sol_s':Tex('$t = \\frac{-v_0 \\pm \\sqrt{v_0^2 - 4(s_0-s)\\frac{a}{2}}}{2\\frac{a}{2}}$', color=RED),
            'alpha_sol':Tex('$\\alpha = (-1)^k \\arcsin{(\\frac{F_L}{qvB})}+2\\pi k, k \\in Z $', color=BLUE),
        }
        texts = {
            'text_0':Text('Lorenco jėgos lygtis'),
            'text_1':Text('Jeigu ieškome q...', color=GREEN),
            'text_2':Text('Jeigu ieškome alfos...', color=BLUE),
            'text_3':Text('Poslinkio lygtis'),
            'text_4':Text('norėdami rasti t, sprendžiame kvadratine lygtį', color=BLUE),
            'text_5':Text('Diskriminantas...', color=BLUE),
            'text_6':Text('Volia!', color=BLUE),
        }

        equations['q_flor'].shift(4*LEFT)
        equations['alpha_sol'].shift(3*RIGHT).scale(0.75)

        #playinam
        self.wait(1)
        self.play(
            Write(equations['F_lor'].shift(2*UP), run_time=2),
            FadeIn(texts['text_0'].shift(3*UP), run_time=3)
        )

        pointer1 = Arrow(start=equations['F_lor'], end=equations['q_flor'])
        pointer2 = Arrow(start=equations['F_lor'], end=equations['alpha_sol'].get_center())
        texts['text_1'].next_to(equations['q_flor'], DOWN).scale(0.5)
        texts['text_2'].next_to(equations['alpha_sol'], DOWN).scale(0.5)

        self.wait(2)
        self.play(
            FadeIn(pointer1, pointer2, lag_ratio=0.5)
        )
        self.play(
            Write(texts['text_1'], run_time=2),
            Write(texts['text_2'], run_time=2),
            Write(equations['q_flor'], run_time=5),
            Write(equations['alpha_sol'], run_time=5)
        )
        self.wait(2)
        self.play(
            FadeOut(
                equations['F_lor'],
                texts['text_0'],
                texts['text_1'],
                texts['text_2'],
                equations['q_flor'],
                equations['alpha_sol'],
                pointer1,
                pointer2
            )
        )
        self.wait(2)

        equations['s'].shift(2*UP)
        texts['text_3'].next_to(equations['s'], UP)
        self.play(
            FadeIn(texts['text_3'], run_time=2),
            Write(equations['s'], run_time=3)
        )
        equations['s_disc'].shift(DOWN)
        texts['text_5'].next_to(equations['s_disc'], UP)

        self.play(
            Write(texts['text_4'].next_to(equations['s'], DOWN).scale(0.5))
        )
        self.play(
            FadeIn(texts['text_5'].scale(0.5), run_time=2),
            Write(equations['s_disc'], run_time=3)
        )
        self.wait(2)
        self.play(
            Transform(texts['text_5'], texts['text_6'].shift(DOWN), run_time=1),
            Transform(equations['s_disc'], equations['t_sol_s'], run_time=1)
        )
        self.wait(5)

class AlgebraManipulations(Scene):
    def construct(self):
        number = ValueTracker(1)
        equation = Tex(
            f"${number.get_value():.2f}$",
            "$=$",
            f"${number.get_value():.2f}$"
        ).scale(2)
        equation.add_updater(
            lambda m: m.become(
                Tex(
                    f"{number.get_value():.2f}",
                    "=",
                    f"{number.get_value():.2f}"
                ).scale(2)
            )
        )

        f_eq = Tex("$a=$","$(f\\times\\frac{b-c+d}{e})^2$").scale(2)
        klausimas = Text("Kam lygus b?").next_to(f_eq, UP)
        #animations
        self.wait(1)
        self.play(FadeIn(equation))
        self.addition(number, 5, equation)
        self.subtraction(number, 3, equation)
        self.multiplication(number, 2, equation)
        self.devision(number, 3, equation)
        self.power(number, 4, equation)
        self.sq_rt(number, 2, equation)
        self.wait(1)
        self.play(
            FadeOut(equation)
        )
        self.play(
            Write(f_eq),
            Write(klausimas)
        )
        self.play(
            Transform(f_eq, Tex("$\\sqrt{a}=f\\times\\frac{b-c+d}{e}$").scale(2))
        )
        self.play(
            Transform(f_eq, Tex("$\\frac{\\sqrt{a}}{f}=\\frac{b-c+d}{e}$").scale(2))
        )
        self.play(
            Transform(f_eq, Tex("$e\\times\\frac{\\sqrt{a}}{f}=b-c+d$").scale(2))
        )
        self.play(
            Transform(f_eq, Tex("$e\\times\\frac{\\sqrt{a}}{f}-d=b-c$").scale(2))
        )
        self.play(
            Transform(f_eq, Tex("$e\\times\\frac{\\sqrt{a}}{f}-d+c$","$=b$").scale(2))
        )
        self.play(
            Write(SurroundingRectangle(f_eq[0], color=YELLOW)),
            klausimas.animate().set(color=YELLOW)
        )
        self.wait(2)

    def addition(self, num_tracker, num_to_add, equation):
        t1 = Tex(f"$+{num_to_add}$", color=RED).next_to(equation[0], LEFT).scale(2)
        t2 = Tex(f"$+{num_to_add}$", color=RED).next_to(equation[2], RIGHT).scale(2)
        t1.shift(LEFT)
        t2.shift(RIGHT)

        self.play(
            Write(t1),
            Write(t2)
        )

        self.play(
            num_tracker.animate().set_value(
                num_tracker.get_value()+num_to_add
            ),
            FadeOut(t1, direction=equation[0]),
            FadeOut(t2, direction=equation[2])
        )

    def subtraction(self, num_tracker, num_to_sub, equation):
        t1 = Tex(f"$-{num_to_sub}$", color=BLUE).next_to(equation[0], LEFT).scale(2)
        t2 = Tex(f"$-{num_to_sub}$", color=BLUE).next_to(equation[2], RIGHT).scale(2)
        t1.shift(LEFT)
        t2.shift(RIGHT)

        self.play(
            Write(t1),
            Write(t2)
        )

        self.play(
            num_tracker.animate().set_value(
                num_tracker.get_value()-num_to_sub
            ),
            FadeOut(t1, direction=equation[0]),
            FadeOut(t2, direction=equation[2])
        )

    def multiplication(self, num_tracker, num_to_mult, equation):
        t1 = Tex(f"$\\times{num_to_mult}$", color=GREEN).next_to(equation[0], LEFT).scale(2)
        t2 = Tex(f"$\\times{num_to_mult}$", color=GREEN).next_to(equation[2], RIGHT).scale(2)
        t1.shift(LEFT)
        t2.shift(RIGHT)

        self.play(
            Write(t1),
            Write(t2)
        )

        self.play(
            num_tracker.animate().set_value(
                num_tracker.get_value()*num_to_mult
            ),
            FadeOut(t1, direction=equation[0]),
            FadeOut(t2, direction=equation[2])
        )

    def devision(self, num_tracker, num_to_div, equation):
        t1 = Tex(f"$:{num_to_div}$", color=TEAL).next_to(equation[0], LEFT).scale(2)
        t2 = Tex(f"$:{num_to_div}$", color=TEAL).next_to(equation[2], RIGHT).scale(2)
        t1.shift(LEFT)
        t2.shift(RIGHT)

        self.play(
            Write(t1),
            Write(t2)
        )

        self.play(
            num_tracker.animate().set_value(
                num_tracker.get_value()/num_to_div
            ),
            FadeOut(t1, direction=equation[0]),
            FadeOut(t2, direction=equation[2])
        )

    def power(self, num_tracker, num_to_div, equation):
        t1 = Tex(f"$x^{num_to_div}$", color=PINK).next_to(equation[0], LEFT).scale(2)
        t2 = Tex(f"$x^{num_to_div}$", color=PINK).next_to(equation[2], RIGHT).scale(2)
        t1.shift(LEFT)
        t2.shift(RIGHT)
        
        self.play(
            Write(t1),
            Write(t2)
        )

        self.play(
            num_tracker.animate().set_value(
                num_tracker.get_value() ** num_to_div
            ),
            FadeOut(t1, direction=equation[0]),
            FadeOut(t2, direction=equation[2])
        )

    def sq_rt(self, num_tracker, num_to_div, equation):
        t1 = Tex("$\\sqrt{x}$", color=PURPLE).next_to(equation[0], LEFT).scale(2)
        t2 = Tex("$\\sqrt{x}$", color=PURPLE).next_to(equation[2], RIGHT).scale(2)
        t1.shift(LEFT)
        t2.shift(RIGHT)
        
        self.play(
            Write(t1),
            Write(t2)
        )

        self.play(
            num_tracker.animate().set_value(
                np.sqrt(num_tracker.get_value())
            ),
            FadeOut(t1, direction=equation[0]),
            FadeOut(t2, direction=equation[2])
        )