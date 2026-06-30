"""
=========================================================
Config Manager
---------------------------------------------------------
Centraliza o carregamento das configurações do projeto.

Author: Rodrigo Magalhães
=========================================================
"""

import json
from pathlib import Path


class ConfigManager:

    def __init__(self):

        self.project_root = Path(__file__).resolve().parent.parent

        self.config_file = self.project_root / "config" / "settings.json"

        self.data = {}

        self.load()

    # -----------------------------------------------------

    def load(self):

        if not self.config_file.exists():
            raise FileNotFoundError(
                f"Configuration file not found:\n{self.config_file}"
            )

        with open(self.config_file, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    # -----------------------------------------------------

    def reload(self):
        self.load()

    # -----------------------------------------------------

    def get(self, section, key=None):

        if key is None:
            return self.data.get(section)

        return self.data.get(section, {}).get(key)

    # -----------------------------------------------------

    @property
    def voice(self):
        return self.get("tts", "voice")

    @property
    def language(self):
        return self.get("tts", "language")

    @property
    def rate(self):
        return self.get("tts", "rate")

    @property
    def volume(self):
        return self.get("tts", "volume")

    @property
    def pitch(self):
        return self.get("tts", "pitch")

    # -----------------------------------------------------

    @property
    def output_directory(self):
        return self.get("output", "directory")

    @property
    def output_filename(self):
        return self.get("output", "filename")

    # -----------------------------------------------------

    @property
    def pause_short(self):
        return self.get("speech", "pause_short")

    @property
    def pause_long(self):
        return self.get("speech", "pause_long")

    @property
    def split_sentences(self):
        return self.get("speech", "split_long_sentences")

    # -----------------------------------------------------

    @property
    def project_name(self):
        return self.get("project", "name")

    @property
    def project_version(self):
        return self.get("project", "version")
    
    @property
    def script_file(self):
        return self.get("input", "script_file")


    @property
    def words_per_minute(self):
        return 145
    
    @property
    def provider(self):
        return self.get("tts", "provider")

    # -----------------------------------------------------

    def show(self):

        print()

        print("=" * 55)
        print(" Configuration")
        print("=" * 55)

        print(f"Project........: {self.project_name}")
        print(f"Version........: {self.project_version}")

        print()

        print(f"Language.......: {self.language}")
        print(f"Voice..........: {self.voice}")
        print(f"Rate...........: {self.rate}")
        print(f"Volume.........: {self.volume}")
        print(f"Pitch..........: {self.pitch}")

        print()

        print(f"Output Folder..: {self.output_directory}")
        print(f"Output File....: {self.output_filename}")

        print("=" * 55)