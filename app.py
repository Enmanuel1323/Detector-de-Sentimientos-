from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
from googletrans import Translator
import random

app = Flask(__name__)

# Consejos
consejos_positivos = [
        "Mantén una actitud positiva y sigue adelante.",
        "Disfruta de los pequeños momentos de felicidad.",
        "Comparte tu alegría con los demás.",
        "Haz algo que te apasione hoy.",
        "Sonríe y disfruta de tu día.",
        "Practica la gratitud diariamente.",
        "Rodéate de personas que te apoyen.",
        "Encuentra tiempo para tus hobbies.",
        "Mantén una perspectiva optimista.",
        "Visualiza tus metas y trabaja hacia ellas.",
        "Celebra tus logros, por pequeños que sean.",
        "Haz ejercicio regularmente para mejorar tu ánimo.",
        "Escucha música que te haga feliz.",
        "Dedica tiempo a la meditación o el mindfulness.",
        "Realiza actos de bondad al azar.",
        "Haz algo creativo que disfrutes.",
        "Sal a caminar y disfruta de la naturaleza.",
        "Mantén un diario de gratitud.",
        "Participa en actividades que te apasionen.",
        "Ríe a menudo y de todo corazón."
]

consejos_negativos = [
        "Recuerda que después de la tormenta siempre llega la calma.",
        "Habla con un amigo cercano sobre tus sentimientos.",
        "Tómate un tiempo para relajarte y descansar.",
        "Haz una lista de cosas por las que estás agradecido.",
        "Encuentra una actividad que te relaje.",
        "Practica la respiración profunda para reducir el estrés.",
        "Escribe tus sentimientos en un diario.",
        "Tómate un descanso de las redes sociales.",
        "Haz algo que disfrutes para distraerte.",
        "Busca ayuda profesional si lo necesitas.",
        "Practica el autocuidado con una rutina que te guste.",
        "Haz ejercicio para liberar endorfinas.",
        "Escucha música que te tranquilice.",
        "Tómate un tiempo para ti mismo.",
        "Rodéate de personas que te apoyen.",
        "Evita tomar decisiones importantes en momentos de estrés.",
        "Medita para encontrar paz interior.",
        "Mantén una rutina diaria estable.",
        "Duerme lo suficiente para mejorar tu estado de ánimo.",
        "Encuentra un hobby que te apasione."
]

consejos_neutrales = [
        "Es un buen momento para reflexionar y meditar.",
        "Disfruta de tu estabilidad emocional.",
        "Aprovecha para hacer algo productivo.",
        "Dedica tiempo a tus hobbies.",
        "Mantén un equilibrio en tus actividades diarias.",
        "Establece metas y trabaja hacia ellas.",
        "Practica la gratitud y aprecia las cosas buenas en tu vida.",
        "Rodéate de personas que te inspiren.",
        "Haz ejercicio regularmente para mantener tu bienestar.",
        "Encuentra tiempo para relajarte y descansar.",
        "Aprende algo nuevo cada día.",
        "Dedica tiempo a la meditación o el mindfulness.",
        "Participa en actividades que te apasionen.",
        "Sal a caminar y disfruta de la naturaleza.",
        "Mantén un diario de reflexiones.",
        "Organiza tu espacio de trabajo o estudio.",
        "Lee un libro que te interese.",
        "Dedica tiempo a la creatividad.",
        "Escucha música que te inspire.",
        "Tómate un momento para desconectar y recargar energías."
]

# Inicializa el traductor
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consejos')
def consejos_page():
    return render_template('consejos.html')

def detectar_sentimiento(texto):
    # Traduce el texto al inglés
    try:
        texto_ingles = translator.translate(texto, dest='en').text
    except Exception as e:
        print(f"Error en la traducción: {e}")
        texto_ingles = texto

    # Detecta el sentimiento usando TextBlob
    blob = TextBlob(texto_ingles)
    sentimiento = blob.sentiment.polarity

    if sentimiento > 0:
        sentimiento_label = "positive"
        consejos = random.sample(consejos_positivos, 5)
    elif sentimiento < 0:
        sentimiento_label = "negative"
        consejos = random.sample(consejos_negativos, 5)
    else:
        sentimiento_label = "neutral"
        consejos = random.sample(consejos_neutrales, 5)

    return sentimiento_label, consejos

@app.route('/detectar', methods=['POST'])
def emotion():
    data = request.get_json()
    texto = data.get('texto')
    sentimiento_label, consejo = detectar_sentimiento(texto)
    return jsonify({'sentimiento': sentimiento_label, 'consejos': consejo})

if __name__ == '__main__':
    app.run(debug=True)
