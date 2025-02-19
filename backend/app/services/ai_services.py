import openai
from ..config import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_contract(prompt: str):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000
    )
    return response.choices[0].text.strip()
