"""
=========================================================
Provider Factory
---------------------------------------------------------
Speech AI Platform

Factory responsável por criar Providers TTS.

Suporta duas formas de criação:

1. ConfigManager (compatibilidade)
2. VoiceProfile (arquitetura dinâmica)

Fluxo:

ConfigManager
        │
        ▼
ProviderFactory.create()

----------------------------

VoiceProfile
        │
        ▼
ProviderFactory.create_from_profile()

Author: Rodrigo Magalhães
=========================================================
"""

from __future__ import annotations

import logging

from config.config_manager import ConfigManager

from models.voice_profile import VoiceProfile

from providers.provider_registry import ProviderRegistry

logger = logging.getLogger(__name__)


class ProviderFactory:
    """
    Factory responsável pela criação de Providers TTS.
    """

    # -------------------------------------------------
    # Legacy
    # -------------------------------------------------

    @staticmethod
    def create(cfg: ConfigManager):
        """
        Cria um Provider utilizando as configurações
        padrão do ConfigManager.

        Mantido para compatibilidade com versões
        anteriores.
        """

        provider_id = cfg.provider.lower()

        logger.info(
            "Creating provider from ConfigManager: %s",
            provider_id
        )

        provider_class = ProviderRegistry.get(
            provider_id
        )

        provider = provider_class(

            voice=cfg.voice,

            rate=cfg.rate,

            pitch=cfg.pitch,

            volume=cfg.volume

        )

        logger.info(
            "Provider created successfully: %s",
            provider.__class__.__name__
        )

        return provider

    # -------------------------------------------------
    # Runtime
    # -------------------------------------------------

    @staticmethod
    def create_from_profile(
        profile: VoiceProfile
    ):
        """
        Cria um Provider utilizando um VoiceProfile.

        Utilizado pela seleção automática de idioma.
        """

        provider_id = profile.provider.lower()

        logger.info(
            "Creating provider from VoiceProfile: %s",
            provider_id
        )

        provider_class = ProviderRegistry.get(
            provider_id
        )

        provider = provider_class(

            voice=profile.voice,

            rate=profile.rate,

            pitch=profile.pitch,

            volume=profile.volume

        )

        logger.info(
            "Voice........: %s",
            profile.voice
        )

        logger.info(
            "Language.....: %s",
            profile.language
        )

        logger.info(
            "Locale.......: %s",
            profile.locale
        )

        logger.info(
            "Provider created successfully."
        )

        return provider

    # -------------------------------------------------

    @staticmethod
    def available_providers():
        """
        Retorna todos os Providers registrados.
        """

        return ProviderRegistry.available()

    # -------------------------------------------------

    @staticmethod
    def exists(provider_id: str) -> bool:
        """
        Verifica se um Provider está registrado.
        """

        return provider_id.lower() in ProviderRegistry.available()

    # -------------------------------------------------

    def __str__(self):

        return "ProviderFactory"