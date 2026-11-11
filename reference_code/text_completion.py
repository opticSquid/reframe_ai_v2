from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-hf", dtype="auto", device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
model_inputs = tokenizer(
    ["The secret to baking a good cake is "], return_tensors="pt"
).to(model.device)
generated_ids = model.generate(**model_inputs, max_length=30)
output_tokens = tokenizer.batch_decode(generated_ids)[0]
print(output_tokens)
