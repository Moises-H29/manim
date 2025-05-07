from manim import *

class add(Scene):
    def construct(self):
        title = Text("Add, Remove, Wait and Play")
        self.add(title)
        self.wait(3)
        self.remove(title)
        self.wait(2)
        self.play(FadeIn(title))
        self.wait()