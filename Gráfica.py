import flet as ft
import flet_charts as fch
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io
import base64

def generar_imagen(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

def main(page: ft.Page):
    page.title = "4 Gráficas en 2 Columnas"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    # ─── 1. LÍNEAS (matplotlib) ───
    fig1, ax1 = plt.subplots()
    ax1.plot([1,2,3,4,5], [10,25,15,40,30], color="blue", marker="o", label="2024")
    ax1.plot([1,2,3,4,5], [5,15,20,30,50], color="red", marker="s", label="2025")
    ax1.set_title("Ventas Anuales")
    ax1.legend()
    ax1.set_xlabel("Mes")
    ax1.set_ylabel("Ventas")

    # ─── 2. DISPERSIÓN (matplotlib) ───
    fig2, ax2 = plt.subplots()
    ax2.scatter([1,2,3,4,5,6,7], [5,8,3,9,6,2,7],
                color="purple", s=150, alpha=0.7)
    ax2.set_title("Dispersión de Datos")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")

    # ─── 3. LÍNEAS (flet-charts) ───
    lineas = fch.LineChart(
        data_series=[
            fch.LineChartData(
                color=ft.Colors.GREEN,
                stroke_width=3,
                points=[
                    fch.LineChartDataPoint(0, 20),
                    fch.LineChartDataPoint(1, 45),
                    fch.LineChartDataPoint(2, 30),
                    fch.LineChartDataPoint(3, 70),
                    fch.LineChartDataPoint(4, 55),
                ],
            ),
            fch.LineChartData(
                color=ft.Colors.ORANGE,
                stroke_width=3,
                points=[
                    fch.LineChartDataPoint(0, 10),
                    fch.LineChartDataPoint(1, 30),
                    fch.LineChartDataPoint(2, 50),
                    fch.LineChartDataPoint(3, 25),
                    fch.LineChartDataPoint(4, 65),
                ],
            ),
        ],
        height=220,
        expand=True,
    )

    # ─── 4. BARRAS (flet-charts) ───
    barras = fch.BarChart(
        groups=[
            fch.BarChartGroup(x=0, rods=[fch.BarChartRod(from_y=0, to_y=55, width=25, color=ft.Colors.CYAN)]),
            fch.BarChartGroup(x=1, rods=[fch.BarChartRod(from_y=0, to_y=30, width=25, color=ft.Colors.PINK)]),
            fch.BarChartGroup(x=2, rods=[fch.BarChartRod(from_y=0, to_y=75, width=25, color=ft.Colors.AMBER)]),
            fch.BarChartGroup(x=3, rods=[fch.BarChartRod(from_y=0, to_y=45, width=25, color=ft.Colors.TEAL)]),
        ],
        max_y=100,
        height=220,
        expand=True,
    )

    page.add(
        ft.Text("📊 4 Gráficas", size=28, weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER),
        ft.Divider(),

        # ── Fila 1 ──
        ft.Row(
            [
                ft.Column([
                    ft.Text("1. Líneas (matplotlib)", size=16, weight=ft.FontWeight.BOLD),
                    ft.Image(src=generar_imagen(fig1), width=380),
                ], expand=True),
                ft.Column([
                    ft.Text("2. Dispersión (matplotlib)", size=16, weight=ft.FontWeight.BOLD),
                    ft.Image(src=generar_imagen(fig2), width=380),
                ], expand=True),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),

        ft.Divider(),

        # ── Fila 2 ──
        ft.Row(
            [
                ft.Column([
                    ft.Text("3. Líneas (flet-charts)", size=16, weight=ft.FontWeight.BOLD),
                    lineas,
                ], expand=True),
                ft.Column([
                    ft.Text("4. Barras (flet-charts)", size=16, weight=ft.FontWeight.BOLD),
                    barras,
                ], expand=True),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        ),
    )

ft.run(main)