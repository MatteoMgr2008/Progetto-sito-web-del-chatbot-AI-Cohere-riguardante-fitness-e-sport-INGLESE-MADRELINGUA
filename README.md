# Sito web del chatbot AI Cohere su fitness e sport

🇮🇹 [Italiano](#-italiano) | 🇬🇧 [English](#-english)

---

## 🇮🇹 Italiano

### 📌 Descrizione
Progetto realizzato per la materia di **Inglese (madrelingua)**: un piccolo sito web con un assistente vocale basato sull'AI di **Cohere**, specializzato in **salute, sport, fitness, alimentazione e benessere**.

L'utente registra la propria domanda a voce (in inglese), la pagina la trascrive in testo, il server Flask la invia a Cohere e restituisce la risposta sia **come testo** sia **come audio** letto ad alta voce (generato con gTTS). L'interfaccia è interamente in inglese.

### ⚙️ Come funziona
- **Registrazione vocale:** i pulsanti *Start recording* / *End recording* usano la Web Speech API del browser (`SpeechRecognition`, lingua `en-US`) per trascrivere la domanda.
- **Generazione della risposta:** il pulsante *Generate the response* invia il testo alla route `/generatore_risposta_e_audio_AI`, che aggiunge un prompt di sistema (rispondere solo su salute, esercizio, dieta, nutrizione e benessere) e chiama `cohere.Client.generate` con `max_tokens=500` e `temperature=0.5`.
- **Risposta audio:** il testo generato viene convertito in voce inglese con **gTTS**, salvato in `static/output.mp3` e riprodotto automaticamente nella pagina.
- **Stop replying:** un pulsante permette di interrompere l'audio in qualsiasi momento.

### 📁 Contenuto
| File / cartella | Descrizione |
|---|---|
| `app.py` | Server Flask: pagina principale, chiamata a Cohere, generazione dell'audio con gTTS e servizio dei file statici |
| `requirements.txt` | Dipendenze Python (`cohere`, `flask`, `gTTS`) |
| `templates/index.html` | Pagina web con il form, i pulsanti e lo script JavaScript per riconoscimento vocale, invio della richiesta e riproduzione dell'audio |
| `static/style.css` | Stili grafici della pagina (usa il font Inter, caricato da Google Fonts in `index.html`) |
| `static/script.js` | Piccolo script che riporta la pagina in cima quando viene ricaricata |
| `static/output.mp3` | File audio dell'ultima risposta generata (viene sovrascritto a ogni richiesta) |
| `static/images/favicon.ico` | Icona del sito |
| `.gitignore` | File e cartelle esclusi dal repository |

### 🛠️ Tecnologie utilizzate
- **Python** con **Flask**
- **Cohere** (libreria Python `cohere`) per la generazione del testo
- **gTTS** (Google Text-to-Speech) per la sintesi vocale
- **HTML**, **CSS** e **JavaScript** (Web Speech API, `fetch`)

### ▶️ Come avviarlo
1. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```
2. Inserisci la **tua** API key di Cohere nella riga di `app.py` dove viene creato `cohere.Client(...)`.
3. Avvia il server:
   ```bash
   python app.py
   ```
4. Apri nel browser l'indirizzo mostrato dal terminale (di default `http://127.0.0.1:5000`).

### 📋 Requisiti
- Python 3 e connessione a Internet (servono sia per Cohere sia per gTTS)
- Un'API key di Cohere
- Un browser che supporti il riconoscimento vocale (`SpeechRecognition` / `webkitSpeechRecognition`, ad esempio Chrome) e un microfono

### 👤 Autore
[MatteoMgr2008](https://github.com/MatteoMgr2008)

---

## 🇬🇧 English

### 📌 Description
Project made for the **English (native-speaker teacher)** school subject: a small website with a voice assistant powered by **Cohere** AI, specialised in **health, sports, fitness, nutrition and wellness**.

The user records a question by voice (in English), the page transcribes it into text, the Flask server sends it to Cohere and returns the answer both **as text** and **as audio** read aloud (generated with gTTS). The whole interface is in English.

### ⚙️ How it works
- **Voice recording:** the *Start recording* / *End recording* buttons use the browser's Web Speech API (`SpeechRecognition`, language `en-US`) to transcribe the question.
- **Answer generation:** the *Generate the response* button sends the text to the `/generatore_risposta_e_audio_AI` route, which prepends a system prompt (only answer about health, exercise, diet, nutrition and wellness) and calls `cohere.Client.generate` with `max_tokens=500` and `temperature=0.5`.
- **Audio answer:** the generated text is converted to English speech with **gTTS**, saved to `static/output.mp3` and played automatically in the page.
- **Stop replying:** a button lets you stop the audio at any time.

### 📁 Contents
| File / folder | Description |
|---|---|
| `app.py` | Flask server: main page, Cohere call, audio generation with gTTS and static file serving |
| `requirements.txt` | Python dependencies (`cohere`, `flask`, `gTTS`) |
| `templates/index.html` | Web page with the form, buttons and the JavaScript for speech recognition, sending the request and playing the audio |
| `static/style.css` | Page styling (uses the Inter font, loaded from Google Fonts in `index.html`) |
| `static/script.js` | Small script that scrolls the page back to the top when it is reloaded |
| `static/output.mp3` | Audio file of the last generated answer (overwritten on every request) |
| `static/images/favicon.ico` | Site icon |
| `.gitignore` | Files and folders excluded from the repository |

### 🛠️ Technologies used
- **Python** with **Flask**
- **Cohere** (`cohere` Python library) for text generation
- **gTTS** (Google Text-to-Speech) for speech synthesis
- **HTML**, **CSS** and **JavaScript** (Web Speech API, `fetch`)

### ▶️ How to run it
1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Put **your own** Cohere API key in the line of `app.py` where `cohere.Client(...)` is created.
3. Start the server:
   ```bash
   python app.py
   ```
4. Open the address shown in the terminal in your browser (by default `http://127.0.0.1:5000`).

### 📋 Requirements
- Python 3 and an Internet connection (needed for both Cohere and gTTS)
- A Cohere API key
- A browser that supports speech recognition (`SpeechRecognition` / `webkitSpeechRecognition`, e.g. Chrome) and a microphone

### 👤 Author
[MatteoMgr2008](https://github.com/MatteoMgr2008)
