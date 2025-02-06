# See: https://api-docs.deepseek.com/
from openai import OpenAI
import os

# Get API key from envrionment variable DEEPSEEK_API_KEY
api_key = os.getenv("DEEPSEEK_API_KEY")
base_url = "https://api.deepseek.com"

client = OpenAI(api_key=api_key, base_url=base_url)

messages=[
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello"},
]

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=messages,
    stream=False
)

print(response.choices[0].message.content)