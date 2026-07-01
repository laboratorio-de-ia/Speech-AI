                Script.txt
                     │
                     ▼
            Language Detection Service
                     │
      ┌──────────────┼───────────────┐
      ▼              ▼               ▼
   English       Portuguese      Spanish
      │              │               │
      ▼              ▼               ▼
 Voice Selector  Voice Selector Voice Selector
      │              │               │
      └──────────────┼───────────────┘
                     ▼
              Voice Manager
                     ▼
              Voice Profile
                     ▼
              Provider Factory
                     ▼
                Edge Provider



                Script.txt
                     │
                     ▼
           Language Detector
                     │
                     ▼
            Voice Selector
                     │
                     ▼
             Voice Manager
                     │
                     ▼
             Voice Profile
                     │
                     ▼
            Provider Factory
                     │
                     ▼
           Provider Registry
                     │
                     ▼
             Edge Provider
                     │
                     ▼
                audio.mp3

| Sprint | Arquivo                                | Status |
| ------ | -------------------------------------- | ------ |
| 8.4.1  | `models/language.py`                   | ⏳      |
| 8.4.2  | `services/language_detector.py`        | ⏳      |
| 8.4.3  | `services/voice_selector.py`           | ⏳      |
| 8.4.4  | `services/voice_manager.py` (evolução) | ⏳      |
| 8.4.5  | `config/config_manager.py`             | ⏳      |
| 8.4.6  | `services/speech_service.py`           | ⏳      |
| 8.4.7  | `config/voices.json`                   | ⏳      |
| 8.4.8  | Testes                                 | ⏳      |


Script
   │
   ▼
LanguageDetector
   │
   ▼
Language
   │
   ▼
VoiceSelector
   │
   ▼
VoiceProfile
   │
   ▼
SpeechService