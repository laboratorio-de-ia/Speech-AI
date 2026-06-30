"""
=========================================================
TTS Engine - Speech AI
---------------------------------------------------------
Application Service

Responsável apenas por:

- Ler o texto de narração
- Selecionar o Provider
- Solicitar a geração do áudio

Toda implementação do mecanismo TTS fica isolada
nos Providers.

Author: Rodrigo Magalhães
=========================================================
"""

from pathlib import Path
import logging

from config.config_manager import ConfigManager
from providers import ProviderFactory

logger = logging.getLogger(__name__)


class TTSEngine:

    # -------------------------------------------------

    def __init__(self, cfg: ConfigManager):

        self.cfg = cfg

        self.provider = ProviderFactory.create(cfg)

        self.output_path = (
            Path(cfg.output_directory)
            / cfg.output_filename
        )

    # -------------------------------------------------

    def show_config(self):

        print()

        print("========== TTS CONFIG ==========")

        print(f"Provider : {self.cfg.provider}")

        print(f"Voice    : {self.cfg.voice}")

        print(f"Rate     : {self.cfg.rate}")

        print(f"Pitch    : {self.cfg.pitch}")

        print(f"Volume   : {self.cfg.volume}")

        print(f"Output   : {self.output_path}")

        print("================================")

        print()

    # -------------------------------------------------

    def generate(

        self,

        narration_path: str,

        output_path: str | Path | None = None

    ) -> Path:

        narration_path = Path(narration_path)

        if not narration_path.exists():

            raise FileNotFoundError(

                f"Narration file not found:\n{narration_path}"

            )

        if output_path is None:

            output_path = self.output_path

        else:

            output_path = Path(output_path)

        output_path.parent.mkdir(

            parents=True,

            exist_ok=True

        )

        text = narration_path.read_text(

            encoding="utf-8"

        )

        self.show_config()

        logger.info(

            "Generating audio using provider '%s'",

            self.cfg.provider

        )

        self.provider.generate(

            text=text,

            output_path=output_path

        )

        print("✅ Audio generated successfully!")

        print(f"📁 {output_path}")

        print()

        return output_path