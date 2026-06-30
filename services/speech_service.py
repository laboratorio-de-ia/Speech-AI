"""
=========================================================
Speech Service
---------------------------------------------------------
Speech AI Platform

Camada de serviço responsável pela geração de áudio.

Responsabilidades

- carregar o texto
- preparar diretórios
- criar o Provider
- instanciar o TTSEngine
- retornar o áudio gerado

Author: Rodrigo Magalhães
=========================================================
"""

from pathlib import Path

from config.config_manager import ConfigManager

from providers.provider_factory import ProviderFactory

from services.tts_engine import TTSEngine


class SpeechService:
    """
    Serviço responsável pela geração de áudio.
    """

    # -------------------------------------------------

    def __init__(self, cfg: ConfigManager):

        self.cfg = cfg

        provider = ProviderFactory.create(cfg)

        self.engine = TTSEngine(provider)

    # -------------------------------------------------

    def synthesize(
        self,
        narration_file: Path,
        output_file: Path
    ) -> Path:
        """
        Gera o áudio final.
        """

        if not narration_file.exists():

            raise FileNotFoundError(
                f"Narration file not found:\n{narration_file}"
            )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        text = narration_file.read_text(
            encoding="utf-8"
        )

        return self.engine.generate(
            text=text,
            output_path=output_file
        )