"""
=========================================================
Voice Selector
---------------------------------------------------------
Speech AI Platform

Seleciona automaticamente o VoiceProfile ideal a partir
do texto recebido.

Fluxo:

Text
    ↓
LanguageDetector
    ↓
VoiceManager
    ↓
VoiceProfile

Author: Rodrigo Magalhães
=========================================================
"""

import logging

from config.config_manager import ConfigManager

from models import VoiceProfile

from services.language_detector import LanguageDetector

logger = logging.getLogger(__name__)


class VoiceSelector:

    # -------------------------------------------------

    def __init__(self, cfg: ConfigManager):

        self.cfg = cfg

        self.voice_manager = cfg.voice_manager

        self.detector = LanguageDetector()

    # -------------------------------------------------

    def select(
        self,
        text: str
    ) -> VoiceProfile:

        # ---------------------------------------------
        # Detect Language
        # ---------------------------------------------

        language = self.detector.detect(text)

        logger.info(
            "Detected language: %s",
            language.code
        )

        # ---------------------------------------------
        # Select Voice
        # ---------------------------------------------

        profile = self.voice_manager.get_default_by_language(

            language=language.code,

            provider=self.cfg.provider

        )

        if profile is None:

            raise ValueError(

                f"No VoiceProfile found for language "

                f"'{language.code}'."

            )

        logger.info(
            "Voice selected: %s",
            profile.voice
        )

        return profile

    # -------------------------------------------------

    def __call__(
        self,
        text: str
    ) -> VoiceProfile:

        return self.select(text)