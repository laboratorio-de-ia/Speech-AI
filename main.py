"""
====================================================
 Speech AI - Pipeline (FINAL FIXED VERSION)
====================================================
"""

import logging
from pathlib import Path

from core.text_analyzer import TextAnalyzer
from core.narration_builder import NarrationBuilder
from core.ssml_builder import SSMLBuilder
from core.tts_engine import TTSEngine


# ====================================================
# PATH ROOT
# ====================================================

PROJECT_ROOT = Path(__file__).resolve().parent


# ====================================================
# LOG CONFIG
# ====================================================

logging.basicConfig(
    filename=PROJECT_ROOT / "logs" / "app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


# ====================================================
# PIPELINE
# ====================================================

def run_pipeline():
    print("\n====================================================")
    print(" Speech AI - Pipeline (FIXED SSML VERSION)")
    print("====================================================\n")

    logger.info("Pipeline started")

    try:
        # =================================================
        # 1. TEXT ANALYZER
        # =================================================
        analyzer = TextAnalyzer()
        presentation = analyzer.run()

        # =================================================
        # 2. NARRATION BUILDER (TEXT LIMPO - SEM TAGS)
        # =================================================
        narrator = NarrationBuilder()
        narrator.load(presentation)

        narration_blocks = narrator.build()

        narration_file = PROJECT_ROOT / "output" / "narration.txt"
        narrator.export_text(str(narration_file))

        # DEBUG OPCIONAL (útil se ainda houver problema)
        # print("\n===== NARRATION DEBUG =====")
        # print("\n".join(narration_blocks))

        # =================================================
        # 3. SSML BUILDER (ÚNICO LUGAR COM TAGS)
        # =================================================
        ssml_builder = SSMLBuilder()
        ssml_builder.load(presentation)

        ssml_output = ssml_builder.build()

        ssml_file = PROJECT_ROOT / "output" / "speech.xml"
        ssml_builder.export(str(ssml_file))

        # DEBUG CRÍTICO (recomendado manter enquanto testa)
        print("\n===== SSML DEBUG =====\n")
        print(ssml_output[:2000])  # evita spam no terminal
        print("\n======================\n")

        # =================================================
        # 4. TTS ENGINE (GERAÇÃO DE ÁUDIO)
        # =================================================
        tts = TTSEngine()

        audio_file = PROJECT_ROOT / "output" / "Audio_Governance_SouthAmerica.mp3"

        tts.generate(
            ssml_path=str(ssml_file),
            output_path=str(audio_file)
        )

        # =================================================
        # 5. SUMMARY
        # =================================================
        print("\n================ RESULT =================\n")

        print(f"Slides: {presentation.total_slides()}")
        print(f"Narration Blocks: {len(narration_blocks)}")
        print(f"Words: {presentation.statistics.words}")
        print(f"Estimated Duration: {presentation.statistics.estimated_minutes} min")

        print("\n--- OUTPUT FILES ---")
        print(f"Narration: {narration_file}")
        print(f"SSML: {ssml_file}")
        print(f"Audio: {audio_file}")

        print("\n==========================================\n")

        logger.info("Pipeline completed successfully")

    except Exception as e:
        logger.error(f"Pipeline error: {e}")
        print(f"ERROR: {e}")


# ====================================================
# ENTRY POINT
# ====================================================

if __name__ == "__main__":
    run_pipeline()