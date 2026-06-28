import asyncio
import edge_tts


VOICE = "en-US-GuyNeural"
INPUT_FILE = "test.ssml"
OUTPUT_FILE = "test.mp3"


async def main():

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        ssml = f.read()

    communicate = edge_tts.Communicate(
        ssml,
        voice=VOICE
    )

    await communicate.save(OUTPUT_FILE)

    print("Audio generated:", OUTPUT_FILE)


if __name__ == "__main__":
    asyncio.run(main())