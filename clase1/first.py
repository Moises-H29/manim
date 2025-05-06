from manimlib import *

class FirstScene(Scene):
    def construct(self):
        title = Text("First Scene!")
        self.add(title)
        self.wait()

class SecondScene(Scene):
    def construct(self):
        title = Text("Second Scene!")
        self.add(title)
        self.wait()