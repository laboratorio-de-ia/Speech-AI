import asyncio
from pathlib import Path
import edge_tts


class TTSEngine:

    def __init__(self):
        self.voice = "en-US-GuyNeural"
        self.rate = "-25%"

    async def _run(self, ssml: str, output_path: str):

        communicate = edge_tts.Communicate(
            ssml,
            voice=self.voice,
            rate=self.rate
        )

        await communicate.save(output_path)

    def generate(self, ssml_path: str, output_path: str):

        ssml_path = Path(ssml_path)

        ssml = ssml_path.read_text(encoding="utf-8")

        asyncio.run(
            self._run(ssml, output_path)
        )