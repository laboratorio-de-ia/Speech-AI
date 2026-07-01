"""
=========================================================
Language Detection Service
---------------------------------------------------------
Speech AI Platform

Responsável por detectar automaticamente o idioma
predominante do texto utilizando detecção offline.

Author: Rodrigo Magalhães
=========================================================
"""

import logging

from langdetect import DetectorFactory
from langdetect import detect_langs

from models import Language

logger = logging.getLogger(__name__)

# Garante resultados determinísticos
DetectorFactory.seed = 0


class LanguageDetector:
    """
    Serviço responsável por detectar o idioma
    predominante de um texto.
    """

    # -------------------------------------------------

    LANGUAGE_MAP = {

        "pt": Language(
            code="pt",
            locale="pt-BR",
            name="Portuguese"
        ),

        "en": Language(
            code="en",
            locale="en-US",
            name="English"
        ),

        "es": Language(
            code="es",
            locale="es-ES",
            name="Spanish"
        ),

        "fr": Language(
            code="fr",
            locale="fr-FR",
            name="French"
        ),

    }

    # -------------------------------------------------

    def detect(
        self,
        text: str
    ) -> Language:

        if not text.strip():

            raise ValueError(
                "Cannot detect language from empty text."
            )

        logger.info(
            "Detecting language..."
        )

        result = detect_langs(text)[0]

        code = result.lang

        confidence = result.prob

        language = self.LANGUAGE_MAP.get(code)

        if language is None:

            logger.warning(
                "Unsupported language detected: %s",
                code
            )

            return Language(
                code=code,
                locale=code,
                name="Unknown",
                confidence=confidence
            )

        detected = Language(

            code=language.code,

            locale=language.locale,

            name=language.name,

            confidence=confidence

        )

        logger.info(

            "Language detected: %s (%.2f%%)",

            detected.name,

            confidence * 100

        )

        return detected

    # -------------------------------------------------

    def detect_file(
        self,
        file_path
    ) -> Language:

        with open(
            file_path,
            encoding="utf-8"
        ) as f:

            text = f.read()

        return self.detect(text)