from pickletools import UP_TO_NEWLINE
from manim import *
import numpy.linalg as linalg

class InclinedPlane(Scene):
    def animate_mobject(self, mobject, dt):
        self.update_velocity(mobject, dt)
        self.movement(mobject, dt)

    def movement(self, mobject, dt):
        mobject.shift(mobject.velocity*dt)

    def update_velocity(self, mobject, dt):
        mobject.velocity += mobject.acceleration*dt

    def right_triangle(
        self, 
        angle_theta, 
        base_len
    ):
        base_part = base_len
        side_part = np.tan(angle_theta)*base_len
        hipp_part = np.sqrt(base_part ** 2 + side_part **2)
        triangle = Polygon(
            np.array([0., 0., 0.]),
            np.array([base_part, 0., 0.]),
            np.array([base_part, side_part, 0])
        )

        along_unit = self.unit_vector(
            np.array([base_len, side_part, 0.])
        )
        normal_unit = self.unit_vector(
            np.array([-side_part, base_len, 0.])
        )
        triangle.set(along_unit = along_unit)
        triangle.set(normal_unit = normal_unit)
        triangle.set(base_len = base_part)
        triangle.set(side_len = side_part)
        triangle.set(hipp_len = hipp_part)

        triangle.shift(-1 * triangle.get_center())
        return triangle

    def place_box_on_ip(
        self, 
        box, 
        plane,
        unit_norm,
        unit_along
    ):
        box.rotate(self.plane_angle)
        box.move_to(plane.get_center())
        box.shift(unit_norm * self.box_length/2)
        box.shift(unit_along * self.box_length)

    def calculate_ip_normal(self, plane):
        on_plane_center = plane.get_center()

    def unit_vector(self, vector):
        length = linalg.norm(vector)
        return vector/length

    def calculate_normal_force(self, direction):
        magnitude = linalg.norm(self.weight)\
            * np.cos(self.plane_angle)
        return direction*magnitude

    def construct(self):
        self.weight = np.array([0., -2., 0])
        self.plane_angle = np.pi/6
        self.plane_base = 8
        self.box_length = 2
        self.initial_velocity = np.array([0., 0., 0.])
        self.initial_acceleration = np.array([0., 0., 0.])


        inclined_plane = self.right_triangle(
            self.plane_angle, 
            self.plane_base
        )
        PLANE_UP = inclined_plane.normal_unit
        PLANE_RIGHT = inclined_plane.along_unit

        box = Square(side_length=self.box_length)
        self.place_box_on_ip(
            box,
            inclined_plane,
            PLANE_UP,
            PLANE_RIGHT
        )

        normal_force = Arrow(
            start=box.get_center(),
            end=box.get_center() \
                + self.calculate_normal_force(PLANE_UP),
            buff=0,
            color=PURPLE
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                box.get_center(),
                box.get_center() \
                    + self.calculate_normal_force(PLANE_UP)
            )
        )

        w_vector = Arrow(
            start=box.get_center(),
            end = box.get_center() + self.weight,
            buff=0,
            color=PURPLE
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                box.get_center(),
                box.get_center()+self.weight
            )
        )

        acceleration = self.weight + self.calculate_normal_force(PLANE_UP)
        box.set(acceleration = acceleration)
        box.set(velocity = self.initial_velocity)
        a_vector = Arrow(
            start=box.get_center(),
            end=box.get_center()+box.acceleration,
            buff=0,
            color=RED
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                box.get_center(),
                box.get_center()+box.acceleration
            )
        )
        box.add_updater(
            lambda m, dt: self.animate_mobject(m, dt)
        )
        v_vector = Arrow(
            buff=0,
            color=GREEN,
            start=box.get_center(),
            end=box.get_center()+box.velocity
        ).add_updater(
            lambda m: m.put_start_and_end_on(
                box.get_center(),
                box.get_center()+box.velocity
            )
        )

        #labels:
        w_label = MathTex("m\\vec{g}", color=PURPLE).next_to(
            w_vector, DOWN
        ).add_updater(
            lambda m: m.next_to(w_vector, DOWN)
        )

        n_label = MathTex("\\vec{N}", color=PURPLE).next_to(
            normal_force, UP
        ).add_updater(
            lambda m: m.next_to(normal_force, UP)
        )
        v_label = MathTex("\\vec{v}", color=GREEN).next_to(
            v_vector, UP
        ).add_updater(
            lambda m: m.next_to(v_vector, UP)
        )
        a_label = MathTex("\\vec{a}", color=RED).next_to(
            a_vector, RIGHT
        ).add_updater(
            lambda m: m.next_to(a_vector, RIGHT)
        )
        labels = VGroup(
            w_label,
            v_label,
            n_label,
            a_label
        )

        self.add(inclined_plane, 
            box, 
            normal_force, 
            w_vector, 
            a_vector,
            v_vector
        )
        self.play(
            Write(labels)
        )
        self.wait(2)