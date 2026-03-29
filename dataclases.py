import flet as ft
from dataclasses import dataclass

@dataclass
class Usuario:
    nombre: str
    rol: str
    color_borde: str = ft.Colors.BLUE

class TarjetaPerfil(ft.Container):
    def __init__(self, data: Usuario):
        super().__init__()
        self.data = data
        
        self.padding = 10
        self.border_radius = 10
        self.border = ft.Border.all(2, self.data.color_borde)
        self.width = 250  
        
        self.content = ft.Column(
            controls=[
                ft.Text(self.data.nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(self.data.rol, italic=True),
                ft.Button("Ver Perfil", on_click=self.saludar)
            ],
            tight=True,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )

    def saludar(self, e):
        print(f"Interactuando con: {self.data.nombre}")

def main(page: ft.Page):
    page.title = "Unidad 2: Data Class corregido"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Datos
    u1 = Usuario("Ana García", "Desarrolladora Senior", ft.Colors.GREEN)
    u2 = Usuario("Carlos Ruiz", "Arquitecto de Software", ft.Colors.BLUE)

    tarjetas = [TarjetaPerfil(u1), TarjetaPerfil(u2)]

    page.add(
        ft.Text("Lista de Usuarios", size=30, weight="bold"),
        ft.Row(
            tarjetas, 
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )

if __name__ == "__main__":
    
    try:
        ft.run(main)
    except AttributeError:
        ft.app(main)