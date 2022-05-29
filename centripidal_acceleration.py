from manim import *

def statusis(vec):
    x = vec[0]
    y = vec[1]
    return np.array([-1*y, x, 0])

class Centripidal_acceleration(Scene):
    def construct(self):
        fps = 60
        dt = 1/60
        r = 3
        
        num_plane = NumberPlane()
        
        pth = Circle(color=BLUE, radius=r)
        red_dot = Dot([3, 0, 0], color=RED)
        a_vec = Arrow(
            start=np.array(red_dot.get_center()), 
            end=np.array([0,0,0]),
            buff=0, 
            color=RED
        ).add_updater(
            lambda m: m.become(Arrow(
                start=np.array(red_dot.get_center()), 
                buff=0, 
                end=np.array([0,0,0]), 
                color=RED)
            )
        )
        a_txt = Tex("pagreitis $\\vec{a}$", color=RED).next_to(a_vec)
        a_txt.add_updater(lambda m: m.next_to(a_vec))
        v_vec = Arrow(
            start=np.array(red_dot.get_center()), 
            end=red_dot.get_center() + statusis(red_dot.get_center()),
            buff=0,
            color=GREEN
        ).add_updater(
            lambda m: m.become(
                Arrow(
                    start=np.array(red_dot.get_center()), 
                    end=red_dot.get_center() + statusis(red_dot.get_center()),
                    buff=0,
                    color=GREEN
                )
            )
        )
        v_txt = Tex('greitis $\\vec{v}$', color = GREEN).add_updater(lambda m: m.move_to(v_vec))
        self.add(    
            num_plane,
            pth,
            red_dot,
            a_vec,
            v_vec,
            a_txt,
            v_txt
        )
        self.play(MoveAlongPath(red_dot, pth, run_time=5, rate_func=linear))