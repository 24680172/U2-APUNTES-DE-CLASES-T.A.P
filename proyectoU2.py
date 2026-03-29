import flet as ft
from product_card import ProductCard

# Lista de productos
productos = [
    {"id": 1, "nombre": "Laptop Gamer", "descripcion": "Ryzen 7 16GB RAM", "precio": 25000, "ruta_imagen": "laptopgamer.jpg"},
    {"id": 2, "nombre": "Mouse Gamer", "descripcion": "Mouse RGB", "precio": 350, "ruta_imagen": "mouse.jpg"},
    {"id": 3, "nombre": "Teclado Mecánico", "descripcion": "Switch blue RGB", "precio": 1200, "ruta_imagen": "teclado.jpg"},
    {"id": 4, "nombre": "Audifonos Gamer", "descripcion": "Sonido envolvente", "precio": 900, "ruta_imagen": "audifonosg.jpg"},
    {"id": 5, "nombre": "Televisión 32", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "televisor.jpg"},
    {"id": 6, "nombre": "Audifonos", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "audifonos.jpg"},
    {"id": 7, "nombre": "Cargador", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "cargador.jpg"},
    {"id": 8, "nombre": "Impresora", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "impresora.jpg"},
    {"id": 9, "nombre": "Tablet", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "tablet.jpg"},
    {"id": 10, "nombre": "Smartwatch", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "smartwatch.jpg"},
    {"id": 11, "nombre": "Laptop", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "laptop.jpg"},
    {"id": 12, "nombre": "Bocina", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "bocina.jpg"},
    {"id": 13, "nombre": "Multicontactos", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "multicontacto.jpg"},
    {"id": 14, "nombre": "Microfono", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "microfono.jpg"},
    {"id": 15, "nombre": "Router", "descripcion": "Full HD 144Hz", "precio": 4200, "ruta_imagen": "router.jpg"},
]

def main(page: ft.Page):
    page.title = "TECHNOLOGY STORE"
    page.scroll = "auto"
    page.bgcolor = "#000000"
    page.padding = 20
    page.assets_dir = "assets"

    carrito = []
    favoritos = []
    
    carrito_text = ft.Text("0", size=14)
    favoritos_text = ft.Text("0", size=14)
    
    def mostrar_mensaje(msg):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(msg),
        )
        page.snack_bar.open = True
        page.update()
    
    def agregar_carrito(producto):
        carrito.append(producto)
        carrito_text.value = str(len(carrito))
        mostrar_mensaje(f"{producto['nombre']} agregado")
        page.update()
    
    def agregar_favorito(producto):
        if producto not in favoritos:
            favoritos.append(producto)
        else:
            favoritos.remove(producto)
        favoritos_text.value = str(len(favoritos))
        page.update()

    # HEADER
    header = ft.Row(
        [
            ft.Text("TECHNOLOGY STORE", size=26, weight="w500"),
            ft.Row(
                [
                    ft.Row([ft.Text("♡"), favoritos_text], spacing=4),
                    ft.Row([ft.Text("🛒"), carrito_text], spacing=4),
                ],
                spacing=15
            )
        ],
        alignment="spaceBetween"
    )

    # TARJETAS
    tarjetas = []
    for p in productos:
        card = ProductCard(
            p["nombre"],
            p["descripcion"],
            p["precio"],
            p["ruta_imagen"]
        )
        
        # Botón carrito
        card.agregar = lambda e, prod=p: agregar_carrito(prod)

        # Botón favorito funcional
        def make_fav_handler(prod, card_ref):
            def handler(e):
                agregar_favorito(prod)

                # Cambiar icono visual
                if prod in favoritos:
                    card_ref.fav_icon.value = "❤️"
                else:
                    card_ref.fav_icon.value = "🤍"
                
                card_ref.fav_icon.update()
            return handler

        

        tarjetas.append(
            ft.Container(
                content=card,
                padding=5
            )
        )

    # GRID
    grid = ft.Row(
        controls=tarjetas,
        wrap=True,
        spacing=15,
        run_spacing=15
    )

    page.add(
        header,
        ft.Container(height=10),
        grid
    )

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")