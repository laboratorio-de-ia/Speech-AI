from dataclasses import dataclass


@dataclass
class SpeechStatistics:
    """
    Centraliza métricas da apresentação.
    """

    characters: int = 0
    words: int = 0
    sentences: int = 0
    paragraphs: int = 0

    estimated_minutes: float = 0.0