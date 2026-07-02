"""
=========================================================
Speech Optimizer
---------------------------------------------------------
Speech AI Platform

Converte um SpeechAnalysis em um SpeechProfile.

Author: Rodrigo Magalhães
=========================================================
"""

from __future__ import annotations

import logging

from models.speech_profile import SpeechProfile

logger = logging.getLogger(__name__)


class SpeechOptimizer:

    def optimize(

        self,

        analysis,

        voice_profile

    ) -> SpeechProfile:

        logger.info("=" * 60)
        logger.info("Speech Optimizer")
        logger.info("=" * 60)

        profile = SpeechProfile()

        profile.language = analysis.language

        profile.voice = voice_profile.voice

        profile.locale = voice_profile.locale

        profile.provider = voice_profile.provider

        profile.rate = analysis.recommended_rate

        profile.recommended_wpm = analysis.recommended_wpm

        profile.complexity = analysis.complexity

        profile.estimated_minutes = analysis.estimated_minutes

        # ----------------------------------------
        # Pitch
        # ----------------------------------------

        if analysis.complexity == "High":

            profile.pitch = "-1Hz"

            profile.pacing = "Slow"

        elif analysis.complexity == "Medium":

            profile.pitch = "+0Hz"

            profile.pacing = "Normal"

        else:

            profile.pitch = "+1Hz"

            profile.pacing = "Fast"

        # ----------------------------------------
        # Reading Style
        # ----------------------------------------

        if analysis.average_words_per_sentence >= 20:

            profile.reading_style = "Technical"

        elif analysis.average_words_per_sentence >= 14:

            profile.reading_style = "Business"

        else:

            profile.reading_style = "Conversational"

        # ----------------------------------------
        # Confidence
        # ----------------------------------------

        confidence = 1.0

        if analysis.words < 150:

            confidence -= 0.10

        if analysis.sentences < 8:

            confidence -= 0.10

        profile.confidence = round(confidence, 2)

        logger.info("Voice........ %s", profile.voice)
        logger.info("Rate......... %s", profile.rate)
        logger.info("Pitch........ %s", profile.pitch)
        logger.info("Reading...... %s", profile.reading_style)
        logger.info("Complexity... %s", profile.complexity)
        logger.info("Confidence... %.2f", profile.confidence)

        return profile