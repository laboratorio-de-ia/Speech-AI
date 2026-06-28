"""
=========================================================
Narration Builder - Speech AI
---------------------------------------------------------
Sprint 3

Transforma estrutura (Presentation) em texto natural
para narração humana e futura geração de SSML.

=========================================================
"""

import re
import logging

from models.presentation import Presentation
from models.slide import Slide
from models.paragraph import Paragraph


# =========================================================
# LOGGER
# =========================================================

logger = logging.getLogger(__name__)


# =========================================================
# NARRATION BUILDER
# =========================================================

class NarrationBuilder:
    """
    Responsável por humanizar o texto para fala.
    """

    def __init__(self):

        self.presentation: Presentation | None = None

        self.output_blocks: list[str] = []

    # -----------------------------------------------------

    def load(self, presentation: Presentation):
        """
        Recebe a Presentation estruturada.
        """

        self.presentation = presentation

    # -----------------------------------------------------

    def _break_long_sentence(self, text: str) -> str:
        """
        Quebra frases longas para simular respiração humana.
        """

        # separa por conectores comuns
        text = re.sub(r",", "...,", text)

        text = re.sub(
            r"\band\b",
            "and...",
            text,
            flags=re.IGNORECASE
        )

        text = re.sub(
            r"\bwith\b",
            "with...",
            text,
            flags=re.IGNORECASE
        )

        return text

    # -----------------------------------------------------

    def _process_paragraph(self, text: str) -> str:
        """
        Aplica regras de fala natural.
        """

        text = text.strip()

        # quebra frases muito longas
        if len(text.split()) > 18:
            text = self._break_long_sentence(text)

        # pausa após dois pontos
        text = text.replace(":", ":\n")

        return text

    # -----------------------------------------------------

    def _process_slide(self, slide: Slide) -> str:
        """
        Converte um slide em bloco de narração.
        """

        lines = []

        # Título do slide (com pausa forte)
        lines.append(slide.title + "...\n")

        # Parágrafos
        for p in slide.paragraphs:

            processed = self._process_paragraph(p.text)

            lines.append(processed + "\n")

        # Listas (ritmo mais marcado)
        for lst in slide.lists:

            for item in lst.items:

                lines.append("- " + item + "...\n")

        return "\n".join(lines)

    # -----------------------------------------------------

    def build(self) -> list[str]:
        """
        Constrói narrativa completa.
        """

        if not self.presentation:
            raise ValueError("Presentation not loaded")

        logger.info("Building narration...")

        self.output_blocks.clear()

        for slide in self.presentation.slides:

            block = self._process_slide(slide)

            self.output_blocks.append(block)

        logger.info(
            "%s narration blocks created",
            len(self.output_blocks)
        )

        return self.output_blocks

    # -----------------------------------------------------

    def export_text(self, path: str):
        """
        Exporta texto final humanizado.
        """

        full_text = "\n\n".join(self.output_blocks)

        with open(path, "w", encoding="utf-8") as f:
            f.write(full_text)

        logger.info("Narration exported to %s", path)