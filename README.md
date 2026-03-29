# **Arquitectura de Sistemas en Python: Componentes, Librerías y la Evolución de la Modularidad**
La ingeniería de software contemporánea ha trascendido la escritura de código lineal para enfocarse en la construcción de sistemas robustos, escalables y mantenibles a través de la modularidad. En el ecosistema de Python, esta modularidad no es solo una característica sintáctica, sino una filosofía estructural que permite a los desarrolladores gestionar la complejidad dividiendo tareas extensas en unidades discretas y reutilizables. La programación modular se fundamenta en la premisa de que un sistema complejo es más fácil de comprender y evolucionar si sus partes están claramente delimitadas, lo que reduce la carga cognitiva del programador y minimiza el impacto colateral de los cambios en el código. En este contexto, el estudio de los componentes, paquetes y librerías en Python constituye la base técnica sobre la cual se erige cualquier arquitectura de software profesional.

## 2.1 Definición conceptual de componentes, paquetes y librerías
La organización del código en Python se articula mediante una jerarquía de abstracciones que comienza en el nivel atómico del módulo y escala hacia estructuras complejas de distribución. Un módulo, en su definición más fundamental, es un objeto que sirve como unidad organizativa de código, generalmente contenido en un archivo con extensión .py. Estos módulos permiten albergar definiciones de funciones, clases y variables, estableciendo un espacio de nombres (namespace) privado que actúa como un contenedor global para todos los objetos definidos en su interior. La importancia de este espacio de nombres radica en la prevención de colisiones de identificadores; dos funciones con el mismo nombre pueden coexistir en un sistema siempre que residan en módulos diferentes, lo que facilita la colaboración en proyectos de gran envergadura.

Técnicamente, Python permite la creación de módulos a través de tres mecanismos distintos: archivos escritos en el propio lenguaje Python, extensiones escritas en lenguaje C que se cargan dinámicamente en tiempo de ejecución —como el módulo de expresiones regulares re—, y módulos integrados (built-in) que forman parte intrínseca del intérprete, como itertools o sys. Cuando el intérprete procesa una sentencia de importación, busca el módulo en una lista de directorios definida en sys.path, que incluye el directorio actual, las variables de entorno como PYTHONPATH y las rutas de instalación estándar.

Ascendiendo en la jerarquía, el paquete representa una forma de estructurar el espacio de nombres de los módulos mediante una "notación de puntos" (dot notation). Un paquete es, en esencia, un módulo de Python que posee un atributo __path__, lo que le permite contener submódulos o, de manera recursiva, subpaquetes. Físicamente, un paquete se manifiesta como un directorio en el sistema de archivos que tradicionalmente incluye un archivo especial denominado __init__.py. Este archivo es crucial por varias razones: primero, indica al intérprete que el directorio debe ser tratado como un paquete; segundo, permite ejecutar código de inicialización cuando el paquete se importa por primera vez; y tercero, ofrece un mecanismo para controlar el acceso a los nombres internos mediante la variable __all__, definiendo qué elementos se exponen durante una importación masiva con el operador asterisco.

| Concepto   | Nivel de Abstracción | Implementación Técnica              | Propósito en la Arquitectura                                      |
|------------|---------------------|------------------------------------|-------------------------------------------------------------------|
| Módulo     | Básico              | Archivo .py, .so o integrado       | Encapsular lógica específica y proteger el namespace.            |
| Paquete    | Intermedio          | Directorio con módulos e __init__.py | Organizar jerárquicamente dominios de problemas relacionados.    |
| Librería   | Alto                | Colección de paquetes y módulos    | Proveer una solución integral para un área funcional.            |
| Componente | Arquitectónico      | Unidad independiente y reemplazable | Facilitar el despliegue y la reutilización basada en contratos.  |

La distinción entre paquetes regulares y paquetes de espacio de nombres (namespace packages) es vital para entender la distribución moderna. Los paquetes regulares son autocontenidos en una única jerarquía de directorios, mientras que los paquetes de espacio de nombres, formalizados en el PEP 420, permiten que las partes de un solo paquete lógico residan en múltiples ubicaciones físicas en el disco. Esta capacidad es fundamental para ecosistemas extensibles donde diferentes proveedores pueden contribuir a un mismo prefijo de importación sin interferir físicamente en los archivos de los demás. Aunque los paquetes de espacio de nombres carecen de un archivo __init__.py, se comportan de manera idéntica a los paquetes regulares una vez cargados en memoria, aunque su implementación interna es más compleja para el cargador de Python.

