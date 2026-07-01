from services.language_detector import LanguageDetector

detector = LanguageDetector()

language = detector.detect_file(
    "input/script.txt"
)

print(language)