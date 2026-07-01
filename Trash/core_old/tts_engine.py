"""
=========================================================
TTS Engine - Speech AI
---------------------------------------------------------
Sprint 6.4.4

Responsável pela geração de áudio utilizando o provider
configurado.

Nesta versão continua utilizando Edge TTS, porém já
preparado para evolução para múltiplos providers.

Author: Rodrigo Magalhães
=========================================================
"""

import asyncio
import logging
from pathlib import Path

import edge_tts

from config.config_manager import ConfigManager

logger = logging.getLogger(__name__)


class TTSEngine:

    # -------------------------------------------------

    def __init__(self, cfg: ConfigManager):

        self.cfg = cfg

        self.voice = cfg.voice
        self.rate = cfg.rate
        self.pitch = cfg.pitch
        self.volume = cfg.volume

        self.output_path = (
            Path(cfg.output_directory)
            / cfg.output_filename
        )

    # -------------------------------------------------

    def show_config(self):

        print()

        print("========== TTS CONFIG ==========")
        print(f"Voice   : {self.voice}")
        print(f"Rate    : {self.rate}")
        print(f"Pitch   : {self.pitch}")
        print(f"Volume  : {self.volume}")
        print(f"Output  : {self.output_path}")
        print("================================")
        print()

    # -------------------------------------------------

    async def _generate_audio(
        self,
        text: str,
        output_path: Path
    ):

        logger.info(
            "Generating audio using Edge TTS..."
        )

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
            rate=self.rate,
            pitch=self.pitch,
            volume=self.volume
        )

        await communicate.save(
            str(output_path)
        )

        logger.info(
            "Audio generated successfully."
        )

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

        asyncio.run(

            self._generate_audio(

                text=text,

                output_path=output_path

            )

        )

        print("✅ Audio generated successfully!")

        print(f"📁 {output_path}")

        print()

        return output_path