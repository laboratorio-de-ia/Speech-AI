"""
=========================================================
Provider Factory
---------------------------------------------------------
Speech AI Platform

Responsável por criar instâncias de Providers TTS.

Nesta versão, a Factory utiliza o ProviderRegistry
para localizar dinamicamente o Provider configurado.

Author: Rodrigo Magalhães
=========================================================
"""

from config.config_manager import ConfigManager

from providers import ProviderRegistry


class ProviderFactory:
    """
    Factory responsável por criar Providers TTS.
    """

    # -------------------------------------------------

    @staticmethod
    def create(cfg: ConfigManager):
        """
        Cria a instância do Provider configurado.

        Parameters
        ----------
        cfg
            Configuração da aplicação.

        Returns
        -------
        BaseTTSProvider
        """

        provider_id = cfg.provider.lower()

        provider_class = ProviderRegistry.get(
            provider_id
        )

        return provider_class(
            voice=cfg.voice,
            rate=cfg.rate,
            pitch=cfg.pitch,
            volume=cfg.volume
        )