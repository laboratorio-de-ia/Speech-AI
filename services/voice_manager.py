"""
=========================================================
Voice Manager
---------------------------------------------------------
Speech AI Platform

Centraliza o gerenciamento dos perfis de voz
disponíveis na plataforma.

Author: Rodrigo Magalhães
=========================================================
"""

from __future__ import annotations

import json
from pathlib import Path

from models import VoiceProfile


class VoiceManager:

    # -------------------------------------------------

    def __init__(
        self,
        voices_file: str | Path
    ):

        self.voices_file = Path(voices_file)

        self._profiles: dict[str, VoiceProfile] = {}

        self._defaults: dict[str, str] = {}

        self.load()

    # -------------------------------------------------

    def load(self):

        if not self.voices_file.exists():

            raise FileNotFoundError(self.voices_file)

        with open(
            self.voices_file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        self._profiles.clear()

        self._defaults = data.get(
            "defaults",
            {}
        )

        for profile_id, item in data["profiles"].items():

            profile = VoiceProfile(

                profile_id=profile_id,

                **item

            )

            self._profiles[profile_id] = profile

    # -------------------------------------------------

    def reload(self):

        self.load()

    # -------------------------------------------------

    def get(
        self,
        profile_id: str
    ) -> VoiceProfile:

        return self._profiles[profile_id]

    # -------------------------------------------------

    def exists(
        self,
        profile_id: str
    ) -> bool:

        return profile_id in self._profiles

    # -------------------------------------------------

    def list(self):

        return list(
            self._profiles.values()
        )

    # -------------------------------------------------

    def list_languages(self):

        return sorted({

            profile.language

            for profile in self._profiles.values()

        })

    # -------------------------------------------------

    def list_providers(self):

        return sorted({

            profile.provider

            for profile in self._profiles.values()

        })

    # -------------------------------------------------

    def get_default_by_language(

        self,

        language: str,

        provider: str | None = None

    ) -> VoiceProfile | None:

        profile_id = self._defaults.get(language)

        if profile_id is None:

            return None

        profile = self._profiles.get(profile_id)

        if profile is None:

            return None

        if provider is not None:

            if profile.provider != provider:

                return None

        return profile

    # -------------------------------------------------

    def get_by_provider(

        self,

        provider: str

    ):

        return [

            profile

            for profile in self._profiles.values()

            if profile.provider == provider

        ]

    # -------------------------------------------------

    def get_by_voice(

        self,

        voice: str

    ) -> VoiceProfile | None:

        for profile in self._profiles.values():

            if profile.voice == voice:

                return profile

        return None

    # -------------------------------------------------

    def search(

        self,

        text: str

    ):

        text = text.lower()

        return [

            profile

            for profile in self._profiles.values()

            if (
                text in profile.name.lower()
                or text in profile.voice.lower()
                or text in profile.language.lower()
                or text in profile.locale.lower()
            )

        ]

    # -------------------------------------------------

    @property
    def statistics(self):

        return {

            "profiles": len(self._profiles),

            "languages": len(self.list_languages()),

            "providers": len(self.list_providers())

        }

    # -------------------------------------------------

    def __len__(self):

        return len(self._profiles)

    # -------------------------------------------------

    def __iter__(self):

        return iter(self._profiles.values())