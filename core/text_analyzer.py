"""
=========================================================
Text Analyzer - Speech AI
---------------------------------------------------------
Sprint 2.1

Responsável por transformar texto bruto em estrutura:

script.txt → Presentation (Slides + Paragraphs)

=========================================================
"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import re
import logging
from typing import List

from models.presentation import Presentation
from models.slide import Slide
from models.paragraph import Paragraph
from models.statistics import SpeechStatistics

from config import SCRIPT_FILE, WORDS_PER_MINUTE


# =========================================================
# LOGGER
# =========================================================

logger = logging.getLogger(__name__)


# =========================================================
# TEXT ANALYZER
# =========================================================

class TextAnalyzer:
    """
    Converte texto em estrutura de apresentação.
    """

    def __init__(self):

        self.raw_text: str = ""

        self.presentation = Presentation()

    # -----------------------------------------------------

    def load(self) -> None:
        """
        Carrega o script.txt
        """

        logger.info("Loading script...")

        if not SCRIPT_FILE.exists():
            raise FileNotFoundError(
                f"Script not found: {SCRIPT_FILE}"
            )

        self.raw_text = SCRIPT_FILE.read_text(
            encoding="utf-8"
        )

    # -----------------------------------------------------

    def normalize(self) -> None:
        """
        Limpa o texto bruto.
        """

        logger.info("Normalizing text...")

        text = self.raw_text

        text = text.replace("\r\n", "\n")

        text = re.sub(r"[ \t]+", " ", text)

        text = re.sub(r"\n{3,}", "\n\n", text)

        self.raw_text = text.strip()

    # -----------------------------------------------------

    def detect_slides(self) -> List[str]:
        """
        Detecta blocos de slides.
        """

        logger.info("Detecting slides...")

        slides_raw = re.split(
            r"(?i)(?=slide\s+\d+)",
            self.raw_text
        )

        return [s.strip() for s in slides_raw if s.strip()]

    # -----------------------------------------------------

    def parse_slide(self, slide_text: str, index: int) -> Slide:
        """
        Converte texto de slide em objeto Slide.
        """

        lines = slide_text.split("\n")

        title = lines[0].strip()

        slide = Slide(
            number=index,
            title=title
        )

        for line in lines[1:]:

            line = line.strip()

            if not line:
                continue

            # Detecta lista simples
            if re.match(r"^[-•*]", line):

                slide.add_list([line])

            else:

                slide.add_paragraph(line)

        return slide

    # -----------------------------------------------------

    def build_presentation(self) -> Presentation:
        """
        Constrói objeto Presentation.
        """

        logger.info("Building presentation structure...")

        slides_raw = self.detect_slides()

        for i, slide_text in enumerate(slides_raw, start=1):

            slide = self.parse_slide(slide_text, i)

            self.presentation.add_slide(slide)

        return self.presentation

    # -----------------------------------------------------

    def calculate_statistics(self) -> None:
        """
        Calcula métricas da apresentação.
        """

        logger.info("Calculating statistics...")

        words = re.findall(r"\b[\w'-]+\b", self.raw_text)

        sentences = re.split(r"[.!?]+", self.raw_text)

        paragraphs = self.raw_text.split("\n\n")

        stats = SpeechStatistics()

        stats.words = len(words)

        stats.sentences = len(
            [s for s in sentences if s.strip()]
        )

        stats.paragraphs = len(
            [p for p in paragraphs if p.strip()]
        )

        stats.characters = len(self.raw_text)

        stats.estimated_minutes = round(
            stats.words / WORDS_PER_MINUTE,
            2
        )

        self.presentation.statistics = stats

    # -----------------------------------------------------

    def run(self) -> Presentation:
        """
        Pipeline principal.
        """

        logger.info("Starting Text Analyzer...")

        self.load()

        self.normalize()

        self.build_presentation()

        self.calculate_statistics()

        logger.info("Text Analyzer completed.")

        return self.presentation