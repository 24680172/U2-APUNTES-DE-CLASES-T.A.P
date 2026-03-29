import flet as ft

# Definición del componente personalizado (Subtema 2.3)
class TarjetaPerfil(ft.Container):
    def __init__(self, nombre, rol, color_borde=ft.Colors.BLUE):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text(nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(rol, italic=True),
                # El botón busca la instrucción en self.saludar
                ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
            ],
            tight=True
        )
        # Usamos ft.Border.all para evitar las advertencias que viste en consola
        self.border = ft.Border.all(2, color_borde)
        self.padding = 10
        self.border_radius = 10
        self.width = 200

    # El flujo del programa salta a esta función al hacer clic
    def saludar(self, e):
        # Se ejecuta el print con los datos del componente
        print(f"Interactuando con el componente de {self.content.controls[0].value}")

def main(page: ft.Page):
    page.title = "Unidad 2: Componentes Definidos por el Usuario"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Instanciando nuestros componentes personalizados
    usuario1 = TarjetaPerfil("Ana García", "Desarrolladora Senior", ft.Colors.GREEN)
    usuario2 = TarjetaPerfil("Carlos Ruiz", "Arquitecto de Software")

    page.add(
        ft.Text("Lista de Usuarios", size=30, weight="bold"),
        ft.Row([usuario1, usuario2], alignment=ft.MainAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.app(target=main)