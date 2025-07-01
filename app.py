from flask import Flask, request, jsonify, send_from_directory, render_template  # Aggiunto jsonify
from gtts import gTTS
import cohere
import os

app = Flask(__name__)

# Route per visualizzare il file HTML principale
@app.route("/")
def index():
    return render_template("index.html")

# Route per generare la risposta e l'audio della risposta dell'AI
@app.route("/generatore_risposta_e_audio_AI", methods=["POST"])
def generatore_risposta_e_audio_AI():
    # Inizializzazione della AI attraverso la dichiarazione dell'API key di Cohere
    API_key_Cohere = cohere.Client("j9Y3mng1QTbej4MsdOUWmdRunnfByC3AtlBp8frA") 
    input_testo_AI = request.form["prompt_utente"] # La variabile acquisisce il valore di tipo stringa dall'apposito campo di testo del file HTML 
    prompt_generico = f"You are an AI assistant specializing in health, sports, and fitness. Only answer questions related to these topics: health, exercise, diet, nutrition, and wellness. {input_testo_AI}"
    # Settaggio delle impostazioni della AI
    risposta_input_testo = API_key_Cohere.generate(
        prompt=prompt_generico, # Specificazione della variabile da cui prendere il prompt
        max_tokens=500, # Numero massimo di token utilizzabili a ogni risposta da parte dell'AI
        temperature=0.5 # Livello di creatività/precisione di una risposta con massimo di 1 (0.5 è una via di mezzo tra creatività e precisione della risposta data)
    )
    testo_finale_AI = risposta_input_testo.generations[0].text
    print()
    print("USER QUESTION TEXT:")
    print(input_testo_AI)
    print()
    print("AI RESPONSE TEXT:")
    print(testo_finale_AI)

    # Utilizzo della libreria gTTS di Google per convertire il testo in audio parlato
    audio_testo_finale_AI = gTTS(text=testo_finale_AI, lang="en", slow=False) # Settaggio delle preferenze di voce
    posizione_audio_testo_finale_AI = "static/output.mp3" # Posizione in cui viene salvato il file audio generato
    
    # Salvataggio dell'audio in un file "mp3"
    audio_testo_finale_AI.save(posizione_audio_testo_finale_AI)
    
    # Restituzione di un file JSON contenente il testo generato e l'audio generato
    return jsonify({"testo": testo_finale_AI, "audio_url": f"/{posizione_audio_testo_finale_AI}"})

# Route per ricavare il file audio statico
@app.route("/static/<path:filename>", methods=["GET"])
def file_static(filename):
    return send_from_directory("static", filename) # Invia il file richiesto dalla directory "static"

if __name__ == '__main__':
    app.run(debug=True)