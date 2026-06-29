# 🎙️ Speech AI Pipeline

A professional **Text-to-Speech (TTS)** pipeline that converts
structured presentation content into natural-sounding audio narration
using **Microsoft Edge TTS**.

## 🚀 Features

-   Slide-based content processing
-   Speech optimization for natural narration
-   Microsoft Edge TTS integration
-   MP3 audio generation
-   Modular architecture
-   Easy to extend

## 🏗️ Architecture

``` text
Text Input
    │
    ▼
Text Analyzer
    │
    ▼
Narration Builder
    │
    ▼
Speech Optimizer
    │
    ▼
Edge TTS Engine
    │
    ▼
MP3 Audio
```

## 📁 Project Structure

``` text
SpeechAI/
├── core/
│   ├── text_analyzer.py
│   ├── narration_builder.py
│   ├── ssml_builder.py
│   └── tts_engine.py
├── models/
│   └── presentation.py
├── output/
├── logs/
├── main.py
├── requirements.txt
└── README.md
```

## ⚙️ Requirements

-   Python 3.11+
-   edge-tts

Install dependencies:

``` bash
pip install -r requirements.txt
```

## ▶️ Running

``` bash
python main.py
```

The generated files are saved in the `output/` directory.

## 🎤 Default Voice

-   Voice: `en-US-GuyNeural`
-   Optimized for professional English narration.

## 📦 Output

Typical generated files:

-   `output/narration.txt`
-   `output/speech.xml`
-   `output/Audio_Governance_SouthAmerica.mp3`

## 🛣️ Roadmap

-   FastAPI REST API
-   Docker support
-   Web interface
-   Multiple voices
-   Azure Speech integration
-   Automatic speech optimization

## 👤 Author

**Rodrigo Magalhães**

AI Engineering • Cloud • Automation • Speech Systems

## 📄 License

This project is intended for educational and professional purposes.
