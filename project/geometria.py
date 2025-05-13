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
            MathTex("q_1").scale(0.9).next_to(q1, DOWN),
            MathTex("q_2").scale(0.9).next_to(q2, UP),
            MathTex("R").scale(1.1).next_to(r_arrow, RIGHT * 0.1).set_color(YELLOW)
        )
        diagrama = VGroup(q1, q2, r_arrow, labels).scale(0.8).next_to(ley_coulomb, DOWN, buff=0.5)
        self.play(Create(diagrama))
        self.wait(1)

        # Proporcionalidad
        proporcion = MathTex("F \\propto \\frac{|q_1||q_2|}{R^2}").next_to(diagrama, DOWN, buff=0.5)
        self.play(Write(proporcion))

class SistemaInternacional(Scene):
    def construct(self):
        # Título
        sistemaI = Text("En el S.I.", color=BLUE).scale(0.7).to_edge(UP)
        self.play(Write(sistemaI))

        # Fórmula de la Ley de Coulomb en el SI
        formula_si = MathTex("F = k \\frac{|q_1||q_2|}{R^2}").scale(0.8).next_to(sistemaI, DOWN, buff=0.5)
        constante_k = MathTex("k = 9 \\times 10^9 \\, \\frac{\\text{Nm}^2}{\\text{C}^2}").scale(0.8).next_to(formula_si, DOWN)
        self.play(Write(formula_si), Write(constante_k))
        self.wait(1)

        # Explicación sobre el coulomb
        coulomb = Text("El coulomb es la unidad de medida de la carga").scale(0.5).next_to(constante_k, DOWN, buff=0.5)
        self.play(FadeIn(coulomb))

        # k como función de epsilon_0
        k_expr = MathTex("k = \\frac{1}{4 \\pi \\varepsilon_0}").scale(0.8).next_to(coulomb, DOWN, buff=0.5)
        self.play(Write(k_expr))

        # Explicación de epsilon_0
        epsilon = MathTex("\\text{Aquí } \\varepsilon_0 \\text{ es la permitividad del vacío (constante)}").scale(0.8).next_to(k_expr, DOWN, buff=0.5)
        self.play(FadeIn(epsilon))

        # Valor numérico de epsilon_0
        epsilon_val = MathTex("\\varepsilon_0 = 8.85 \\times 10^{-12} \\, \\frac{\\text{C}^2}{\\text{Nm}^2}").scale(0.8).next_to(epsilon, DOWN)
        self.play(Write(epsilon_val))

        self.wait(2)

class CargaElectron(Scene):
    def construct(self):
        # Título
        titulo = Text("La carga del electrón:", color=BLUE).scale(0.8).to_edge(UP)
        self.play(Write(titulo))

        # Primera ecuación: e⁻ = 1.6 × 10⁻¹⁹ C
        eq1 = MathTex("e^-", "=", "1.6 \\times 10^{-19}", "\\,\\text{C}").scale(0.9).next_to(titulo, DOWN, buff=0.6)
        self.play(Write(eq1))
        self.wait(1)

        # Segunda ecuación: 1C = (1 / 1.6×10⁻¹⁹) e⁻
        eq2 = MathTex("1\\,\\text{C}", "=", "\\frac{1}{1.6 \\times 10^{-19}}", "e^-").scale(0.9).next_to(eq1, DOWN, buff=0.6)
        self.play(Write(eq2))
        self.wait(1)

        # Tercera ecuación: = 6×10¹⁸ e⁻
        eq3 = MathTex("= 6 \\times 10^{18} \\; e^-").scale(0.9).next_to(eq2, DOWN, buff=0.4).align_to(eq2, LEFT)
        self.play(Write(eq3))
        self.wait(2)

class DireccionFuerzaElectrostatica(Scene):
    def construct(self):
        # Título
        titulo = Text("Dirección de la fuerza electrostática", color=BLUE).scale(0.6).to_edge(UP)
        self.play(Write(titulo))

        # Puntos de carga
        q1 = Dot(LEFT * 3, color=RED)
        q2 = Dot(RIGHT * 3, color=RED)

        # Cargas q1 y q2
        q1_label = MathTex("q_1", color=RED).scale(0.7).next_to(q1, UP, buff=0.2)
        q2_label = MathTex("q_2", color=RED).scale(0.7).next_to(q2, UP, buff=0.2)

        # Fuerzas
        f1 = Arrow(q1.get_center(), q1.get_center() + LEFT * 1.2, buff=0.05, color=GREEN)
        f2 = Arrow(q2.get_center(), q2.get_center() + RIGHT * 1.2, buff=0.05, color=GREEN)
        f1_label = MathTex("\\vec{F}_1", color=GREEN).scale(0.6).next_to(f1, LEFT)
        f2_label = MathTex("\\vec{F}_2", color=GREEN).scale(0.6).next_to(f2, RIGHT)


        # Dirección
        direccion = DashedLine(q1.get_center(), q2.get_center(), color=RED)
        direccion_label = Text("Dirección", color=RED).scale(0.4).next_to(direccion, UP)

        # Línea R
        linea_r = Line(q1.get_center() + DOWN * 0.6, q2.get_center() + DOWN * 0.6)
        inicio = Line(UP * 0.2, DOWN * 0.2).move_to(linea_r.get_start())
        fin = Line(UP * 0.2, DOWN * 0.2).move_to(linea_r.get_end())

        linea_con_bordes = VGroup(inicio, linea_r, fin)
        r_label = MathTex("R").scale(0.8).next_to(linea_r, DOWN)

        # Texto explicativo
        explicacion = Text("En este caso, con fuerzas opuestas, cargas iguales se repelen", font_size=24)
        explicacion.next_to(linea_r, DOWN, buff=1)

        # Mostrar objetos
        self.play(Write(q1), Write(q2), Write(q1_label), Write(q2_label))
        self.play(GrowArrow(f1), GrowArrow(f2), Write(f1_label), Write(f2_label))
        self.play(Create(direccion), Write(direccion_label))
        self.play(Create(linea_con_bordes), Write(r_label))
        self.wait(0.5)
        self.play(Write(explicacion))
        self.wait(2)