El término "librería" o "biblioteca", aunque ubicuo, carece de una definición técnica estricta en la documentación oficial de Python, utilizándose de manera más informal para describir colecciones de paquetes diseñadas para proporcionar utilidades orientadas a programas externos. Una librería, como NumPy o Pandas, integra múltiples paquetes y módulos para resolver problemas complejos en un dominio específico, como la computación científica o el análisis de datos. En el contexto de la Ingeniería de Software Basada en Componentes (CBSE), el "componente" se define como una unidad de software casi independiente y reemplazable que cumple una función clara y se comunica a través de interfaces bien definidas. A diferencia de un simple módulo de código, un componente es una construcción de mayor nivel que enfatiza la separación de preocupaciones y la independencia de implementación, permitiendo que un sistema se ensamble a partir de piezas preexistentes y probadas.

### Ejemplo Práctico
```Python
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
```
**1. Definición del Modelo de Datos (dataclass)**

En este bloque se define la estructura de los datos que usará la aplicación. Usar @dataclass ahorra escribir el método __init__ manualmente.

```Python
@dataclass
class Usuario:
    nombre: str
    rol: str
    color_borde: str = ft.Colors.BLUE
```
- Propósito: Crear un "molde" para los usuarios.
- Detalle: Define qué información necesita cada perfil (nombre, rol y un color opcional para el borde).

**2. El Componente Visual (TarjetaPerfil)**

Aquí es donde ocurre la magia de la Programación Orientada a Objetos aplicada a la UI. Se crea un componente personalizado que hereda de ft.Container.

```Python
class TarjetaPerfil(ft.Container):
    def __init__(self, data: Usuario):
        super().__init__()
        self.data = data
        
        # Configuración visual del contenedor
        self.padding = 10
        self.border_radius = 10
        self.border = ft.Border.all(2, self.data.color_borde)
        self.width = 250  
        
        # Contenido interno: Una columna con textos y un botón
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
```
- super().__init__(): Inicializa las propiedades básicas del contenedor de Flet.
- Encapsulamiento: La tarjeta sabe cómo dibujarse a sí misma usando el objeto Usuario que recibe.
- Interactividad: El método saludar maneja el evento de clic del botón.

**3. La Función Principal (main)**

Este bloque configura la ventana de la aplicación y orquesta la creación de los elementos.

```Python
def main(page: ft.Page):
    page.title = "Unidad 2: Data Class corregido"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Creación de instancias de datos
    u1 = Usuario("Ana García", "Desarrolladora Senior", ft.Colors.GREEN)
    u2 = Usuario("Carlos Ruiz", "Arquitecto de Software", ft.Colors.BLUE)

    # Creación de la lista de componentes visuales
    tarjetas = [TarjetaPerfil(u1), TarjetaPerfil(u2)]

    # Renderizado en la página
    page.add(
        ft.Text("Lista de Usuarios", size=30, weight="bold"),
        ft.Row(
            tarjetas, 
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )
```

- Instanciación: Se crean dos objetos Usuario.
- Mapeo: Se transforman esos datos en objetos TarjetaPerfil.
- ft.Row: Organiza las tarjetas de forma horizontal.

**4. Punto de Entrada y Compatibilidad**

Este último bloque asegura que la aplicación se ejecute correctamente independientemente de la versión de Flet o del entorno.

```Python
if __name__ == "__main__":
    try:
        ft.run(main) # Método moderno
    except AttributeError:
        ft.app(main) # Método tradicional/fallback
```

**Ejecución**
<img width="1568" height="874" alt="image" src="https://github.com/user-attachments/assets/13ce717b-55b4-4216-9311-f106903df0e2" />

## 2.2 Uso de librerías proporcionadas por el lenguaje
Python se distingue por su filosofía de "baterías incluidas", lo que significa que el lenguaje se distribuye con una biblioteca estándar extensa que permite a los desarrolladores abordar una amplia variedad de tareas sin depender de paquetes externos. Esta biblioteca estándar no es solo una conveniencia, sino una garantía de portabilidad y estabilidad, ya que sus módulos están diseñados para funcionar de manera coherente en diversas plataformas y arquitecturas.

