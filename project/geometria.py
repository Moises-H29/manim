from manim import *

class titulo(Scene):
    def construct(self):
        # Título
        titulo = Text("Ley de Coulomb en forma vectorial", color=RED).scale(0.8)
        self.play(Write(titulo))
        self.wait(3)
        self.wait(2)

class definicion(Scene):
    def construct(self):
        titulo = Text("¿Qué explica la Ley de Coulomb?").scale(0.8).to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)
        # Definición
        definicion = BulletedList(
            "Fuerza que existe entre cuerpos cargados",
            "La carga eléctrica siempre se presenta como un múltiplo\nentero de una cantidad    básica de carga"
        ).scale(0.6).next_to(titulo, DOWN, buff=0.5).align_to(titulo, RIGHT)
        self.play(FadeIn(definicion))
        self.wait(1)

        # Ecuación de carga q = ±Ze
        carga_eq = MathTex("q = \\pm n e, \\text{ con } n \\in \\mathbb{Z}").scale(0.8).next_to(definicion, DOWN, buff=0.5).align_to(titulo, LEFT)

        valor_e = MathTex("e = 1.6 \\times 10^{-19} \\, \\text{C}").scale(0.8).next_to(carga_eq, DOWN).align_to(carga_eq, LEFT)

        self.play(Write(carga_eq), Write(valor_e))
        self.wait(1)

       
