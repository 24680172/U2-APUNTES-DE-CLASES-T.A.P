import flet as ft
import random


def main(page: ft.Page):
    page.title = "Piedra, Papel o Tijeras"
    page.window_width = 420
    page.window_height = 650
    page.bgcolor = "#0f172a"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    opciones = ["Piedra", "Papel", "Tijeras"]
    emojis = {"Piedra": "🪨", "Papel": "📄", "Tijeras": "✂️"}

    # Marcador
    score_user = 0
    score_cpu = 0

    marcador = ft.Text(
        "Tú 0  |  0 CPU",
        size=20,
        color="white",
        weight="bold"
    )

    resultado = ft.Text(size=24, weight="bold")
    user_pick = ft.Text(color="white")
    cpu_pick = ft.Text(color="white")

    # Animación
    resultado_container = ft.Container(
        content=resultado,
        padding=15,
        border_radius=15,
        bgcolor="#1e293b",
        animate=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
    )

    def jugar(eleccion):
        nonlocal score_user, score_cpu

        maquina = random.choice(opciones)

        user_pick.value = f"Tú: {emojis[eleccion]} {eleccion}"
        cpu_pick.value = f"CPU: {emojis[maquina]} {maquina}"

        # Lógica
        if eleccion == maquina:
            resultado.value = "Empate "
            resultado_container.bgcolor = "#334155"

        elif (
            (eleccion == "Piedra" and maquina == "Tijeras")
            or (eleccion == "Papel" and maquina == "Piedra")
            or (eleccion == "Tijeras" and maquina == "Papel")
        ):
            score_user += 1
            resultado.value = "¡Ganaste! "
            resultado_container.bgcolor = "#065f46"

        else:
            score_cpu += 1
            resultado.value = "Perdiste "
            resultado_container.bgcolor = "#7f1d1d"

        marcador.value = f"Tú {score_user}  |  {score_cpu} CPU"

        page.update()

    def boton_jugada(nombre, color):
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Column(
                    [
                        ft.Text(emojis[nombre], size=30),
                        ft.Text(nombre)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                style=ft.ButtonStyle(
                    bgcolor=color,
                    color="white",
                    shape=ft.RoundedRectangleBorder(radius=15),
                    padding=15,
                ),
                on_click=lambda e: jugar(nombre),
            ),
            expand=True,
        )

    # Tarjeta principal
    card = ft.Container(
        width=360,
        padding=25,
        border_radius=25,
        bgcolor="#1e293b",
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=15,
            color="black",
        ),
        content=ft.Column(
            [
                ft.Text(
                    "Piedra, Papel o Tijeras",
                    size=28,
                    weight="bold",
                    color="white",
                    text_align="center",
                ),
                marcador,
                ft.Divider(color="#334155"),

                ft.Text("Elige tu jugada:", color="white"),
                ft.Row(
                    [
                        boton_jugada("Piedra", "#2563eb"),
                        boton_jugada("Papel", "#9333ea"),
                        boton_jugada("Tijeras", "#f97316"),
                    ],
                    spacing=10,
                ),

                ft.Divider(color="#334155"),
                user_pick,
                cpu_pick,
                resultado_container,
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    page.add(card)


ft.app(target=main)