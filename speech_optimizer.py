"""
=========================================================
Speech Optimizer
---------------------------------------------------------
Sprint 2.1

Responsável por:

- Ler o roteiro
- Normalizar o texto
- Calcular estatísticas
- Estimar duração
- Preparar o roteiro para otimizações futuras

Autor: Rodrigo Magalhães
Versão: 1.0.0
=========================================================
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

from config import (
    SCRIPT_FILE,
    OPTIMIZED_SCRIPT_FILE,
    REPORT_FILE,
    LOG_FILE,
    WORDS_PER_MINUTE,
    TARGET_DURATION_MINUTES,
    BANNER,
)

# ==========================================================
# LOGGER
# ==========================================================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)

# ==========================================================
# DATA CLASS
# ==========================================================


@dataclass
class SpeechStatistics:
    characters: int = 0
    words: int = 0
    sentences: int = 0
    paragraphs: int = 0
    estimated_minutes: float = 0.0


# ==========================================================
# SPEECH OPTIMIZER
# ==========================================================


class SpeechOptimizer:

    def __init__(self):

        self.original_text: str = ""
        self.optimized_text: str = ""

        self.sentences: List[str] = []
        # Slides detectados
        self.slides: List[dict] = []

        # Listas encontradas
        self.lists: List[List[str]] = []

        # Estrutura preparada para narração
        self.narration_blocks: List[str] = []

        self.statistics = SpeechStatistics()

    # ------------------------------------------------------

    def load_script(self) -> None:

        """
        Carrega o roteiro.
        """

        logger.info("Loading script...")

        if not SCRIPT_FILE.exists():
            raise FileNotFoundError(
                f"Script not found: {SCRIPT_FILE}"
            )

        self.original_text = SCRIPT_FILE.read_text(
            encoding="utf-8"
        )

        logger.info("Script loaded successfully.")

    # ------------------------------------------------------

    def normalize_text(self) -> None:

        """
        Remove espaços duplicados e padroniza quebras.
        """

        logger.info("Normalizing text...")

        text = self.original_text

        text = text.replace("\r\n", "\n")

        text = re.sub(r"[ \t]+", " ", text)

        text = re.sub(r"\n{3,}", "\n\n", text)

        self.optimized_text = text.strip()

        logger.info("Normalization complete.")

    # ------------------------------------------------------

    def tokenize_sentences(self) -> None:

        """
        Divide o roteiro em frases.
        """

        logger.info("Tokenizing sentences...")

        pattern = r'(?<=[.!?])\s+'

        self.sentences = [
            s.strip()
            for s in re.split(pattern, self.optimized_text)
            if s.strip()
        ]

        logger.info(
            "Detected %s sentences.",
            len(self.sentences),
        )

    # ------------------------------------------------------

    def calculate_statistics(self) -> None:

        """
        Calcula estatísticas básicas.
        """

        logger.info("Calculating statistics...")

        words = re.findall(r"\b[\w'-]+\b", self.optimized_text)

        paragraphs = [
            p for p in self.optimized_text.split("\n\n")
            if p.strip()
        ]

        self.statistics.characters = len(self.optimized_text)

        self.statistics.words = len(words)

        self.statistics.sentences = len(self.sentences)

        self.statistics.paragraphs = len(paragraphs)

        self.statistics.estimated_minutes = round(
            self.statistics.words / WORDS_PER_MINUTE,
            2,
        )

    # ------------------------------------------------------

    def print_summary(self) -> None:

        print("\n")

        print("=" * 60)

        print("Speech Optimizer")

        print("=" * 60)

        print(f"Characters : {self.statistics.characters}")

        print(f"Words      : {self.statistics.words}")

        print(f"Sentences  : {self.statistics.sentences}")

        print(f"Paragraphs : {self.statistics.paragraphs}")

        print(
            f"Estimated Duration : "
            f"{self.statistics.estimated_minutes:.2f} min"
        )

        print(
            f"Target Duration    : "
            f"{TARGET_DURATION_MINUTES} min"
        )

        delta = (
            TARGET_DURATION_MINUTES
            - self.statistics.estimated_minutes
        )

        if delta > 0:
            print(f"Missing approximately {delta:.2f} minutes.")

        elif delta < 0:
            print(
                f"Approximately {-delta:.2f} minutes longer."
            )

        else:
            print("Estimated duration matches the target.")

        print(f"Slides     : {len(self.slides)}")

        print(f"Lists      : {len(self.lists)}")

        print(
              f"Narration Blocks : {len(self.narration_blocks)}"
              )

        print("=" * 60)

    # ------------------------------------------------------

    def save_current_script(self) -> None:

        """
        Salva a versão atual do roteiro.
        """

        logger.info("Saving optimized script...")

        OPTIMIZED_SCRIPT_FILE.write_text(
            self.optimized_text,
            encoding="utf-8",
        )

    # ------------------------------------------------------

    def generate_report(self) -> None:

        """
        Gera relatório simples em JSON.
        """

        import json

        logger.info("Generating report...")

        REPORT_FILE.write_text(
            json.dumps(
                asdict(self.statistics),
                indent=4,
            ),
            encoding="utf-8",
        )

    # ------------------------------------------------------

    def run(self) -> None:

        print(BANNER)

        logger.info("Starting Speech Optimizer.")

        self.load_script()

        self.normalize_text()

        self.tokenize_sentences()

        self.calculate_statistics()

        self.detect_slides()

        self.detect_lists()

        self.prepare_narration()

        self.save_current_script()

        self.generate_report()

        self.print_summary()

        self.save_current_script()

        self.generate_report()

        self.print_summary()

        logger.info("Finished successfully.")
        
        def detect_slides(self) -> None:
            """
            Detecta automaticamente os slides da apresentação.

            Critérios:
            - Linhas iniciadas por 'Slide'
            - Slide 1
            - Slide 2
            - etc.
            """

            logger.info("Detecting slides...")

            lines = self.optimized_text.splitlines()

            current = None

            for line in lines:

                line = line.strip()

                if not line:
                    continue

                if re.match(r"^slide\s+\d+", line, re.IGNORECASE):

                    if current:
                        self.slides.append(current)

                    current = {
                        "title": line,
                        "content": []
                    }

                    continue

                if current:
                    current["content"].append(line)

            if current:
                self.slides.append(current)

            logger.info(
                "%s slides detected.",
                len(self.slides)
            )
            
        def detect_lists(self) -> None:
            """
            Procura listas simples.

            Exemplo:

            • item
            - item
            * item
            """

            logger.info("Detecting lists...")

            current = []

            for line in self.optimized_text.splitlines():

                line = line.strip()

                if re.match(r"^[-*•]", line):

                    current.append(line)

                else:

                    if len(current) > 1:
                        self.lists.append(current)

                    current = []

            if len(current) > 1:
                self.lists.append(current)

            logger.info(
                "%s lists detected.",
                len(self.lists)
            )


# ==========================================================
# MAIN
# ==========================================================

if __name__ == "__main__":

    optimizer = SpeechOptimizer()

    optimizer.run()