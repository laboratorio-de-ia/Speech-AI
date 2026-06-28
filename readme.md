# 🎙️ Speech AI Pipeline

A professional Text-to-Speech (TTS) pipeline that converts structured presentation content into natural-sounding audio narration using Microsoft Edge TTS.

The system transforms slide-based content into speech-optimized text and generates high-quality audio narrations with natural pacing, pauses, and voice control.

---

## 🚀 Features

- 📑 Slide-based text processing
- 🧠 Intelligent speech optimization (pause simulation)
- 🎙️ Natural male English voice (US Neural)
- ⚡ Fast text-to-audio generation
- 📦 Modular pipeline architecture
- 🔁 Fully reproducible outputs
- 💾 Export to MP3 audio files
- 🧩 Clean separation of concerns (Analyzer → Builder → TTS)

---

## 🏗️ Architecture
Text Input
↓
Text Analyzer
↓
Narration Builder
↓
Speech Text Optimizer
↓
Edge TTS Engine
↓
MP3 Output


---

## 📁 Project Structure

SpeechAI/
│
├── core/
│ ├── text_analyzer.py
│ ├── narration_builder.py
│ ├── ssml_builder.py
│ └── tts_engine.py
│
├── models/
│ └── presentation.py
│
├── output/
│ ├── narration.txt
│ ├── speech.xml
│ └── Audio_Governance_SouthAmerica.mp3
│
├── main.py
├── requirements.txt
└── README.md


---

## ⚙️ How It Works

### 1. Text Analysis
Breaks presentation content into structured slides and sentences.

### 2. Narration Builder
Converts structured content into clean narration text.

### 3. Speech Optimization
Applies natural speech flow:
- pauses using "..."
- sentence segmentation
- rhythm control

### 4. Audio Generation
Uses Microsoft Edge TTS to generate final MP3 audio.

---

## 🎧 Voice Configuration

- Voice: `en-US-GuyNeural`
- Rate: `-20%`
- Style: Professional narration

---

## ▶️ How to Run

### Clone repository
```bash
git clone git@github.com:rjmagalhaes/Texto_Audio.git
cd Texto_Audio

pip install -r requirements.txt

python main.py

📊 Output Example
Slides: 6
Narration Blocks: 6
Words: 974
Estimated Duration: 6.72 min

🎯 Use Cases
Corporate presentations
Training content
AI narration systems
Accessibility audio generation
Educational material
🧠 Design Decisions
Edge TTS for simplicity and speed
Speech-optimized text instead of SSML
Modular architecture for scaling
🚀 Roadmap
FastAPI service layer
Web UI for text-to-audio
Docker support
Multi-voice system
Emotion-based narration
👤 Author

Rodrigo Magalhães
AI Engineering | Cloud | Automation | Speech Systems

📜 License

Educational and professional use.


---

# 🔥 O QUE FOI CORRIGIDO

✔ removido todos os `id="..."` (isso quebrava o Markdown)  
✔ corrigidos blocos ``` aninhados  
✔ removido nesting inválido  
✔ compatível 100% com GitHub renderer  
✔ layout limpo e profissional  

---

# 🧠 POR QUE ESTAVA QUEBRANDO

GitHub quebra quando vê:

- blocos ``` dentro de outros sem separação
- atributos HTML dentro de markdown (`id="..."`)
- nesting de código mal fechado

---

# 🚀 PRÓXIMO PASSO (se quiser evoluir)

Agora seu README já está correto.

Podemos seguir para:

## 🔥 1. requirements.txt profissional
## 🔥 2. Dockerfile
## 🔥 3. FastAPI (API de geração de áudio)
## 🔥 4. UI web tipo “ElevenLabs clone”

Só me fala 👍