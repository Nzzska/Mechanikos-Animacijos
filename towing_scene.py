from manim import *

class Towing_scene(Scene):
    def ttnparr(self, t): #t - tracker
        return np.array([i.get_value() for i in t])
    
    def above_vector(self, mobj, vec_mobj):
        mobj.next_to(vec_mobj, UP)
        
    def update_vector(
        self, 
        mobj_vector, 
        mobj_tracker, 
        center_mobj, 
        color,
        stroke_width=3):
        mobj_vector.become(
            Arrow(
                start=center_mobj.get_center(),
                end=self.ttnparr(mobj_tracker) + center_mobj.get_center(),
                buff=0,
                color=color,
                stroke_width=stroke_width
            )
        )
    
    def add_trackers(self, trackers1, trackers2):
        given_trackers = zip(trackers1, trackers2)
        resultant_trackers = []
        for t1, t2 in given_trackers:
            active_tracker = ValueTracker(t1.get_value()+t2.get_value())
            resultant_trackers.append(active_tracker)
        return resultant_trackers

    def construct(self):
        
        box = Square(side_length=2, color=GREEN, fill_opacity=0.2)
        
        f1_trackers = [ValueTracker(-3), ValueTracker(0), ValueTracker(0)]
        f2_trackers = [ValueTracker(5), ValueTracker(0), ValueTracker(0)]
        
        fsum_trackers = self.add_trackers(f1_trackers, f2_trackers)
        fsum_trackers[0].add_updater(
            lambda m: m.set_value(
                f1_trackers[0].get_value() + f2_trackers[0].get_value()
            )
        )
        fsum_trackers[1].add_updater(
            lambda m: m.set_value(
                f1_trackers[1].get_value() + f2_trackers[1].get_value()
            )
        )
        fsum_trackers[2].add_updater(
            lambda m: m.set_value(
                f1_trackers[2].get_value() + f2_trackers[2].get_value()
            )
        )
        
        vec1 = Arrow(
                start=box.get_center(), 
                end=self.ttnparr(f1_trackers) + box.get_center(), 
                color=BLUE, 
                buff=0
        ).add_updater(
            lambda m: self.update_vector(
                mobj_vector=m, 
                mobj_tracker=f1_trackers, 
                center_mobj=box,
                color=BLUE
            )
        )
        vec1_name = Tex('$\\vec{F_1}$', color=BLUE)\
        .next_to(vec1, UP)
        
        vec2 = Arrow(
                start=box.get_center(), 
                end=self.ttnparr(f2_trackers) + box.get_center(), 
                color=RED, 
                buff=0
        ).add_updater(
            lambda m: self.update_vector(
                mobj_vector=m, 
                mobj_tracker=f2_trackers, 
                center_mobj=box,
                color=RED
            )
        )
        vec2_name = Tex('$\\vec{F_2}$', color=RED).next_to(vec2, UP)

        vec_sum = Arrow(
            start=box.get_center(),
            end=self.ttnparr(fsum_trackers) + box.get_center(),
            color=GREEN,
            buff=0,
            stroke_width=5
        ).add_updater(
            lambda m: self.update_vector(
                mobj_vector=m,
                mobj_tracker=fsum_trackers,
                center_mobj=box,
                color=GREEN,
                stroke_width=5
            )
        )
        vec_sum_name = Tex('$\\vec{F_1}+$'+'$\\vec{F_2}$', color=WHITE)\
        .next_to(vec_sum, UP)
        
        init_vectors = VGroup(vec1.copy(), vec2.copy())
        init_names = VGroup(
            vec1_name.copy().add_updater(lambda m: self.above_vector(m, init_vectors[0])),
            vec2_name.copy().add_updater(lambda m: self.above_vector(m, init_vectors[1]))
        )
        init_items = init_vectors + init_names
        sum_group = VGroup(
            vec_sum, 
            vec_sum_name.add_updater(lambda m: self.above_vector(m, vec_sum))
        )
        self.ttnparr(fsum_trackers)
        self.add(box, init_items)
        self.play(
            FadeOut(init_items),
            ReplacementTransform(
                init_items.copy(), 
                sum_group
            )
        )
        self.play(
            box.animate().shift(2*RIGHT)
        )
        self.play(
            FadeOut(sum_group),
            FadeIn(init_items),
        )
        self.play(
            f1_trackers[0].animate().set_value(-5),
            f2_trackers[0].animate().set_value(3),
            fsum_trackers[0].animate(),
            fsum_trackers[1].animate(),
            fsum_trackers[2].animate()
        )
        self.play(
            FadeOut(init_items),
            ReplacementTransform(init_items.copy(), sum_group)
        )
        self.play(
            box.animate().shift(2*LEFT)
        )
        self.play(
            FadeOut(sum_group),
            FadeIn(init_items),
        )
        self.play(
            f1_trackers[0].animate().set_value(0),
            f1_trackers[1].animate().set_value(-3)
        )
        self.play(
            FadeOut(init_items),
            ReplacementTransform(init_items.copy(), sum_group)
        )
        self.play(
            box.animate().shift(RIGHT+DOWN)
        )
        self.play(
            FadeOut(sum_group),
            FadeIn(init_items),
        )
        self.play(
            f2_trackers[0].animate().set_value(-3),
            f1_trackers[1].animate().set_value(+3)
        )
        self.play(
            FadeOut(init_items),
            ReplacementTransform(init_items.copy(), sum_group)
        )
        self.play(
            box.animate().shift(UP+LEFT)
        )
        self.play(
            FadeOut(sum_group),
            FadeIn(init_items),
        )
        self.play(
            f1_trackers[0].animate().set_value(-3),
            f2_trackers[0].animate().set_value(5),
            f1_trackers[1].animate().set_value(0)
        )

        print(self.ttnparr(f1_trackers))
        print(self.ttnparr(f2_trackers))
        print(self.ttnparr(fsum_trackers))