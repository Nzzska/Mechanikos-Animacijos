from manim import *
import numpy as np
import numpy.linalg as linalg

class PendulumScene(Scene):
    def update_pendulum(self, mobject, dt, gravity_tracker):
        mobject.set(acceleration = self.add_vectors(
            self.calculate_tension(mobject),
            self.weight
        ))
        self.weight = np.array(
            [
                0., 
                -1*gravity_tracker.get_value(), 
                0.
            ]
        )

        self.update_velocity(mobject, dt)
        self.movement(mobject, dt)

    def movement(self, mobject, dt):
        mobject.shift(mobject.velocity * dt)

    def update_velocity(self, mobject, dt):
        mobject.velocity += mobject.acceleration * dt

    def add_vectors(self, *vectors):
        vector_sum = np.array([0., 0., 0.])
        for vector in vectors:
            vector_sum += vector
        return vector_sum

    def calculate_tension(self, mobj):
        tension_unit = self.calculate_vector_towards_pin(mobj)
        tension = np.dot(mobj.velocity, mobj.velocity)\
        /linalg.norm(mobj.get_center() - mobj.pin) + tension_unit[1]\
        *linalg.norm(self.weight)
        return tension * tension_unit

    def unit_vector(self, vector):
        return vector/linalg.norm(vector)

    def calculate_vector_towards_pin(self, mobj):
        displacement = -1*mobj.get_center() + mobj.pin
        displacement_unit = self.unit_vector(displacement)
        return displacement_unit

    def construct(self):
        self.weight = np.array([0, -2., 0.])
        init_velocity = np.array([2., 0., 0])
        init_acceleration = np.array([0., 0., 0])
        weight_tracker = ValueTracker(-1*self.weight[1])

        pendulum = Circle(
            radius=0.5, 
            color=BLUE,
            fill_opacity=1,
            z_index=0
        ).shift(2*DOWN)
        pendulum.set(velocity = init_velocity)
        pendulum.set(acceleration = init_acceleration)
        pendulum.set(pin = np.array([0., 4., 0.]))

        pendulum_thread = Line(
            start=pendulum.get_center(), 
            end=pendulum.pin
        ).add_updater(
            lambda m: pendulum_thread.put_start_and_end_on(
                pendulum.get_center(),
                pendulum.pin
            )
        )

        pointer = Vector(RIGHT)
        pointer.add_updater(
            lambda m: m.next_to(
                        gravity_line.n2p(weight_tracker.get_value()),
                        LEFT
                    )
        )

        #vectors
        v_vector = Arrow(
            buff=0, 
            start=pendulum.get_center(),
            end=pendulum.get_center() + pendulum.velocity,
            color=WHITE
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                start=pendulum.get_center(),
                end=pendulum.get_center() + pendulum.velocity
            )
        )
        v_label = Tex('$\\vec{v}$', color=WHITE, z_index=2).next_to(v_vector)\
            .add_updater(
                lambda m: m.next_to(v_vector)
            )
        a_vector = Arrow(
            buff=0, 
            start=pendulum.get_center(),
            end=pendulum.get_center() +\
                 self.calculate_tension(pendulum) + self.weight,
            color=RED
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                start=pendulum.get_center(),
                end=pendulum.get_center() +\
                    self.calculate_tension(pendulum) + self.weight
            )
        )
        a_label = Tex('$\\vec{a}$', color=RED, z_index=2).next_to(a_vector)\
            .add_updater(
                lambda m: m.next_to(a_vector)
            )
        w_vector = Arrow(
            buff=0, 
            start=pendulum.get_center(),
            end=pendulum.get_center() + self.weight,
            color=PURPLE
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                start=pendulum.get_center(),
                end=pendulum.get_center() + self.weight
            )
        )
        w_label = Tex('$m\\vec{g}$', color=PURPLE, z_index=2).next_to(w_vector)\
            .add_updater(
                lambda m: m.next_to(w_vector)
            )
        t_vector = Arrow(
            buff=0, 
            start=pendulum.get_center(),
            end=pendulum.get_center() + self.calculate_tension(pendulum),
            color=GREEN
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                start=pendulum.get_center(),
                end=pendulum.get_center() + self.calculate_tension(pendulum)
            )
        )
        t_label = Tex('$\\vec{T}$', color=GREEN).next_to(t_vector)\
            .add_updater(
                lambda m: m.next_to(t_vector)
            )

        labels = VGroup(
            v_label,
            a_label,
            t_label,
            w_label
        )

        gravity_line = NumberLine(
            x_range=[0, 13, 2],
            length=6,
            include_tip=True,
            include_numbers=True,
            rotation=90 * DEGREES,
            label_direction=RIGHT
        ).shift(5*RIGHT)
        gravity_line_label = Tex(
            '$\\vec{g}$ ( $\\frac{m}{s^2}$ )',
            font_size=30,
            z_index=3
        ).next_to(gravity_line, np.array([0, 1., 0.]))

        self.add(
            pendulum, 
            pendulum_thread, 
            w_vector, 
            v_vector, 
            t_vector, 
            a_vector,
            gravity_line,
            gravity_line_label,
            pointer,
        )
        pendulum.add_updater(
            lambda m, dt: self.update_pendulum(m, dt, weight_tracker)
        )
        self.wait(5)
        self.play(
            Write(labels)
        )
        self.wait(5)
        self.play(
            weight_tracker.animate().set_value(3),
            gravity_line.animate().set(color=RED),
            gravity_line_label.animate().set(color=RED),
            pointer.animate().set(color=RED)
        )
        self.wait(10)
        self.play(
            weight_tracker.animate().set_value(1),
            gravity_line.animate().set(color=BLUE),
            gravity_line_label.animate().set(color=BLUE),
            pointer.animate().set(color=BLUE)
        )
        self.wait(10)