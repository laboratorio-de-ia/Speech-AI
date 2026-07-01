from config.config_manager import ConfigManager

from pipeline.text_analyzer import TextAnalyzer

from services.language_detector import LanguageDetector

from services.speech_analyzer import SpeechAnalyzer

cfg = ConfigManager()

presentation = TextAnalyzer(cfg).run()

language = LanguageDetector().detect(
    presentation.to_text()
)

analysis = SpeechAnalyzer().analyze(
    presentation,
    language
)

print(analysis)