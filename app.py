from transformers import pipeline
import torch

model_id = "meta-llama/Llama-3.2-1B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

# prompt = "Tell me a joke"
prompt = "What is the capital of India"
messages = [
    { "role": "system", "content": "You are a helpful assistant." },
    { "role": "user", "content": prompt },
]
outputs = pipe(
    messages,
    max_new_tokens=256,
)
response = outputs[0]["generated_text"][-1]["content"]
print(f"Input: {prompt}\nOutput: {response}")