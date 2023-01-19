import os
import openai
from dotenv import load_dotenv
load_dotenv()

MODEL = 'text-davinci-003'
MAX_TOKENS = 3_000

prompts = [
    """
Create a SVG 100px by 100px icon of a skull wearing a pirate hat.
    """
]

openai.api_key = os.getenv("OPENAI_API_KEY")

for prompt in prompts:
    try: 
        result = openai.Completion.create(
                model=MODEL,
                prompt=prompt,
                temperature=0.5,
                max_tokens=MAX_TOKENS,
                frequency_penalty=0,
                presence_penalty=0)
        
        if result and result.get('choices'):
            answer = result.get('choices').pop()
            text = answer.get('text')
            print(text)
    except Exception as e:
        print('=============================')
        print(e)
        print(prompt)
        print('=============================')

