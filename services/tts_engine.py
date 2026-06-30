from pathlib import Path

from providers.base_provider import BaseTTSProvider


class TTSEngine:

    def __init__(

        self,

        provider: BaseTTSProvider

    ):

        self.provider = provider

    def generate(

        self,

        text: str,

        output_path: Path

    ) -> Path:

        return self.provider.generate(

            text=text,

            output_path=output_path

        )