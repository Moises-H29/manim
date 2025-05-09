from manim import *

class titulo(Scene):
    def construct(self):
        # Título
        titulo = Text("Ley de Coulomb en forma vectorial", color=RED).scale(1.2)
        self.play(Write(titulo))
        self.wait(3)

class definicion(Scene):
    def construct(self):
        titulo = Text("¿Qué explica la Ley de Coulomb?").scale(0.9).to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)
        # Definición
        definicion1 = Text("• Fuerza que existe entre cuerpos cargados").scale(0.6).next_to(titulo, DOWN, buff=0.5).align_to(titulo, LEFT)
        self.play(FadeIn(definicion1))
        self.wait(1)
        definicion2 = Text("• La carga eléctrica siempre se presenta como\n   un múltiplo entero de una cantidad básica \n   de carga").scale(0.6).next_to(definicion1, DOWN, buff=0.5).align_to(titulo, LEFT)
        self.play(FadeIn(definicion2))
        self.wait(2)

        # Ecuación de carga q = ±Ze
        carga_eq = MathTex("q = \\pm n e, \\text{ con } n \\in \\mathbb{Z}").scale(0.8).next_to(definicion2, DOWN, buff=0.5).align_to(titulo, LEFT)

        valor_e = MathTex("e = 1.6 \\times 10^{-19} \\, \\text{C}").scale(0.8).next_to(carga_eq, DOWN).align_to(carga_eq, LEFT)

        self.play(Write(carga_eq), Write(valor_e))
        self.wait(1)

class leyDeCoulomb(Scene):
    def construct(self):
        ley_coulomb = Text("Ley de Coulomb:", color=BLUE).scale(0.7).to_edge(UP)
        self.play(Write(ley_coulomb))

        # Diagrama de cargas
        q1 = Dot(LEFT * 3 + DOWN * 3, color=RED)
        q2 = Dot(RIGHT * 1 + UP * 1, color=BLUE)
        r_arrow = DoubleArrow(q1.get_center(), q2.get_center(), buff=0, color=YELLOW)
        labels = VGroup(
            MathTex("q_1").scale(0.7).next_to(q1, DOWN),
            MathTex("q_2").scale(0.7).next_to(q2, UP),
            MathTex("R").scale(0.9).next_to(r_arrow, RIGHT).set_color(YELLOW)
        )
        diagrama = VGroup(q1, q2, r_arrow, labels).scale(0.8).next_to(ley_coulomb, DOWN, buff=0.5)
        self.play(Create(diagrama))
        self.wait(1)

        # Proporcionalidad
        proporcion = MathTex("F \\propto \\frac{|q_1||q_2|}{R^2}").next_to(diagrama, DOWN, buff=0.5)
        self.play(Write(proporcion))
