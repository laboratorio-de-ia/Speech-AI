"""
=========================================================
Speech AI Application
---------------------------------------------------------
Application Kernel

Responsável por:

- Configuração
- Pipeline
- Dependency Injection
- Logging
- Services

Author: Rodrigo Magalhães
=========================================================
"""

import logging
from pathlib import Path

from config.config_manager import ConfigManager

from core.text_analyzer import TextAnalyzer
from core.narration_builder import NarrationBuilder
from core.ssml_builder import SSMLBuilder
from core.tts_engine import TTSEngine


class SpeechAIApp:

    # -------------------------------------------------

    def __init__(self):

        self.cfg = ConfigManager()

        self.project_root = Path(__file__).resolve().parent

        self.logger = logging.getLogger(__name__)

        self._configure_logging()

        self._show_banner()

    # -------------------------------------------------

    def _configure_logging(self):

        logs = self.project_root / "logs"

        logs.mkdir(exist_ok=True)

        logging.basicConfig(
            filename=logs / "app.log",
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
        )

    # -------------------------------------------------

    def _show_banner(self):

        print()

        print("=" * 60)
        print(f" {self.cfg.project_name}")
        print("=" * 60)

        print(f"Version : {self.cfg.project_version}")

        print("=" * 60)

    # -------------------------------------------------

    def show_configuration(self):

        self.cfg.show()

    # -------------------------------------------------

    def run(self):

        print()

        print("Starting pipeline...\n")

        self.logger.info("Pipeline started")

        # ==============================================
        # Text Analyzer
        # ==============================================

        analyzer = TextAnalyzer(self.cfg)

        presentation = analyzer.run()

        # ==============================================
        # Narration
        # ==============================================

        narrator = NarrationBuilder(self.cfg)

        narrator.load(presentation)

        narration_blocks = narrator.build()

        narration_file = (
            self.project_root
            / "output"
            / "narration.txt"
        )

        narrator.export_text(str(narration_file))

        # ==============================================
        # SSML
        # ==============================================

        ssml = SSMLBuilder(self.cfg)

        ssml.load(presentation)

        ssml.build()

        ssml_file = (
            self.project_root
            / "output"
            / "speech.xml"
        )

        ssml.export(str(ssml_file))

        # ==============================================
        # Audio
        # ==============================================

        tts = TTSEngine(self.cfg)

        audio_file = (
            self.project_root
            / self.cfg.output_directory
            / self.cfg.output_filename
        )

        tts.generate(
            narration_path=str(narration_file),
            output_path=str(audio_file)
        )

        # ==============================================

        print()

        print("=" * 50)
        print(" Pipeline Finished")
        print("=" * 50)

        print(f"Slides............ {presentation.total_slides()}")
        print(f"Words............. {presentation.statistics.words}")

        print(
            f"Estimated Duration {presentation.statistics.estimated_minutes} min"
        )

        print()

        print(f"Audio............. {audio_file}")

        print()

        self.logger.info("Pipeline finished")

    # -------------------------------------------------

    def get_config(self):

        return self.cfg