La biblioteca estándar se organiza en categorías funcionales que cubren desde el procesamiento de texto y servicios de datos hasta la interacción con el sistema operativo y protocolos de red. Módulos como os y shutil proporcionan interfaces para interactuar con el sistema de archivos de manera agnóstica a la plataforma, permitiendo la creación de directorios, copia de archivos y manipulación de rutas de manera segura. Por otro lado, módulos como sys ofrecen acceso a parámetros y funciones específicos del intérprete de Python, permitiendo la gestión de argumentos de línea de comandos a través de sys.argv o la terminación controlada de programas mediante sys.exit().

Para la gestión de datos y algoritmos, Python provee módulos potentes como collections, que introduce tipos de datos especializados como namedtuple y defaultdict, y itertools, que ofrece herramientas para la creación de iteradores eficientes. En el ámbito de la red, aunque módulos como ftplib y smtplib siguen presentes para protocolos heredados, la tendencia moderna se inclina hacia el uso de asyncio para la programación asíncrona, permitiendo manejar múltiples conexiones de red de manera concurrente sin la sobrecarga de los hilos de ejecución tradicionales.

| Categoría               | Módulos Representativos        | Funcionalidad Principal                                      |
|------------------------|-------------------------------|--------------------------------------------------------------|
| Interfaz de SO         | os, shutil, pathlib           | Gestión de archivos, directorios y rutas de sistema.         |
| Procesamiento de Texto | re, string, textwrap          | Manipulación de cadenas y expresiones regulares.             |
| Servicios de Datos     | datetime, collections, heapq  | Tipos de datos avanzados y gestión de tiempo.                |
| Matemáticas            | math, random, statistics      | Funciones científicas, estadísticas y generación aleatoria.  |
| Persistencia           | pickle, sqlite3, json         | Almacenamiento y serialización de datos.                     |

A pesar de su amplitud, la biblioteca estándar ha experimentado un proceso de revisión crítica bajo el PEP 594, que propone la eliminación de "baterías muertas". Muchos módulos incluidos en las primeras versiones de Python se han vuelto obsoletos debido a cambios tecnológicos o han sido superados por alternativas de la comunidad mucho más robustas. La eliminación de estos módulos, que incluyen utilidades para formatos de audio de los años 80 como sunau o implementaciones de red ineficientes como cgi, reduce la carga de mantenimiento para el equipo central de desarrollo de CPython y mejora la seguridad al eliminar superficies de ataque poco probadas.

Este adelgazamiento de la biblioteca estándar es particularmente beneficioso para despliegues modernos en entornos con recursos limitados, como dispositivos de Internet de las Cosas (IoT) o aplicaciones que se ejecutan en navegadores web mediante WebAssembly (WASM). El calendario de depreciación asegura que los desarrolladores tengan tiempo suficiente para migrar sus aplicaciones: los módulos afectados emitieron advertencias en la versión 3.11, se mantuvieron con advertencias en la 3.12 y son eliminados definitivamente en la 3.13. Para aquellos casos donde el código antiguo sigue siendo necesario, la licencia permisiva de Python permite a las organizaciones "vendorizar" los módulos eliminados, incorporando el código directamente en sus bases de proyectos privados.

### Ejemplo Práctico
```Python
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
```

**1. Configuración de la Página y Variables de Estado**

En este bloque se define el aspecto visual de la ventana y se inicializan los datos que rastrearán el progreso del juego.

```Python
def main(page: ft.Page):
    page.title = "Piedra, Papel o Tijeras"
    page.window_width = 420
    page.window_height = 650
    page.bgcolor = "#0f172a" # Fondo oscuro tipo "slate"

    opciones = ["Piedra", "Papel", "Tijeras"]
    emojis = {"Piedra": "🪨", "Papel": "📄", "Tijeras": "✂️"}

    # Marcador (Estado inicial)
    score_user = 0
    score_cpu = 0
```
- Propósito: Establece el lienzo de la aplicación y las reglas básicas (opciones y emojis).
- Variables de score: Se declaran aquí para que persistan mientras la aplicación esté abierta.

**2. Definición de Componentes Visuales Dinámicos**

Aquí se crean los elementos de texto y contenedores que cambiarán su contenido durante el juego.

