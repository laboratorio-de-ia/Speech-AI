# 🎙️ Speech AI Pipeline

> A modular Text-to-Speech (TTS) pipeline that converts presentation
> scripts into natural English audio using Microsoft Edge TTS.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

------------------------------------------------------------------------

# Overview

Speech AI Pipeline automates the complete process of transforming
structured presentation text into professional narration.

The project is organized into independent modules, making it easy to
maintain and extend.

------------------------------------------------------------------------

# Features

-   Presentation text analysis
-   Narration optimization
-   Natural speech generation
-   Microsoft Edge TTS integration
-   MP3 audio generation
-   Modular architecture
-   Git version control

------------------------------------------------------------------------

# Architecture

``` text
Input Script
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
Audio MP3
```

------------------------------------------------------------------------

# Project Structure

``` text
SpeechAI/
│
├── core/
│   ├── text_analyzer.py
│   ├── narration_builder.py
│   ├── ssml_builder.py
│   └── tts_engine.py
│
├── models/
│   └── presentation.py
│
├── output/
├── logs/
├── main.py
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

# Requirements

-   Python 3.11 or newer
-   FFmpeg (optional)
-   Microsoft Edge TTS

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# Running

``` bash
python main.py
```

Generated files are written to the **output** directory.

------------------------------------------------------------------------

# Voice Configuration

Default voice:

-   `en-US-GuyNeural`

Output file:

``` text
output/Audio_Governance_SouthAmerica.mp3
```

------------------------------------------------------------------------

# Typical Workflow

1.  Read the presentation text.
2.  Analyze slides and sections.
3.  Build narration.
4.  Optimize speech flow.
5.  Generate MP3 audio.

------------------------------------------------------------------------

# Roadmap

-   FastAPI API
-   Docker support
-   Web interface
-   Multi-language support
-   Azure Speech integration
-   Multiple voices
-   Automatic pronunciation dictionary

------------------------------------------------------------------------

# Contributing

1.  Fork the repository.
2.  Create a feature branch.
3.  Commit your changes.
4.  Open a Pull Request.

------------------------------------------------------------------------

# License

MIT License.

------------------------------------------------------------------------

# Author

**Rodrigo Magalhães**

AI Engineering • Cloud • Automation • Speech Systems

Obrigado Senhor


                           +----------------------+
                           |    SpeechAIApp       |
                           +----------+-----------+
                                      |
                                      v
                           +----------------------+
                           |     TTSEngine        |
                           +----------+-----------+
                                      |
                                      v
                           +----------------------+
                           |   ProviderFactory    |
                           +----------+-----------+
                                      |
                +---------------------+----------------------+
                |                                            |
                v                                            v
      +----------------------+                 +----------------------+
      |    EdgeProvider      |                 |   AzureProvider      |
      +----------+-----------+                 +----------+-----------+
                 |                                         |
                 +-------------------+---------------------+
                                     |
                                     v
                          +------------------------+
                          |   Provider Metadata    |
                          +------------------------+


                                              +------------------+
                    |   TTSEngine      |
                    +--------+---------+
                             |
                             ▼
                    +------------------+
                    | ProviderFactory  |
                    +--------+---------+
                             |
                             ▼
                    +------------------+
                    | ProviderRegistry |
                    +--------+---------+
                             |
        ┌────────────────────┼────────────────────┐
        ▼                    ▼                    ▼
  EdgeProvider        AzureProvider       OpenAIProvider