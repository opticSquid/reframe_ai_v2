from pathlib import Path
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from accelerate import Accelerator

PROJECT_ROOT = Path(__file__).resolve().parents[2]
AUDIO_FILE = PROJECT_ROOT / "data" / "punjay_audio.mp3"
MODEL_ID = "openai/whisper-large-v3"
TORCH_DTYPE = torch.float32

device = Accelerator().device

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    MODEL_ID, dtype=TORCH_DTYPE, low_cpu_mem_usage=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(MODEL_ID)

pipeline = pipeline(
    "automatic-speech-recognition",
    model=MODEL_ID,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    chunk_length_s=30,
    dtype=TORCH_DTYPE,
    device=device,
)
# pipeline = pipeline(
#     "automatic-speech-recognition", model="openai/whisper-tiny", device=device
# )
result = pipeline(
    str(AUDIO_FILE),
    return_timestamps=True,
    generate_kwargs=[{"language": "english"}, {"task": "translate"}],
)
print(result["chunks"])