```Python
    marcador = ft.Text("Tú 0  |  0 CPU", size=20, color="white", weight="bold")
    resultado = ft.Text(size=24, weight="bold")
    user_pick = ft.Text(color="white")
    cpu_pick = ft.Text(color="white")

    # Contenedor con animación para el resultado
    resultado_container = ft.Container(
        content=resultado,
        padding=15,
        border_radius=15,
        bgcolor="#1e293b",
        animate=ft.Animation(500, ft.AnimationCurve.EASE_IN_OUT),
    )
```
animate: Esta propiedad es clave. Permite que cuando el color de fondo (bgcolor) cambie (verde si ganas, rojo si pierdes), la transición sea suave y no un salto brusco.

**3. Lógica del Juego (Función jugar)**

Este es el "cerebro" del programa. Se ejecuta cada vez que el usuario presiona un botón.

```Python
    def jugar(eleccion):
        nonlocal score_user, score_cpu # Permite modificar variables fuera de la función

        maquina = random.choice(opciones) # Elección aleatoria de la CPU

        # Lógica de comparación
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
            resultado_container.bgcolor = "#065f46" # Verde
        else:
            score_cpu += 1
            resultado.value = "Perdiste "
            resultado_container.bgcolor = "#7f1d1d" # Rojo

        marcador.value = f"Tú {score_user}  |  {score_cpu} CPU"
        page.update() # Refresca la interfaz para mostrar cambios
```
4. Fábrica de Botones (boton_jugada)
Para no repetir código tres veces (uno para cada opción), se crea una función que genera botones personalizados.

```Python
    def boton_jugada(nombre, color):
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Column(
                    [ft.Text(emojis[nombre], size=30), ft.Text(nombre)],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                on_click=lambda e: jugar(nombre), # Envía la elección a la función jugar
            ),
            expand=True,
        )
```
Lambda: Se usa lambda e: jugar(nombre) para que la función no se ejecute inmediatamente al cargar la página, sino solo al hacer clic.

**5. Construcción de la Interfaz (Layout)**

Finalmente, se agrupa todo dentro de un contenedor principal (card) con sombras y bordes redondeados.

```Python
    card = ft.Container(
        content=ft.Column([
            ft.Text("Piedra, Papel o Tijeras", size=28, weight="bold"),
            marcador,
            ft.Row([
                boton_jugada("Piedra", "#2563eb"),
                boton_jugada("Papel", "#9333ea"),
                boton_jugada("Tijeras", "#f97316"),
            ]),
            user_pick,
            cpu_pick,
            resultado_container,
        ])
    )
    page.add(card)
```
**Ejecución**
<img width="1562" height="867" alt="image" src="https://github.com/user-attachments/assets/2da2e4c8-41f4-4a75-ba19-148be716ce0f" />

**Estructura y Funcionamiento del Proyecto**

El desarrollo se basa en el aprovechamiento de librerías y la aplicación de patrones de diseño que optimizan la comunicación y el procesamiento de datos.

1. Gestión de Librerías
- Librerías Externas (Flask): Se utiliza para la construcción del entorno web. Flask abstrae la complejidad de la comunicación cliente-servidor mediante herramientas clave:
  - @app.route: Gestión de rutas de navegación.
  - request: Manejo de solicitudes de datos.
  - render_template: Renderizado de vistas dinámicas.

- Librerías Estándar (Random): Se emplea la librería nativa de Python para generar valores aleatorios, permitiendo simular la toma de decisiones de la computadora sin depender de instalaciones externas.

2. Arquitectura del Sistema

El proyecto sigue un modelo de Separación de Responsabilidades, dividiendo la lógica en tres etapas fundamentales:

| Etapa         | Componente          | Función                                                   |
|--------------|--------------------|-----------------------------------------------------------|
| Entrada       | request             | Captura de datos enviados por el usuario.                |
| Procesamiento | determinar_ganador  | Ejecución de la lógica interna del juego.                |
| Salida        | render_template     | Presentación de resultados en la interfaz visual.        |

**Visualización**
Web
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6bccc669-2d90-4743-9022-29b317e29aed" />

App
<img width="1080" height="2340" alt="image" src="https://github.com/user-attachments/assets/4e9d1600-8992-4dbe-9caf-7516cf680016" />


