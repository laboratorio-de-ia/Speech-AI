"""
=========================================================
Voice Selector
---------------------------------------------------------
Speech AI Platform

Responsável apenas por selecionar o VoiceProfile
mais adequado para um idioma já detectado.

Fluxo:

Language
    ↓
VoiceManager
    ↓
VoiceProfile

Author: Rodrigo Magalhães
=========================================================
"""

from __future__ import annotations

import logging

from config.config_manager import ConfigManager

from models import Language
from models import VoiceProfile

logger = logging.getLogger(__name__)


class VoiceSelector:
    """
    Seleciona automaticamente um VoiceProfile
    a partir de um objeto Language.
    """

    # -------------------------------------------------

    def __init__(self, cfg: ConfigManager):

        self.cfg = cfg

        self.voice_manager = cfg.voice_manager

    # -------------------------------------------------

    def select(
        self,
        language: Language
    ) -> VoiceProfile:

        logger.info(
            "Selecting voice for language: %s",
            language.code
        )

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
        language: Language
    ) -> VoiceProfile:

        return self.select(language)