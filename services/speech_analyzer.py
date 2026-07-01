"""
=========================================================
Speech Analyzer
---------------------------------------------------------
Speech AI Platform

Analisa o roteiro antes da síntese.

Author: Rodrigo Magalhães
=========================================================
"""

from __future__ import annotations

import re
import logging

from models.speech_analysis import SpeechAnalysis

logger = logging.getLogger(__name__)


class SpeechAnalyzer:

    DEFAULT_WPM = 145

    def analyze(
        self,
        presentation,
        language
    ) -> SpeechAnalysis:

        logger.info("Running Speech Analyzer...")

        analysis = SpeechAnalysis()

        analysis.language = language.code

        stats = presentation.statistics

        analysis.words = stats.words
        analysis.characters = stats.characters
        analysis.sentences = stats.sentences
        analysis.paragraphs = stats.paragraphs
        analysis.estimated_minutes = stats.estimated_minutes

        analysis.slides = presentation.total_slides

        text = presentation.to_text()

        analysis.list_items = len(
            re.findall(r"^[-•*]", text, flags=re.MULTILINE)
        )

        analysis.numbers = len(
            re.findall(r"\d+", text)
        )

        words = re.findall(r"\b[\w'-]+\b", text)

        uppercase = [
            w for w in words
            if len(w) > 1 and w.isupper()
        ]

        analysis.uppercase_words = len(uppercase)

        if analysis.sentences > 0:

            analysis.average_words_per_sentence = round(
                analysis.words /
                analysis.sentences,
                1
            )

        if analysis.words > 0:

            analysis.average_word_length = round(

                sum(len(w) for w in words) /
                analysis.words,

                1

            )

        logger.info("Speech Analyzer completed.")

        return analysis