## 2.3 Creación de componentes (visuales y no visuales) definidos por el usuario

La creación de componentes personalizados en Python permite a los ingenieros extender las capacidades del lenguaje y construir abstracciones que se alineen perfectamente con las necesidades del dominio del problema. Esta actividad se divide en dos grandes áreas: el desarrollo de componentes visuales para interfaces gráficas de usuario (GUI) y el diseño de componentes no visuales orientados a la lógica de negocio y servicios de infraestructura.

**Desarrollo de componentes visuales y diseño de interfaces**

En el ámbito de las GUIs, Python ofrece diversas bibliotecas con filosofías arquitectónicas contrastantes. Tkinter, al ser la biblioteca estándar, se utiliza frecuentemente para prototipos rápidos y herramientas sencillas debido a su disponibilidad inmediata y facilidad de uso. Sin embargo, para aplicaciones profesionales con requisitos estéticos y de usabilidad modernos, los desarrolladores suelen optar por frameworks como PyQt (o su contraparte con licencia LGPL, PySide) o Kivy.

PyQt, basado en el framework Qt escrito en C++, proporciona un modelo de componentes extremadamente maduro donde los desarrolladores pueden crear widgets personalizados mediante herencia de clases base. Esta biblioteca permite una integración profunda con los servicios del sistema operativo y ofrece herramientas como Qt Designer para el diseño visual de interfaces, que luego se traducen a código Python. Por su parte, Kivy se especializa en aplicaciones multiplataforma con soporte para interfaces táctiles y gestos, utilizando OpenGL para renderizar sus propios componentes en lugar de depender de los widgets nativos del sistema. Kivy introduce el lenguaje KV, una sintaxis declarativa que permite separar drásticamente la estructura de la interfaz de la lógica de programación en Python, facilitando un flujo de trabajo similar al desarrollo web moderno con HTML/CSS.

Para gestionar la complejidad de estas interfaces, es fundamental aplicar patrones de diseño arquitectónico. El patrón Model-View-Controller (MVC) es uno de los más extendidos, dividiendo la aplicación en tres partes: el Modelo, que gestiona los datos y la lógica de negocio; la Vista, que representa la interfaz visual; y el Controlador, que actúa como puente procesando las entradas del usuario y actualizando el modelo. Esta separación garantiza que el modelo pueda ser reutilizado en contextos no visuales, como scripts automatizados o aplicaciones web, sin necesidad de modificar el código de datos. En aplicaciones de interfaz más modernas, el patrón Model-View-ViewModel (MVVM) ha ganado tracción, especialmente por su capacidad de realizar vinculación de datos (data binding) bidireccional, lo que reduce la necesidad de código explícito para sincronizar el estado de la UI con los datos subyacentes.

| Framework GUI      | Tecnología de Renderizado     | Licencia           | Fortalezas Principales                                           |
|-------------------|------------------------------|--------------------|------------------------------------------------------------------|
| Tkinter           | Native Wrappers (Tcl/Tk)     | PSF                | Estándar, ligero, curva de aprendizaje baja.                     |
| PyQt / PySide     | Native Wrappers (Qt/C++)     | Comercial / LGPL   | Profesional, widgets complejos, herramientas de diseño.          |
| Kivy              | OpenGL (Custom)              | MIT                | Multiplataforma (incluye móvil), táctil, lenguaje KV.            |
| CustomTkinter     | Tcl/Tk (Modernizado)         | MIT                | Apariencia moderna manteniendo la simplicidad de Tk.             |

**Componentes no visuales y arquitectura de servicios**

Los componentes no visuales se centran en la encapsulación de servicios de backend, motores de cálculo o capas de persistencia. Para que estos componentes sean verdaderamente modulares, deben diseñarse bajo principios de bajo acoplamiento y alta cohesión. Un patrón crítico en la creación de componentes no visuales en Python es la Inyección de Dependencias (DI). La DI permite que un componente reciba sus dependencias desde el exterior en lugar de instanciarlas internamente, lo que facilita enormemente la sustitución de implementaciones en tiempo de ejecución y la realización de pruebas unitarias mediante el uso de objetos simulados (mocks).

