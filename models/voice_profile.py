"""
=========================================================
Voice Profile
---------------------------------------------------------
Speech AI Platform

Representa um perfil completo de voz utilizado pelos
Providers TTS.

Esta classe encapsula todas as configurações necessárias
para geração de áudio, permitindo que diferentes
providers utilizem a mesma estrutura de configuração.

A classe não possui lógica de negócio.

Ela representa apenas um objeto de domínio.

Author: Rodrigo Magalhães
=========================================================
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class VoiceProfile:
    """
    Representa um perfil de voz.

    Um perfil agrupa todas as configurações necessárias
    para sintetizar áudio utilizando um Provider TTS.
    """

    # -------------------------------------------------
    # Identificação
    # -------------------------------------------------

    profile_id: str

    name: str

    description: str

    # -------------------------------------------------
    # Idioma
    # -------------------------------------------------

    language: str

    locale: str

    # -------------------------------------------------
    # Configuração da voz
    # -------------------------------------------------

    voice: str

    rate: str

    pitch: str

    volume: str

    # -------------------------------------------------
    # Recursos avançados
    # -------------------------------------------------

    style: str = "default"

    role: str = "default"

    gender: str = "neutral"

    provider: str = "edge"

    # -------------------------------------------------

    @property
    def is_english(self) -> bool:
        """
        Retorna True caso seja um perfil em inglês.
        """

        return self.language.lower().startswith("en")

    # -------------------------------------------------

    @property
    def is_portuguese(self) -> bool:
        """
        Retorna True caso seja um perfil em português.
        """

        return self.language.lower().startswith("pt")

    # -------------------------------------------------

    def to_dict(self) -> dict:
        """
        Serializa o perfil.
        """

        return {

            "profile_id": self.profile_id,

            "name": self.name,

            "description": self.description,

            "language": self.language,

            "locale": self.locale,

            "voice": self.voice,

            "rate": self.rate,

            "pitch": self.pitch,

            "volume": self.volume,

            "style": self.style,

            "role": self.role,

            "gender": self.gender,

            "provider": self.provider

        }

    # -------------------------------------------------

    def __str__(self) -> str:
        """
        Representação amigável.
        """

        return (
            f"{self.name} "
            f"[{self.voice}] "
            f"({self.language})"
        )