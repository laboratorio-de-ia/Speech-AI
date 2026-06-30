"""
=========================================================
Provider Factory

Responsável por instanciar o provider configurado.

Author: Rodrigo Magalhães
=========================================================
"""

from config.config_manager import ConfigManager

from .edge_provider import EdgeProvider


class ProviderFactory:

    @staticmethod
    def create(cfg: ConfigManager):

        provider = cfg.provider.lower()

        if provider == "edge":

            return EdgeProvider(
                voice=cfg.voice,
                rate=cfg.rate,
                pitch=cfg.pitch,
                volume=cfg.volume
            )

        raise ValueError(
            f"Unsupported TTS provider: {provider}"
        )