Además de la DI, los desarrolladores utilizan patrones de diseño de comportamiento y creación para estructurar sus componentes:
- Factory Method: Abstrae el proceso de creación de objetos, permitiendo al sistema trabajar con interfaces o clases base en lugar de implementaciones concretas, lo que desacopla al consumidor del creador.
- Strategy Pattern: Permite definir una familia de algoritmos y hacerlos intercambiables, lo que es ideal para componentes que deben soportar diferentes métodos de procesamiento de datos o protocolos de comunicación.
- Observer Pattern: Crucial para sistemas basados en eventos, donde un componente (el sujeto) mantiene una lista de dependientes (observadores) a los que notifica automáticamente sobre cambios de estado.

Un ejemplo avanzado de arquitectura de componentes no visuales es la Zope Component Architecture (ZCA). La ZCA se basa en la definición de interfaces explícitas mediante zope.interface, que actúan como contratos de comportamiento. En este ecosistema, los componentes se registran en un registro central y se recuperan no por su clase, sino por la interfaz que implementan. La ZCA distingue entre "Utilidades" (componentes que proporcionan una funcionalidad global) y "Adaptadores" (componentes que transforman un objeto con una interfaz determinada para que sea compatible con otra interfaz requerida). Este nivel de abstracción permite construir sistemas empresariales extremadamente flexibles donde las piezas de software pueden ser reemplazadas o extendidas sin modificar el código que las utiliza.

## 2.4 Creación y uso de paquetes/librerías definidas por el usuario
La culminación de la modularidad en Python es la capacidad de empaquetar y distribuir el código de manera que otros desarrolladores puedan consumirlo con facilidad. El proceso de empaquetado ha experimentado una transformación radical en los últimos años, alejándose de los scripts de instalación imperativos hacia un modelo declarativo estandarizado.

**Estructura y configuración moderna del paquete**

Un paquete de Python profesional debe seguir una estructura de directorios que facilite tanto el desarrollo como la distribución. La estructura recomendada por las autoridades de empaquetado (PyPA) suele incluir un directorio de código fuente (frecuentemente llamado src/), una carpeta de pruebas, y archivos de metadatos en la raíz del proyecto. El archivo central de esta nueva era es el pyproject.toml, que reemplaza o complementa al antiguo setup.py.

El archivo pyproject.toml organiza la información en tres tablas principales:
- [build-system]: Especifica las herramientas necesarias para construir el paquete (como setuptools, hatchling o flit) y el backend de construcción que se encargará del proceso.
- [project]: Contiene los metadatos estándar, como el nombre del paquete en PyPI, la versión, los autores, la descripción y, de manera crítica, las dependencias necesarias para que el paquete funcione.
- [tool]: Permite configurar herramientas de desarrollo adicionales como linters, formateadores de código o marcos de prueba.

| Atributo Metadatos | Propósito                                      | Ejemplo / Formato                          |
|--------------------|-----------------------------------------------|--------------------------------------------|
| name               | Identificador único en el registro de paquetes | mi-libreria-procesamiento                  |
| version            | Control de lanzamientos y compatibilidad       | 1.2.3 o dinámico de Git                    |
| dependencies       | Paquetes de terceros requeridos                | ["numpy>=1.20", "requests"]                |
| scripts            | Comandos de terminal expuestos al usuario      | mi-comando = "mi_paquete.cli:main"         |
| requires-python    | Versiones compatibles del intérprete           | >=3.8                                      |

La creación de un paquete no termina con el código; la inclusión de archivos de soporte como README.md (para la descripción larga en PyPI) y un archivo de LICENSE es imperativa para el uso en entornos profesionales y de código abierto. Una vez configurado, el paquete se compila en formatos de distribución, siendo los más comunes el Source Distribution (sdist) y el Built Distribution (Wheel). Los archivos Wheel son especialmente valorados porque contienen el código pre-compilado (especialmente relevante si hay extensiones en C), lo que acelera drásticamente la instalación para el usuario final.

**Ecosistema de herramientas de gestión de paquetes**

El panorama de herramientas para gestionar el ciclo de vida de un paquete ha madurado hacia un modelo de "flujo de trabajo integral". Atrás quedaron los días en que pip era la única herramienta; hoy, los desarrolladores eligen entre potentes gestores que unifican la creación de entornos virtuales, la resolución de dependencias y la publicación.

