from manim import *

class config(Scene):
    def construct(self):

        title_kwargs = {
            "color": PURPLE,
            "opacity": 0.7
        }
        
        title = Text("Add, Remove, Wait and Play", **title_kwargs)
        self.add(title)
        self.wait(3)
        self.remove(title)
        self.wait(2)
        self.play(FadeIn(title))
        self.wait()

from manim import *

class BaseScene(Scene):
    def __init__(self, number=0, **kwargs):
        self.number = number
        super().__init__(**kwargs)

    def construct(self):
        title = Text(f"My number is: {self.number}")
        self.add(title)

# Ahora puedes crear subclases que hereden de BaseScene con distintos parámetros

class ExampleScene1(BaseScene):
    def __init__(self, **kwargs):
        super().__init__(number=2, **kwargs)

class ExampleScene2(BaseScene):
    def __init__(self, **kwargs):
        super().__init__(number=10, **kwargs)
