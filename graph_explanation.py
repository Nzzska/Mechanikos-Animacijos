from manim import *

class GraphExplanation(Scene):
    def construct(self):
        label_x = Tex('Argumentas').set(color=RED)
        label_y = Tex('Reikšmė').set(color=BLUE)
        ax = Axes()
        label_x = ax.get_x_axis_label(
            label_x
        )
        label_y = ax.get_y_axis_label(
            label_y
        )
        y_axis = ax.get_y_axis()
        y_axis.set(color=BLUE)
        x_axis = ax.get_x_axis()
        x_axis.set(color=RED)

        frame1 = SurroundingRectangle(x_axis, buff=0.1, color=YELLOW)
        frame2 = SurroundingRectangle(y_axis, buff=0.1, color=YELLOW)

        explanation1 = Tex(
            '''Argumentas - funkcijos kintamasis. \n
            Tai yra dydis nuo kurio priklauso \n
            funkcijos reikšmė. Argumentas dažniausiai yra \n
            vaizduojamas ant horizontalios (matematikos \n
            pamokoje labiau žinomos kaip x) ašies. \n
            ''',
            color=RED
        ).shift(2*UP + 3*RIGHT).scale(0.5)

        explanation2 = Tex(
            '''\n
            Funkcijos reikšmė - tai rezultatas \n
            kurį gauname įsistate, argumentą į funkcija
            ''',
            color=BLUE
        ).shift(2*UP + 3*LEFT).scale(0.5)

        self.add(ax, label_x, label_y, x_axis)
        self.wait(1)
        self.play(
            Write(frame1),
            Write(explanation1)
        )
        self.wait(2)
        self.play(
            FadeOut(explanation1),
            Transform(frame1, frame2)
        )
        self.play(
            Write(explanation2)
        )
        self.wait(2)