"""
=========================================================
Text Analyzer - Speech AI
---------------------------------------------------------
Sprint 6.4.1

Responsável por transformar texto bruto em:

script.txt -> Presentation

Agora utilizando Dependency Injection.
=========================================================
"""

import logging
import re
from pathlib import Path
from typing import List

from config.config_manager import ConfigManager

from models.presentation import Presentation
from models.slide import Slide
from models.statistics import SpeechStatistics

logger = logging.getLogger(__name__)


class TextAnalyzer:

    def __init__(self, cfg: ConfigManager):

        self.cfg = cfg

        self.raw_text: str = ""

        self.presentation = Presentation()

    # -----------------------------------------------------

    def load(self):

        logger.info("Loading script...")

        script_file = Path(self.cfg.script_file)

        if not script_file.exists():

            raise FileNotFoundError(
                f"Script not found:\n{script_file}"
            )

        self.raw_text = script_file.read_text(
            encoding="utf-8"
        )

    # -----------------------------------------------------

    def normalize(self):

        logger.info("Normalizing text...")

        text = self.raw_text

        text = text.replace("\r\n", "\n")

        text = re.sub(r"[ \t]+", " ", text)

        text = re.sub(r"\n{3,}", "\n\n", text)

        self.raw_text = text.strip()

    # -----------------------------------------------------

    def detect_slides(self) -> List[str]:

        logger.info("Detecting slides...")

        slides_raw = re.split(
            r"(?i)(?=slide\s+\d+)",
            self.raw_text,
        )

        return [
            slide.strip()
            for slide in slides_raw
            if slide.strip()
        ]

    # -----------------------------------------------------

    def parse_slide(
        self,
        slide_text: str,
        index: int
    ):

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

            if re.match(r"^[-•*]", line):

                slide.add_list([line])

            else:

                slide.add_paragraph(line)

        return slide

    # -----------------------------------------------------

    def build_presentation(self):

        logger.info("Building presentation...")

        slides = self.detect_slides()

        for index, slide_text in enumerate(slides, start=1):

            slide = self.parse_slide(
                slide_text,
                index
            )

            self.presentation.add_slide(slide)

        return self.presentation

    # -----------------------------------------------------

    def calculate_statistics(self):

        logger.info("Calculating statistics...")

        stats = SpeechStatistics()

        words = re.findall(
            r"\b[\w'-]+\b",
            self.raw_text
        )

        sentences = re.split(
            r"[.!?]+",
            self.raw_text
        )

        paragraphs = self.raw_text.split("\n\n")

        stats.words = len(words)

        stats.sentences = len(
            [s for s in sentences if s.strip()]
        )

        stats.paragraphs = len(
            [p for p in paragraphs if p.strip()]
        )

        stats.characters = len(
            self.raw_text
        )

        stats.estimated_minutes = round(
            stats.words /
            self.cfg.words_per_minute,
            2
        )

        self.presentation.statistics = stats

    # -----------------------------------------------------

    def run(self):

        logger.info("Starting Text Analyzer")

        self.load()

        self.normalize()

        self.build_presentation()

        self.calculate_statistics()

        logger.info("Text Analyzer completed")

        return self.presentation