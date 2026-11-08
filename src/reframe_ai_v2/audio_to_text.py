from pathlib import Path
from transformers import pipeline
from accelerate import Accelerator

PROJECT_ROOT = Path(__file__).resolve().parents[2]
AUDIO_FILE = PROJECT_ROOT / "data" / "punjay_audio.mp3"
# MODEL_ID = "openai/whisper-large-v3"
MODEL_ID = "openai/whisper-tiny"

device = Accelerator().device

pipeline = pipeline(
    "automatic-speech-recognition",
    model=MODEL_ID,
    chunk_length_s=30,
    device=device,
)
result = pipeline(str(AUDIO_FILE), batch_size=8, language="en", return_timestamps=True)
print(result["chunks"])
