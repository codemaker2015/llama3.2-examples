import requests
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-11B-Vision-Instruct"
headers = {"Authorization": "Bearer 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"}
def query(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
# Example usage
prompt = "What is the importance of black holes in classical physics"
result = query(prompt)
print(result)