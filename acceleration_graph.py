from manim import *

# Klipas skirtas parodyti, kaip poslinkis, greitis ir pagreitis yra susije labiau iš matematinės pusės.
# '''
# pradedame nuo poslinkio grafiko, įsivaizduojame, greičio nėra, kaip atrodys grafikas? 
# Pabrėžiame, kad toks grafikas yra konstanta (S0)
# Panašiai kartojame, kai S0 = 0, bet jau v0 != 0
# '''
def poslinkis(t, s0, v0, a):
    return s0 + v0 * t + (a * t ** 2) / 2
def greitis(t, v0, a):
    return v0 + a * t
def pagreitis(t, a):
    return a

class DerivativeExample(Scene):
    def sva_axes(self):
        #Acceleration
        a_axis = Axes(
            x_length=3.5,
            y_length=4,
            x_range=[0., 6., 1.5],
            y_range=[0., 10., 2],
            tips=True,
            axis_config={"include_numbers":True}
        ).shift(4.5*RIGHT)
        a_xlabel = a_axis.get_x_axis_label(
            "Laikas - t, s"
        ).shift(2*DOWN+3*LEFT)
        a_ylabel = a_axis.get_y_axis_label(
            "Pagreitis - \\vec{a}, \\frac{m}{s^2}"
        ).shift(2*LEFT)
        a_labels = VGroup(a_xlabel, a_ylabel).shift(2*RIGHT)
        #Velocity
        v_axis = Axes(
            x_length=3.5,
            y_length=4,
            x_range=[0., 6., 1.5],
            y_range=[0., 10., 2],
            tips=True,
            axis_config={"include_numbers":True}
        )
        v_xlabel = v_axis.get_x_axis_label(
            "Laikas - t, s"
        ).shift(2*DOWN+3*LEFT)
        v_ylabel = v_axis.get_y_axis_label(
            "Greitis - \\vec{v}, \\frac{m}{s}"
        )
        v_labels = VGroup(v_xlabel, v_ylabel)
        #Displacement
        s_axis = Axes(
            x_length=3.5,
            y_length=4,
            x_range=[0., 6., 1.5],
            y_range=[0., 10., 2],
            tips=True,
            axis_config={"include_numbers":True}
        ).shift(4.5*LEFT)
        s_xlabel = v_axis.get_x_axis_label(
            "Laikas - t, s"
        ).shift(2*DOWN+3*LEFT)
        s_ylabel = v_axis.get_y_axis_label(
            "Poslinkis - \\vec{s}, m"
        )
        s_labels = VGroup(s_xlabel, s_ylabel).shift(4.5*LEFT)

        return {
            'a_axis':a_axis,
            'a_labels':a_labels,
            'v_axis':v_axis,
            'v_labels':v_labels,
            's_axis':s_axis,
            's_labels':s_labels,
        }

    def construct(self):
        all_axis = self.sva_axes()
        self.add(
            all_axis['a_axis'].set(color=PURPLE),
            all_axis['v_axis'].set(color=BLUE),
            all_axis['s_axis'].set(color=GREEN),
            all_axis['a_labels'].set(color=PURPLE),
            all_axis['v_labels'].set(color=BLUE),
            all_axis['s_labels'].set(color=GREEN)
        )

class DisplacementGraph(Scene):
    def construct(self):

        initial_displacement = 2.0

        v0 = ValueTracker(0)
        a0 = ValueTracker(0)
        s0 = ValueTracker(0)

        pointer = Arrow(
            start=np.array([0., 1., 0]),
            end=np.array([0., 0., 0.])
        )

        displacement_tex = Tex(
            f"$\\vec{{s_0}} = {s0.get_value():.2f}$"
        ).add_updater(lambda m:
            m.become(
                Tex(
                    f"$\\vec{{s_0}} = {s0.get_value():.2f}$"
                )
            )
        )

        velocity_tex = Tex(
            f"$\\vec{{v_0}} = {v0.get_value():.2f}$"
        ).add_updater(lambda m:
            m.become(
                Tex(
                    f"$\\vec{{v_0}} = {v0.get_value():.2f}$"
                ).next_to(displacement_tex, DOWN)
            )
        ).next_to(displacement_tex, DOWN)

        acceleration_tex = Tex(
            f"$\\vec{{a}} = {a0.get_value():.2f}$"
        ).add_updater(lambda m:
            m.become(
                Tex(
                    f"$\\vec{{a}} = {a0.get_value():.2f}$"
                ).next_to(velocity_tex, DOWN)
            )
        ).next_to(velocity_tex, DOWN)

        #times = [ 0.  5. 10. 15. 20.]
        time_end = np.linspace(5, 20, 4)
        time_begin = np.linspace(0, 15, 4)
        velocities = np.array([0., 0.6, 0., -0.6, 0.3])
        accelerations = np.array([0., 0., 0.1, 0.1, -0.1])
        displacements = [initial_displacement]
        colors = [RED, BLUE, RED, BLUE] 
        for v,a,t_end, t_begin in zip(
            velocities,
            accelerations,
            time_end,
            time_begin
        ):
            new_displ = poslinkis(
                t_end-t_begin,
                displacements[len(displacements)-1],
                v, 
                a
            )
            displacements.append(new_displ)
            

        ax = Axes(
            x_range=[0., 20., 2],
            y_range=[0., 10., 1.5],
            axis_config={
                "include_numbers":True,
            },
        )
        graphs = [
            ax.plot(lambda t:
                poslinkis(t=t-t_begin, s0=s, v0=v, a=a),
                x_range=[t_begin, t_end],
                color = c
            ) for t_begin, t_end, s, v, a, c in zip(
                time_begin, 
                time_end, 
                displacements, 
                velocities, 
                accelerations,
                colors
            )
        ]
        displacement_tex.add_updater(
            lambda m: m.next_to(pointer, 6*UP)
        )

        self.add(ax, pointer, displacement_tex, velocity_tex, acceleration_tex)
        for graph,v,s,a in zip(
            graphs, velocities, displacements, accelerations
        ):
            self.play(
                pointer.animate().move_to(graph, UP),
            )
            self.play(
                Write(graph, run_time=3),
                s0.animate().set_value(s),
                v0.animate().set_value(v),
                a0.animate().set_value(a)
            )