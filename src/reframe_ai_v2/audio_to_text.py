from transformers import pipeline
from accelerate import Accelerator

device = Accelerator().device

pipeline = pipeline(
    "automatic-speech-recognition", model="openai/whisper-large-v3", device=device
)
output_tokens = pipeline("../../data/punjay_audio.mp3", return_timestamps=True)
print(output_tokens)
