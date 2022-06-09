from manim import *
import numpy.linalg as linalg

class SpringScene(Scene):
    def rope_thickness(self, moving_mob):
        rope_len = linalg.norm(np.array([-5., -2., 0.]) - moving_mob.get_center())
        if rope_len >= self.MAX_ROPE_LEN:
            return self.MIN_THICKNESS
        else:
            #normal - normal/min * len
            rope_thicc = self.NORMAL_THICKNESS  \
                - 1 * rope_len
            return rope_thicc
    def move_mobject(self, mob, dt):
        mob.shift(mob.v * dt)
        self.update_velocity(mob, dt)
        self.apply_a(mob)
    def apply_a(self, mob):
        displacement_vec = self.eq_pos - mob.get_center()
        displacement_len = linalg.norm(displacement_vec)
        displacement_unit = displacement_vec/displacement_len
        acceleration_len = self.calculate_a(
            displacement_len, 
            self.stiffness_tracker.get_value()
        )
        mob.set(a=acceleration_len*displacement_unit)

    def calculate_a(self, x, k):
        return k * x ** 2

    def mob_shift_vectors(self, mob):
        velocity = Arrow(
            buff=0,
            start=mob.get_center(),
            end=mob.get_center() + mob.v,
            color=RED
        ).add_updater(
            lambda m: m.become(
                Arrow(
                    start=mob.get_center(),
                    end=mob.get_center() + mob.v,
                    color=RED,
                    buff=0
                )
            )
        )
        acceleration = Arrow(
            buff=0,
            start=mob.get_center(),
            end=mob.get_center() + mob.a,
            color=BLUE
        ).add_updater(
            lambda m: m.become(
                Arrow(
                    start=mob.get_center(),
                    end=mob.get_center() + mob.a,
                    color=BLUE,
                    buff=0
                )
            )
        )
        v_label = Tex("$\\vec{v}$", color=RED).add_updater(
            lambda m: m.next_to(velocity, UP)
        )
        a_label = Tex("$\\vec{a}$", color=BLUE).add_updater(
            lambda m: m.next_to(acceleration, DOWN)
        )
        return {
            'v':velocity, 
            'a':acceleration,
            'v_label':v_label,
            'a_label':a_label
        }
    def update_velocity(self, mob, dt):
        mob.v += mob.a * dt
    def construct(self):
        #Some self stuff x_X
        self.stiffness_tracker = ValueTracker(0.5)
        self.eq_pos = np.array([0., -2., 0.])
        self.initial_velocity = np.array([0., 0., 0.,])
        self.initial_acceleration = np.array([0., 0., 0.])
        self.MAX_ROPE_LEN = 8
        self.MIN_THICKNESS = 1
        self.NORMAL_THICKNESS = 10

        floor = Line(
            start=np.array([-5., -3., 0.]),
            end=np.array([5., -3., 0.])
        )

        taselis = Square(
            side_length=2,
            color=GREEN
        ).shift(2*LEFT+2*DOWN)
        taselis.set(v=self.initial_velocity)
        taselis.set(a=self.initial_acceleration)

        vertical_wall = Line(
            start=np.array([-5., -3., 0.]),
            end=np.array([-5., 1., 0.]),
            color=BLUE
        )

        spring = Line(
            start=taselis.get_center(),
            end=np.array([-5., -2., 0.]),
            color=GREEN,
            stroke_width=self.rope_thickness(taselis)
        ).add_updater(
            lambda m: m.become(
                Line(
                    start=taselis.get_center(),
                    end=np.array([-5., -2., 0.]),
                    stroke_width=self.rope_thickness(taselis)
                )
            )
        )

        taselis.add_updater(
            lambda m, dt: self.move_mobject(m, dt)
        )

        vectors = self.mob_shift_vectors(taselis)


        self.add(
            floor,
            taselis,
            vertical_wall,
            spring,
            vectors['v'],
            vectors['a'],
        )
        self.play(
            Write(vectors['v_label']),
            Write(vectors['a_label'])
        )
        self.wait(15)