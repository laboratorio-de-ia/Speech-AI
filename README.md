Acessar o diretório abaixo com toda a documentação do projeto

https://github.com/laboratorio-de-ia/Speech-AI/tree/main/docs/SpeechAI_Docs


                                    Speech AI Platform v1.0 Enterprise
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                          USER INPUT                                                        │
│                                                                                                            │
│                         script.txt / PowerPoint / Future PDF / DOCX                                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                   │
                                                   ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                        PIPELINE LAYER                                                     │
│                                                                                                            │
│  Text Analyzer ─────► Presentation ─────► Narration Builder ─────► Speech Builder                         │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                   │
                                                   ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                  SPEECH INTELLIGENCE LAYER                                                │
│                                                                                                            │
│  Language Detector                                                                   │                    │
│          │                                                                           │                    │
│          ▼                                                                           │                    │
│  Voice Selector                                                                      │                    │
│          │                                                                           │                    │
│          ▼                                                                           │                    │
│  Speech Analyzer                                                                     │                    │
│          │                                                                           │                    │
│          ▼                                                                           │                    │
│  Timing Calculator                                                                   │                    │
│          │                                                                           │                    │
│          ▼                                                                           │                    │
│  Speech Optimizer                                                                    │                    │
│          │                                                                           │                    │
│          └──────────────► Speech Intelligence Engine ───────────────► SpeechProfile │                    │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                   │
                                                   ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                      SPEECH SERVICE                                                       │
│                                                                                                            │
│                           Speech Service                                                                   │
│                                   │                                                                        │
│                                   ▼                                                                        │
│                            Provider Factory                                                                │
│                                   │                                                                        │
│                                   ▼                                                                        │
│                              TTSEngine                                                                     │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                   │
                                                   ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                     PROVIDERS                                                             │
│                                                                                                            │
│       Edge Provider       Azure Provider (Future)       ElevenLabs (Future)       OpenAI (Future)         │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                   │
                                                   ▼
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                            OUTPUT                                                         │
│                                                                                                            │
│                            narration.txt   speech.txt   audio.mp3                                          │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

| Camada             | Responsabilidade                 |
| ------------------ | -------------------------------- |
| Input Layer        | Entrada de arquivos              |
| Pipeline Layer     | Conversão do conteúdo em domínio |
| Intelligence Layer | Inteligência da narração         |
| Service Layer      | Orquestração da síntese          |
| Provider Layer     | Motores de TTS                   |
| Output Layer       | Geração dos artefatos finais     |

Avaliação da arquitetura atual

A plataforma atingiu um nível de maturidade significativo:

Arquitetura em camadas, separando pipeline, inteligência, serviços e provedores.
Objetos de domínio enriquecidos, reduzindo lógica espalhada pela aplicação.
Baixo acoplamento, permitindo evoluir a inteligência sem impactar a síntese.
Preparação para múltiplos provedores TTS e futuras integrações.
Base pronta para SSML avançado, múltiplos narradores, emoções e IA na Sprint 9.

Esses dois entregáveis representam fielmente o estado atual do SpeechAI e podem servir como base para a documentação oficial do projeto antes de iniciarmos a Sprint 8.6.5.


Foundation
     │
     ▼
Configuration
     │
     ▼
Text Processing
     │
     ▼
Domain Models
     │
     ▼
Narration Pipeline
     │
     ▼
Speech Pipeline
     │
     ▼
Dependency Injection
     │
     ▼
Provider Architecture
     │
     ▼
Voice Intelligence
     │
     ▼
Speech Intelligence Engine
     │
     ▼
Project Cleanup
     │
     ▼
Sprint 9 (IA Avançada)

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                            SPEECH AI PLATFORM v1.0 ENTERPRISE                                                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

                                          ┌───────────────────────────────┐
                                          │         INPUT LAYER           │
                                          │───────────────────────────────│
                                          │ script.txt                    │
                                          │ PowerPoint (.pptx)            │
                                          │ PDF (Sprint 9)                │
                                          │ Word (Sprint 9)               │
                                          └───────────────┬───────────────┘
                                                          │
                                                          ▼

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                PIPELINE LAYER                                                                        │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                    │
│  TextAnalyzer                                                                                                                     │
│       │                                                                                                                           │
│       ▼                                                                                                                           │
│  Presentation                                                                                                                     │
│       │                                                                                                                           │
│       ├──────────────────────────────┐                                                                                             │
│       ▼                              ▼                                                                                             │
│ NarrationBuilder               SpeechBuilder                                                                                       │
│       │                              │                                                                                             │
│       └──────────────┬───────────────┘                                                                                             │
│                      ▼                                                                                                             │
│              narration.txt / speech.txt                                                                                            │
│                                                                                                                                    │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                          │
                                                          ▼

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                         SPEECH INTELLIGENCE LAYER                                                                  │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                    │
│ Presentation                                                                                                                      │
│      │                                                                                                                            │
│      ▼                                                                                                                            │
│ LanguageDetector                                                                                                                  │
│      │                                                                                                                            │
│      ▼                                                                                                                            │
│ VoiceSelector                                                                                                                     │
│      │                                                                                                                            │
│      ▼                                                                                                                            │
│ SpeechAnalyzer                                                                                                                    │
│      │                                                                                                                            │
│      ▼                                                                                                                            │
│ TimingCalculator                                                                                                                  │
│      │                                                                                                                            │
│      ▼                                                                                                                            │
│ SpeechOptimizer                                                                                                                   │
│      │                                                                                                                            │
│      ▼                                                                                                                            │
│ SpeechIntelligenceEngine                                                                                                          │
│      │                                                                                                                            │
│      ▼                                                                                                                            │
│ SpeechProfile                                                                                                                     │
│                                                                                                                                    │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                          │
                                                          ▼

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                 SERVICE LAYER                                                                      │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                    │
│ SpeechService                                                                                                                     │
│       │                                                                                                                           │
│       ▼                                                                                                                           │
│ ProviderFactory                                                                                                                   │
│       │                                                                                                                           │
│       ▼                                                                                                                           │
│ TTSEngine                                                                                                                         │
│                                                                                                                                    │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                          │
                                                          ▼

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                PROVIDER LAYER                                                                      │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                    │
│ ProviderRegistry                                                                                                                  │
│       │                                                                                                                           │
│       ├───────────── Edge Provider                                                                                                 │
│       ├───────────── Azure Provider (Roadmap)                                                                                      │
│       ├───────────── OpenAI TTS (Roadmap)                                                                                          │
│       ├───────────── ElevenLabs (Roadmap)                                                                                          │
│       └───────────── Amazon Polly (Roadmap)                                                                                         │
│                                                                                                                                    │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
                                                          │
                                                          ▼

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                 OUTPUT LAYER                                                                       │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                                                    │
│ narration.txt                                                                                                                     │
│ speech.txt                                                                                                                        │
│ audio.mp3                                                                                                                         │
│ logs                                                                                                                              │
│ metrics (Sprint 9)                                                                                                                │
│                                                                                                                                    │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

