"""
=============================================================
 Speech AI Narrator
-------------------------------------------------------------
Configuration File
=============================================================

Centraliza todas as configurações do projeto.

Alterando este arquivo, todo o projeto utilizará os novos
parâmetros automaticamente.

Author : Rodrigo Magalhães
Version: 1.0.0
"""

from pathlib import Path

# ============================================================
# PROJECT
# ============================================================

PROJECT_NAME = "Speech AI Narrator"
VERSION = "1.0.0"

# ============================================================
# DIRECTORIES
# ============================================================

BASE_DIR = Path(__file__).parent.resolve()

INPUT_DIR = BASE_DIR

OUTPUT_DIR = BASE_DIR / "output"

LOG_DIR = BASE_DIR / "logs"

TEMP_DIR = OUTPUT_DIR / "temp"

# Cria diretórios automaticamente
for folder in (
    OUTPUT_DIR,
    LOG_DIR,
    TEMP_DIR
):
    folder.mkdir(parents=True, exist_ok=True)

# ============================================================
# FILES
# ============================================================

SCRIPT_FILE = INPUT_DIR / "script.txt"

OPTIMIZED_SCRIPT_FILE = OUTPUT_DIR / "script_optimized.txt"

SSML_FILE = OUTPUT_DIR / "script.ssml"

REPORT_FILE = OUTPUT_DIR / "speech_report.json"

AUDIO_FILE = OUTPUT_DIR / "audio.mp3"

LOG_FILE = LOG_DIR / "speech.log"

# ============================================================
# MICROSOFT EDGE TTS
# ============================================================

VOICE = "en-US-ChristopherNeural"

RATE = "+0%"

PITCH = "+0Hz"

VOLUME = "+0%"

# ============================================================
# PRESENTATION
# ============================================================

TARGET_DURATION_MINUTES = 10

WORDS_PER_MINUTE = 145

# ============================================================
# HUMANIZATION
# ============================================================

DEFAULT_SHORT_PAUSE = 300

DEFAULT_MEDIUM_PAUSE = 600

DEFAULT_LONG_PAUSE = 1000

SLIDE_PAUSE = 1500

# ============================================================
# SPEECH OPTIMIZATION
# ============================================================

MAX_SENTENCE_WORDS = 28

MAX_PARAGRAPH_SENTENCES = 5

ENABLE_KEYWORD_EMPHASIS = True

ENABLE_SLIDE_DETECTION = True

ENABLE_LIST_OPTIMIZATION = True

ENABLE_REPORT = True

# ============================================================
# KEYWORDS
# ============================================================

KEYWORDS = [

    "AI",

    "Artificial Intelligence",

    "Governance",

    "Business",

    "Innovation",

    "Compliance",

    "Security",

    "Strategy",

    "Executive",

    "Technology",

    "Platform",

    "South America",

    "Committee",

    "Leadership",

    "Data",

    "Digital",

    "Transformation",

    "Automation",

    "Manufacturing",

    "Engineering"

]

# ============================================================
# LOGGING
# ============================================================

LOG_LEVEL = "INFO"

# ============================================================
# BANNER
# ============================================================

BANNER = f"""
====================================================
 {PROJECT_NAME}
 Version : {VERSION}
====================================================
"""