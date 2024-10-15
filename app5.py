from together import Together

client = Together(api_key="your-together-api-key")

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
    messages=[
        {
                "role": "user",
                "content": [
                        {
                                "type": "text",
                                "text": "Describe the image"
                        },
                        {
                                "type": "image_url",
                                "image_url": {
                                        "url": "s3://together-ai-uploaded-user-images-prod/f176fdd4-dcd1-4c73-b16b-4a2f124844a6.jpg"
                                }
                        }
                ]
        }
],
    max_tokens=512,
    temperature=0.7,
    top_p=0.7,
    top_k=50,
    repetition_penalty=1,
    stop=["<|eot_id|>","<|eom_id|>"],
    truncate=130560
)
print(response.choices[0].message.content)