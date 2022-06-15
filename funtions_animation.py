from manim import *
import random

random.seed(42)

class functionDefinition(Scene):
    def construct(self):
        random_numbers = [random.randint(1,10) for _ in range(10)]
        text_1 = \
            '''
            Funkcija - tam tikra taisyklė pakeisti vieną reikšme kita.\n
            Matematikoje, tai gali pasirodyti kiek sausa, tačiau funkcijas \n
            reikia gerai išmanyti ir atpažinti, nes šios nuolatos pasirodo \n
            įvairiuose moksluose. Pavyzdžiui fizikoje, nueitas kelias gali \n
            funkcija nuo laiko. Kuo ilgiau ėjau - tuo daugiau nuėjau. \n
            Programavime taip pat yra funkcijos, kažkokie duomenys yra funkcijos argumentai \n
            o funkcija gražina savo reikšme...
            '''
        text_2 = \
            '''

            '''
        x_sq = Tex("$ f(x) = x^2 $", color=WHITE)
        f_a = Tex("$ f(a) $","$ = a^2 $", color=YELLOW)
        a = Tex("a", color=WHITE).shift(3*LEFT).scale(3)
        b = Tex("b", color=WHITE).shift(3*RIGHT).scale(3)
        f_tex = Tex(
            "f", 
            color=WHITE,
            z_index=2
        ).scale(3)
        f_rec = SurroundingRectangle(
            f_tex, 
            color=YELLOW, 
            buff=0.3,
            z_index=2,
            fill_opacity=.7
        )
        f = VGroup(f_tex, f_rec)
        x_sq.next_to(f, DOWN)
        f_a.next_to(x_sq, DOWN)
        a_b = Arrow(
            start=a.get_center(), 
            end=b.get_center(), 
            fill_opacity=0.4,
            color=BLUE
        )
        fab = Tex("$f$","$(a)$", "$=$", "$b$", color=WHITE)

        self.add(fab.scale(3))
        self.wait(2)
        self.play(
            ReplacementTransform(fab[0].copy(), f),
            ReplacementTransform(fab[1].copy(), a),
            ReplacementTransform(fab[3].copy(), b),
            FadeOut(*[item for item in fab], run_time=0.5)
        )
        self.play(
            Write(a_b),
            FadeIn(x_sq),
            FadeIn(f_a)
        )
        for rand_num in random_numbers:
            rnd_num_tex = Tex(f"{rand_num}").shift(2*UP+3*LEFT).scale(2)
            rnd_num_sq_tex = Tex(f"{rand_num**2}").shift(2*UP+3*RIGHT).scale(2)
            arrow1 = Arrow(
                buff=0.3,
                start=rnd_num_tex.get_center(),
                end=f_a[0].get_center(),
                color=RED,
                fill_opacity=0.1,
                z_index=0
            )
            arrow2 = Arrow(
                buff=0.3,
                start=f_a[1].get_center(),
                end=rnd_num_sq_tex.get_center(),
                color=RED,
                fill_opacity=0.1,
                z_index=0
            )
            self.play(Write(rnd_num_tex))
            self.play(Write(arrow1))
            self.play(Write(arrow2))
            self.play(Write(rnd_num_sq_tex))
            self.play(
                FadeOut(*[arrow1, rnd_num_tex, arrow2, rnd_num_sq_tex])
            )
            self.wait(1)

class functionGraphs(Scene):
    def movement(self, t, s0, v0, a):
        return s0 + v0*t + a/2 * t ** 2
    def radioactive_decay(self, t, half_life, N0):
        return N0 * np.exp(-1*(np.log(2)/half_life)*t)
    def construct(self):
        linear_formula = Tex("$f(x) = \\frac{x}{2} + 2$")
        movement_formula = Tex(
            "$s(t) = $","$4$","$-2$","$t+\\frac{0.5t^2}{2}$"
        )
        decay_formula = Tex(
            "$N(t)=$","$7e^{\\frac{-ln(2) t}{5}}$"
        )
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 8, 1],
            tips=False,
            axis_config={"include_numbers":True}
        )
        linear = ax.plot(
            lambda x: 0.5*x + 2, x_range=[0.001, 10]
        )
        movement = ax.plot(
            lambda t: self.movement(
                t=t,
                s0=4,
                v0=-2,
                a=0.5
            )
        )
        decay = ax.plot(
            lambda t: self.radioactive_decay(
                t=t,
                half_life=5,
                N0=7
            )
        )
        self.add(ax)
        self.play(
            Write(linear),
            Write(linear_formula.shift(3*UP+2*LEFT))
        )
        self.wait(2)
        self.play(
            FadeOut(linear),
            FadeOut(linear_formula)
        )
        self.play(
            Write(movement.set(color=YELLOW)),
            Write(movement_formula.set(color=YELLOW))
        )
        self.play(
            FadeOut(movement),
            FadeOut(movement_formula)
        )
        self.wait(2)
        self.play(
            Write(decay.set(color=GREEN)),
            Write(decay_formula.set(color=GREEN).shift(2*DOWN+2*LEFT))
        )
    