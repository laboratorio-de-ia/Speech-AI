"""
=========================================================
Voice Manager
---------------------------------------------------------
Speech AI Platform

Responsável por carregar e disponibilizar os perfis de voz
configurados em voices.json.

Esta classe é a única responsável por conhecer a estrutura
do arquivo de configuração.

Author: Rodrigo Magalhães
=========================================================
"""

import json
from pathlib import Path

from models.voice_profile import VoiceProfile


class VoiceManager:
    """
    Gerencia os perfis de voz da aplicação.
    """

    # -------------------------------------------------

    def __init__(self, voices_file: Path):

        self.voices_file = Path(voices_file)

        if not self.voices_file.exists():

            raise FileNotFoundError(
                f"Voice configuration not found:\n{self.voices_file}"
            )

        with open(
            self.voices_file,
            "r",
            encoding="utf-8"
        ) as file:

            self._config = json.load(file)

    # -------------------------------------------------

    @property
    def default_profile(self) -> str:
        """
        Retorna o profile padrão.
        """

        return self._config["default_profile"]

    # -------------------------------------------------

    def exists(
        self,
        profile_id: str
    ) -> bool:
        """
        Verifica se o perfil existe.
        """

        return profile_id in self._config["profiles"]

    # -------------------------------------------------

    def list_profiles(self) -> list[str]:
        """
        Lista todos os perfis disponíveis.
        """

        return sorted(
            self._config["profiles"].keys()
        )

    # -------------------------------------------------

    def get(
        self,
        profile_id: str | None = None
    ) -> VoiceProfile:
        """
        Retorna um VoiceProfile.
        """

        if profile_id is None:

            profile_id = self.default_profile

        if not self.exists(profile_id):

            raise ValueError(
                f"Voice profile '{profile_id}' not found."
            )

        profile = self._config["profiles"][profile_id]

        return VoiceProfile(

            profile_id=profile_id,

            name=profile["name"],

            description=profile["description"],

            language=profile["language"],

            locale=profile["locale"],

            voice=profile["voice"],

            rate=profile["rate"],

            pitch=profile["pitch"],

            volume=profile["volume"],

            style=profile.get(
                "style",
                "default"
            ),

            role=profile.get(
                "role",
                "default"
            ),

            gender=profile.get(
                "gender",
                "neutral"
            ),

            provider=profile.get(
                "provider",
                "edge"
            )

        )

    # -------------------------------------------------

    def __len__(self) -> int:
        """
        Quantidade de perfis cadastrados.
        """

        return len(
            self._config["profiles"]
        )