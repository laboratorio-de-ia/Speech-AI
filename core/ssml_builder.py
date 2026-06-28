"""
=========================================================
Speech Text Builder - Edge TTS Compatible
---------------------------------------------------------
Substitui SSML real por texto otimizado para fala natural

Objetivo:
- eliminar tags SSML (Edge não suporta corretamente)
- criar ritmo humano com pontuação
- simular pausas naturais

=========================================================
"""

import re
import logging

from models.presentation import Presentation


logger = logging.getLogger(__name__)


class SSMLBuilder:
    """
    Na prática: Speech Optimizer para Edge TTS.
    (mantemos nome por compatibilidade do pipeline)
    """

    def __init__(self):

        self.presentation: Presentation | None = None

        self.output_text: str = ""

    # -----------------------------------------------------

    def load(self, presentation: Presentation):
        self.presentation = presentation

    # -----------------------------------------------------

    def _clean(self, text: str) -> str:
        """
        Remove qualquer vestígio de SSML antigo.
        """

        # remove tags se ainda existirem de versões anteriores
        text = re.sub(r"<[^>]+>", "", text)

        # normaliza espaços
        text = re.sub(r"\s+", " ", text)

        return text.strip()

    # -----------------------------------------------------

    def _naturalize(self, text: str) -> str:
        """
        Simula pausas naturais usando pontuação.
        """

        # pausa leve
        text = text.replace(",", ", ...")

        # pausa forte
        text = text.replace(".", ".\n")

        # dois pontos → pausa explicativa
        text = text.replace(":", ":\n...")

        return text

    # -----------------------------------------------------

    def _process_slide(self, slide) -> str:
        """
        Converte slide em fala natural.
        """

        lines = []

        # título do slide (pausa forte implícita)
        title = self._clean(slide.title)
        lines.append(title)
        lines.append("...")

        # parágrafos
        for p in slide.paragraphs:

            text = self._clean(p.text)
            text = self._naturalize(text)

            lines.append(text)

        # listas
        for lst in slide.lists:
            for item in lst.items:

                item = self._clean(item)
                lines.append("- " + item)
                lines.append("...")

        # separação entre slides
        lines.append("")
        lines.append("...")

        return "\n".join(lines)

    # -----------------------------------------------------

    def build(self) -> str:
        """
        Gera texto final otimizado para TTS.
        """

        if not self.presentation:
            raise ValueError("Presentation not loaded")

        logger.info("Building speech-optimized text...")

        blocks = []

        for slide in self.presentation.slides:

            block = self._process_slide(slide)

            blocks.append(block)

        self.output_text = "\n".join(blocks)

        logger.info("Speech text generated successfully")

        return self.output_text

    # -----------------------------------------------------

    def export(self, path: str):
        """
        Exporta texto final.
        """

        with open(path, "w", encoding="utf-8") as f:
            f.write(self.output_text)

        logger.info("Speech text exported to %s", path)