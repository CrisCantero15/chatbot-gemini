# Proyecto Chatbot Web con Flask

Este proyecto es un chatbot web que combina un frontend estático con un backend en Flask que se comunica con un modelo de IA en la nube (Google Gemini).

---

## Estructura del proyecto

```bash
mi_proyecto/
├─ index.html # Página principal
├─ /css/ # Archivos CSS
│ └─ index.css
├─ /js/ # Archivos JS
│ └─ index.js
├─ /backend/ # Código de la API Flask
│ └─ app.py
├─ /env/ # Entorno virtual con dependencias Python
├─ .env # Variables de entorno (API keys)
```

---

## Requisitos

- Python 3.10+
- Entorno virtual (`env`) con las siguientes dependencias:
  
```bash
pip install flask python-dotenv
```

Para esto, también puedes reconstruir el entorno con:

```bash
pip install -r requirements.txt
```

- Una API key de Gemini (u otra API de tu modelo) definida en el archivo .env:

```bash
GEMINI_API_KEY=tu_api_key_aquí
```

---

## Cómo ejecutar el proyecto

1. Abre la terminal o consola.
2. Navega a la raíz del proyecto:

```bash
cd /ruta-absoluta/mi-proyecto
```

3. Activa el entorno virtual:

```bash
env\Scripts\activate
```

O en macOS / Linux:

```bash
source env/bin/activate
```

4. Ejecuta la aplicación Flask:

```bash
python backend/app.py
```

5. Abre el navegador y visita:

```bash
http://127.0.0.1:5000/
http://localhost:5000/
```

* Esto abrirá la página principal (index.html).
* Los archivos /css y /js se cargarán automáticamente.
* La API /api/chat estará disponible para que el frontend haga peticiones al modelo de IA.

---

# Notas importantes

Flask solo sirve rutas que hayas definido. Por ejemplo:

* / → index.html
* /api/chat → endpoint dinámico que devuelve JSON

Cualquier ruta no definida devuelve error 404. Además, el frontend no debe contener API keys; el backend se encarga de hacer llamadas seguras a la API externa.

---

# Uso del chatbot

1. Escribe un mensaje en el frontend y haz click en “Enviar”.
2. El frontend hace un POST a /api/chat.
3. Flask procesa la petición, llama al modelo de IA y devuelve la respuesta que se muestra en la web.

---

# Contacto

* Autor: Cristian Cantero López.
* Curso / Asignatura: Máster FP en Inteligencia Artificial y Big Data / Programación de Inteligencia Artificial.
* Fecha de entrega: 11/11/2025.