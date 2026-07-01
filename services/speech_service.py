"""
=========================================================
Speech Service
---------------------------------------------------------
Speech AI Platform

Responsável pela síntese de voz.

Fluxo:

Text
    ↓
Voice Selector
    ↓
Voice Profile
    ↓
TTS Engine
    ↓
Audio

Author: Rodrigo Magalhães
=========================================================
"""

from __future__ import annotations

import logging
from pathlib import Path

from config.config_manager import ConfigManager

from services.voice_selector import VoiceSelector
from services.tts_engine import TTSEngine

logger = logging.getLogger(__name__)


class SpeechService:

    # -------------------------------------------------

    def __init__(
        self,
        cfg: ConfigManager
    ):

        self.cfg = cfg

        self.voice_selector = VoiceSelector(cfg)

        self.tts = TTSEngine(cfg)

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

        # -------------------------------------------------
        # Automatic Voice Selection
        # -------------------------------------------------

        profile = self.voice_selector.select(

            text=text

        )

        logger.info("=" * 60)
        logger.info("VOICE PROFILE")
        logger.info("=" * 60)
        logger.info("Profile   : %s", profile.profile_id)
        logger.info("Name      : %s", profile.name)
        logger.info("Provider  : %s", profile.provider)
        logger.info("Language  : %s", profile.language)
        logger.info("Locale    : %s", profile.locale)
        logger.info("Voice     : %s", profile.voice)
        logger.info("Rate      : %s", profile.rate)
        logger.info("Pitch     : %s", profile.pitch)
        logger.info("Volume    : %s", profile.volume)
        logger.info("=" * 60)

        # -------------------------------------------------
        # Update Runtime Configuration
        # -------------------------------------------------

        self.cfg.voice = profile.voice
        self.cfg.language = profile.language
        self.cfg.rate = profile.rate
        self.cfg.pitch = profile.pitch
        self.cfg.volume = profile.volume

        logger.info("Generating audio...")

        self.tts.generate(

            text=text,

            output_path=output_file

        )

        logger.info("Speech synthesis finished.")

        return output_file