"""
=========================================================
Speech Service
---------------------------------------------------------
Speech AI Platform

Responsável pela síntese de voz.

Fluxo:

Narration File
        │
        ▼
Read Text
        │
        ▼
Voice Selector
        │
        ▼
Voice Profile
        │
        ▼
Provider Factory
        │
        ▼
TTS Engine
        │
        ▼
Audio

Author: Rodrigo Magalhães
=========================================================
"""

from __future__ import annotations

import logging
from pathlib import Path

from config.config_manager import ConfigManager

from providers.provider_factory import ProviderFactory

from services.tts_engine import TTSEngine
from services.voice_selector import VoiceSelector

logger = logging.getLogger(__name__)


class SpeechService:

    # -------------------------------------------------

    def __init__(
        self,
        cfg: ConfigManager
    ):

        self.cfg = cfg

        self.voice_selector = VoiceSelector(cfg)

    # -------------------------------------------------

    def synthesize(
        self,
        narration_file: Path,
        output_file: Path
    ) -> Path:

        logger.info("=" * 60)
        logger.info("Speech Service")
        logger.info("=" * 60)

        narration_file = Path(narration_file)

        if not narration_file.exists():

            raise FileNotFoundError(
                f"Narration file not found:\n{narration_file}"
            )

        logger.info("Loading narration...")

        text = narration_file.read_text(
            encoding="utf-8"
        )

        logger.info(
            "Characters loaded: %d",
            len(text)
        )

        # =====================================================
        # Automatic Voice Selection
        # =====================================================

        profile = self.voice_selector.select(
            text=text
        )

        logger.info("=" * 60)
        logger.info("VOICE PROFILE")
        logger.info("=" * 60)

        logger.info("Profile....: %s", profile.profile_id)
        logger.info("Name.......: %s", profile.name)
        logger.info("Provider...: %s", profile.provider)
        logger.info("Language...: %s", profile.language)
        logger.info("Locale.....: %s", profile.locale)
        logger.info("Voice......: %s", profile.voice)
        logger.info("Rate.......: %s", profile.rate)
        logger.info("Pitch......: %s", profile.pitch)
        logger.info("Volume.....: %s", profile.volume)

        logger.info("=" * 60)

        # =====================================================
        # Provider Factory
        # =====================================================

        provider = ProviderFactory.create_from_profile(
            profile
        )

        logger.info(
            "Provider instantiated: %s",
            provider
        )

        # =====================================================
        # TTS Engine
        # =====================================================

        tts = TTSEngine(
            provider
        )

        logger.info(
            "Generating audio..."
        )

        audio = tts.generate(

            text=text,

            output_path=output_file

        )

        logger.info(
            "Speech synthesis completed successfully."
        )

        return audio