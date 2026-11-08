from pathlib import Path
from transformers import pipeline
from accelerate import Accelerator

PROJECT_ROOT = Path(__file__).resolve().parents[2]
AUDIO_FILE = PROJECT_ROOT / "data" / "punjay_audio.mp3"

device = Accelerator().device


pipeline = pipeline(
    "automatic-speech-recognition", model="openai/whisper-large-v3", device=device
)
output_tokens = pipeline(str(AUDIO_FILE), return_timestamps=True, language="en")
print(output_tokens)
