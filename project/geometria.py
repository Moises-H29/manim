from manim import *

class titulo(Scene):
    def construct(self):
        # Título
        titulo = Text("Ley de Coulomb en forma vectorial", color=RED).scale(1.2)
        moises = Text("Hernandez Pacheco Moises").scale(0.6).next_to(titulo,DOWN,buff=0.5)
        self.play(FadeIn(titulo))
        self.play(Write(moises))
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

class VectorDiagramWithText(Scene):
    def construct(self):
        # Diagrama vectorial (como antes)
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 4, 1],
            tips=True,
            axis_config={"include_numbers": False}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        origin = axes.c2p(0, 0)
        pos_r1 = axes.c2p(2, 1)
        pos_r2 = axes.c2p(5, 3)

        vec_r1 = Arrow(start=origin, end=pos_r1, buff=0, color=BLUE)
        label_r1 = MathTex(r"\vec{r}_1", color=BLUE).next_to(vec_r1, DOWN)

        vec_r2 = Arrow(start=origin, end=pos_r2, buff=0, color=GREEN)
        label_r2 = MathTex(r"\vec{r}_2", color=GREEN).next_to(vec_r2, UP)

        vec_R12 = Arrow(start=pos_r1, end=pos_r2, buff=0, color=PURPLE)
        label_R12 = MathTex(r"\vec{R}_{12}", color=PURPLE).next_to(vec_R12, DOWN)

        vec_a12 = Arrow(start=pos_r1, end=axes.c2p(3.2, 1.8), buff=0, color=RED)
        label_a12 = MathTex(r"\hat{a}_{12}", color=RED).next_to(vec_a12, DOWN)

        vec_F2 = Arrow(start=pos_r2, end=axes.c2p(5.7, 3.6), buff=0, color=YELLOW)
        label_F2 = MathTex(r"\vec{F}_2", color=YELLOW).next_to(vec_F2, RIGHT)

        q1_dot = Dot(pos_r1, color=WHITE)
        q2_dot = Dot(pos_r2, color=WHITE)
        label_q1 = MathTex("q_1").next_to(q1_dot, DOWN)
        label_q2 = MathTex("q_2").next_to(q2_dot, UP)

        diagram_group = VGroup(
            axes, labels,
            vec_r1, label_r1,
            vec_r2, label_r2,
            vec_R12, label_R12,
            vec_a12, label_a12,
            vec_F2, label_F2,
            q1_dot, label_q1,
            q2_dot, label_q2
        ).scale(0.65).to_edge(LEFT)

        # Texto de fórmulas a la derecha
        formulas = VGroup(
            MathTex(r"\vec{r}_1 + \vec{R}_{12} = \vec{r}_2"),
            MathTex(r"\vec{R}_{12} = \vec{r}_2 - \vec{r}_1"),
            MathTex(r"\|\vec{F}_2\| = K \frac{q_1 q_2}{\|\vec{R}_{12}\|^2}"),
            MathTex(r"\hat{a}_{12} = \text{Unitario}").set_color(RED),
            MathTex(r"\hat{a}_{12}: \text{Vector unitario de 1 a 2}"),
            MathTex(r"\hat{a} = \frac{\vec{R}_{12}}{\|\vec{R}_{12}\|}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).scale(0.65).to_edge(RIGHT)

        # Animación
        self.play(Create(axes), Write(labels))
        self.play(GrowArrow(vec_r1), Write(label_r1))
        self.play(GrowArrow(vec_r2), Write(label_r2))
        self.play(FadeIn(q1_dot), Write(label_q1))
        self.play(FadeIn(q2_dot), Write(label_q2))
        self.play(GrowArrow(vec_R12), Write(label_R12))
        self.play(GrowArrow(vec_a12), Write(label_a12))
        self.play(GrowArrow(vec_F2), Write(label_F2))

        self.wait()

        for formula in formulas:
            self.play(Write(formula))
            self.wait(0.5)

        self.wait(2)

class Vectorial(Scene):
    def construct(self):
        # Título
        titulo = Text("Sustituimos en la Ley de Coulomb:", color=RED, font_size=38).to_edge(UP)

        # Columna izquierda
        col1_eq1 = MathTex(r"\vec{F}_2 = \dfrac{K \, q_1 q_2}{\lVert \vec{R}_{12} \rVert^2} \, \hat{a}_{12}").scale(0.6)
        col1_eq2 = MathTex(r"\vec{F} = \dfrac{K \, q_1 q_2}{\lVert \vec{R}_{12} \rVert^2} \, \dfrac{\vec{R}_{12}}{\lVert \vec{R}_{12} \rVert}").scale(0.6)
        col1_eq3 = MathTex(r"\vec{F} = K \, \dfrac{q_1 q_2 \, \vec{R}_{12}}{\lVert \vec{R}_{12} \rVert^3}").scale(0.6)
        col1 = VGroup(col1_eq1, col1_eq2, col1_eq3).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        # Columna derecha
        texto_sust = Text("Sustituimos", font_size=23)
        texto_vec = MathTex(r"\lVert \vec{R}_{12} \rVert \text{ por } \lVert \vec{r}_2 - \vec{r}_1 \rVert").scale(0.6)
        eq_final = MathTex(
            r"\vec{F} = K \, \dfrac{q_1 q_2 (\vec{r}_2 - \vec{r}_1)}{\lVert \vec{r}_2 - \vec{r}_1 \rVert^3}"
        ).set_color(BLUE)
        texto_forma = Text("Forma vectorial de la ley de Coulomb.", color=BLUE, font_size=28)
        k_eq = MathTex(r"\text{Con } K = \dfrac{1}{4 \pi \varepsilon_0}").scale(0.6)

        col2 = VGroup(
            texto_sust,
            texto_vec,
            eq_final,
            texto_forma,
            k_eq
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)

        # Organizar columnas lado a lado
        contenido = VGroup(col1, col2).arrange(RIGHT, buff=1.2).next_to(titulo, DOWN, buff=0.5)

        # Mostrar
        self.play(Write(titulo))
        self.wait(0.3)
        for eq in col1:
            self.play(Write(eq))
            self.wait(0.2)
        for elem in col2:
            self.play(Write(elem))
            self.wait(0.2)
        self.wait(2)


class Ejercicio(Scene):
    def construct(self):
        # Enunciado
        enunciado = Tex(
            r"Demostrar que la magnitud de la fuerza resultante que dos",
            r"partículas cargadas $q_1$ y $q_2$ ejercen sobre una carga de",
            r"prueba $Q$ dispuestas según la siguiente figura, dada por:",
            tex_environment="flushleft"
        ).scale(0.7).to_edge(UP)

        # Ecuación de la magnitud de la fuerza
        fuerza = MathTex(
            r"\left\lVert \vec{F} \right\rVert = \left[ \dfrac{Q}{4 \pi \varepsilon_0 (b^2 + d^2)^{3/2}} \right]",
            r"\sqrt{b^2(q_1 - q_2)^2 + d^2(q_1 + q_2)^2}"
        ).scale(0.8).next_to(enunciado, DOWN, aligned_edge=LEFT, buff=0.5)

        # Nota sobre la permitividad
        nota = Tex(r"Dónde $\varepsilon_0$ es la permitividad del vacío.").scale(0.7)
        nota.next_to(fuerza, DOWN, aligned_edge=LEFT, buff=0.5)

        # Mostrar todo
        self.play(Write(enunciado))
        self.wait(0.5)
        self.play(Write(fuerza))
        self.wait(0.5)
        self.play(Write(nota))
        self.wait(2)