from manim import *
from manim_physics import *

class Opening(SpaceScene):
    def construct(self):
        # Generate opening text and shift upwards
        openingText = Text("Let's take a look at Pendulums")
        self.play(Write(openingText))
        self.play(openingText.animate.to_edge(UP))

        # Create basic pendulum using Physics library
        pend = Pendulum(5, bob_style= {"color": GREEN, "fill_opacity": 1, "radius": 0.25})
        self.play(Create(pend))
        self.make_rigid_body(*pend.bobs)
        pend.start_swinging()
        self.wait(10)