Poetry se ha consolidado como el estándar para muchos proyectos de librerías, gracias a su resolutor de dependencias inteligente que evita conflictos de versiones y su facilidad para publicar en PyPI con un solo comando. Por otro lado, uv, una herramienta extremadamente rápida escrita en Rust, ha irrumpido en el mercado en 2024-2025, ofreciendo velocidades de instalación y resolución de dependencias que superan por órdenes de magnitud a pip y poetry, convirtiéndose en la opción predilecta para entornos de integración continua (CI). Hatch y PDM también ofrecen alternativas robustas; Hatch se distingue por su excelente manejo de múltiples entornos de desarrollo y pruebas, mientras que PDM destaca por su estricto cumplimiento de los estándares PEP y su soporte para entornos sin carpetas virtuales tradicionales (venv-less).

La elección de estas herramientas afecta directamente la mantenibilidad del proyecto. Un buen gestor de paquetes genera un archivo de bloqueo (lockfile), como poetry.lock o pdm.lock, que registra las versiones exactas de cada dependencia y sub-dependencia utilizada durante el desarrollo. Este archivo garantiza que cualquier otro desarrollador o servidor de despliegue pueda recrear exactamente el mismo entorno de ejecución, eliminando el clásico problema de "en mi máquina funciona".

### Ejemplo práctico
```python
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
```
**1. El "Inventario" (Lista de Diccionarios)**
En lugar de escribir cada tarjeta a mano, el código utiliza una lista de Python llamada productos.

- Propósito: Almacenar la información técnica de cada artículo (ID, nombre, precio, descripción e imagen).
- Escalabilidad: Si mañana quieres agregar 100 productos más, solo los añades a esta lista y la interfaz se actualizará sola.

**2. Gestión de Estado y Feedback**
Dentro de main, se definen las listas que guardan la "memoria" de la sesión del usuario.

```Python
carrito = []
favoritos = []

# Referencias visuales para los contadores del header
carrito_text = ft.Text("0", size=14)
favoritos_text = ft.Text("0", size=14)
mostrar_mensaje: Utiliza un SnackBar (esa pequeña notificación que sale abajo) para avisar al usuario que un producto fue agregado.

agregar_carrito y agregar_favorito: Funciones que modifican las listas de memoria y actualizan el texto de los contadores en la pantalla.
```

**3. El Header (Barra de Navegación)**
Este bloque crea la parte superior de la tienda.

```Python
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
```

Layout: Usa un ft.Row con alignment="spaceBetween" para que el nombre de la tienda quede a la izquierda y los iconos a la derecha.

**4. Generación Dinámica de Tarjetas**

Este es el bloque más complejo. Itera sobre la lista de productos y crea un objeto ProductCard por cada uno.

```Python
for p in productos:
    card = ProductCard(p["nombre"], p["descripcion"], p["precio"], p["ruta_imagen"])
    
    # Asignación de funciones a los botones de la tarjeta
    card.agregar = lambda e, prod=p: agregar_carrito(prod)

    # Manejador de favoritos con lógica de cambio de icono (❤️/🤍)
    def make_fav_handler(prod, card_ref):
        # ... lógica para alternar favorito ...
```

- Inyección de lógica: El componente ProductCard (que viene de otro archivo) recibe las funciones agregar_carrito y agregar_favorito.
- Importante: Se usa un "handler" para que cada tarjeta sepa exactamente a qué producto se refiere cuando haces clic en ella.

**5. El Grid de Productos y Renderizado**

Finalmente, se organizan todas las tarjetas en una cuadrícula adaptable.

```Python
grid = ft.Row(
    controls=tarjetas,
    wrap=True, # Permite que las tarjetas pasen a la siguiente fila si no caben
    spacing=15,
    run_spacing=15
)
```
- wrap=True: Es fundamental. Convierte la fila en una "malla" o grid. Si reduces el tamaño de la ventana, las tarjetas se acomodarán hacia abajo automáticamente.
- assets_dir: Al final del código, se especifica dónde están guardadas las fotos de los productos para que Flet pueda encontrarlas.

**Visualizaciones**

Ejecición
<img width="1567" height="873" alt="image" src="https://github.com/user-attachments/assets/c6775f95-b26b-4fd9-ad25-ed8270b6abd6" />

Web
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3535c0c7-2f07-46dc-a122-d0d66821db0a" />
