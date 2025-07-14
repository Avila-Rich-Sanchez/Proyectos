⚽ SuperKickFinder – Explorador de Conexiones entre Jugadores

**SuperKickFinder** es una aplicación deportiva escrita en Python que permite al usuario descubrir si un jugador ha compartido equipo con otros jugadores seleccionados(No terminada, con la ultima version se creo la funcion de extraer datos como los clubes de los jugadores, falta la busquedas de plantillas de temporadas exactas y las coincidencias de los jugadores). La app evoluciona a lo largo de cinco versiones, cada una agregando nuevas funcionalidades, mejoras de rendimiento y mejores prácticas de programación.

Este proyecto demuestra cómo una idea puede crecer desde una lógica local hasta convertirse en una herramienta asincrónica capaz de consultar datos reales desde una API externa. Ideal para practicar consumo de APIs, manejo de datos, asincronía y diseño modular.

---

🚀 Características principales

- Búsqueda de coincidencias entre jugadores por clubes compartidos
- Versiones incrementales del proyecto con mejoras visibles
- Integración con la API-Football mediante requests y aiohttp
- Lógica basada en datos simulados (JSON) para versión offline
- Código optimizado, estructurado y fácil de escalar

---

🧠 Evolución del proyecto

| Versión | Archivo | Tecnología | Mejora clave |
|--------|---------|------------|--------------|
| v1     | `v1_datos_locales.py` | JSON local | Lógica inicial con datos simulados |
| v2     | `v2_requests_basico.py` | requests | Primeras llamadas GET a API |
| v3     | `v3_requests_mejorado.py` | requests | Búsqueda más profunda y detallada |
| v4     | `v4_optimizacion_sintaxis.py` | requests | Refactor para mayor claridad y eficiencia |
| v5     | `v5_async_aiohttp.py` | asyncio + aiohttp | Velocidad, asincronía y mejor rendimiento |

---

📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Avila-Rich-Sanchez/superkickfinder.git
cd superkickfinder
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

> Asegúrate de tener Python 3.10 o superior

---

▶️ Uso

Cada versión funciona de forma independiente. Puedes ejecutar cualquiera de ellas:

```bash
python versiones/v1_datos_locales.py
```

O probar la versión más avanzada:

```bash
python versiones/v5_async_aiohttp.py
```

---

📁 Estructura del repositorio

```text
superkickfinder/
├── README.md
├── versiones/
  ├── v1_datos_locales.py
  ├── v2_requests_basico.py
  ├── v3_requests_mejorado.py
  ├── v4_optimizacion_sintaxis.py
  └── v5_async_aiohttp.py
```

---

🛠 Dependencias

- `requests`
- `aiohttp`
- `asyncio`

> Añade otras según evoluciones futuras (por ejemplo, `tkinter`, `pandas`, `PyQt`, etc.)

---

🌐 Fuente de datos

- API utilizada: [API-Football](https://www.api-football.com/)

---

🌟 Próximos pasos

- Encontrar el jugador que haya jugado con 5 jugadores aleatorios
- Añadir una interfaz grafica usando tkinter o PyQt

---

🤝 Contribuciones

¿Quieres ayudar a mejorar el proyecto? ¡Tu aporte es bienvenido!

1. Haz un fork del repositorio
2. Crea una nueva rama
3. Realiza tus cambios
4. Envía un Pull Request

También puedes abrir un issue para sugerencias o reportar errores.

---

📄 Licencia

Este proyecto se encuentra bajo la [Licencia MIT](LICENSE). Puedes modificarlo, usarlo y compartirlo libremente.

---

👤 Autor

**Ricardo Avila**

¿Te gustó el proyecto? ¡Dale una estrella ⭐ y compártelo con la comunidad!

