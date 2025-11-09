# Proyecto 2: Aplicación que se Conecta a la API de Google Gemini en la Nube
# Descripción:
# Este proyecto consiste en una aplicación sencilla (por ejemplo, un script en Python o una API Flask) que envía un texto a la API de Google Gemini en la nube y muestra la respuesta. Se utiliza HTTPS y autenticación mediante token. El flujo es:
# 1. El usuario introduce un texto (por consola o mediante una interfaz web).
# 2. La aplicación envía el texto al endpoint de Google Gemini.
# 3. Se recibe la respuesta en formato JSON, que se procesa y muestra al usuario.

import os
from flask import Flask, request, jsonify, send_from_directory
from google import genai
from google.genai import types
from dotenv import load_dotenv

os.system("cls" if os.name == "nt" else "clear")
app = Flask(__name__, static_url_path="", static_folder="..")

# API Key utilizada para Gemini
load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("La variable de entorno GEMINI_API_KEY no está configurada.")

@app.route("/", methods=["GET"])
def home():
    """ Endpoint root que sirve el contenido de la home de la aplicación """
    
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    """ Endpoint que se encarga de realizar una petición POST a la API de Gemini """

    # Establecer conexión con la API de Gemini
    client = genai.Client(api_key=API_KEY)
    MODEL = "gemini-2.5-pro"
    
    # Obtener mensaje del usuario
    data = request.get_json(silent=True)
    
    if not data:
        return jsonify({ "error": "JSON inválido o faltante." }), 400
    
    message = data.get("prompt")

    if not message:
        return jsonify({"error": "Falta el campo 'prompt'."}), 400
    
    # Se genera el payload con el prompt que se va a mandar a la API
    payload = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=message),
            ],
        ),
    ]

    # Configurar la petición
    generate_content_config = types.GenerateContentConfig(
        temperature=0.7, # 0.7 de temperatura para que no alucine en exceso
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1, # Presupuesto de "pensamiento" ilimitado
        ),
        image_config=types.ImageConfig(
            image_size="1K", # Si el modelo genera una imagen, será de 1024x1024 píxeles
        ),
    )

    try:
        # Se realiza la petición a Gemini
        response = client.models.generate_content(
            model=MODEL,
            contents=payload,
            config=generate_content_config
        )
        return jsonify({ "message": response.text or "Sin respuesta generada." })
    except Exception as e:
        return jsonify({ "error": f"Error al realizar la petición a la API de Gemini: {e}" }), 500

if __name__ == "__main__":
    app.run(debug=True)