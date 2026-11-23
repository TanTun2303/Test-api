import os
from pathlib import Path

from openai import OpenAI

from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

api_key = os.getenv("key")
base_url = os.getenv("url")
if not api_key:
    raise RuntimeError("Missing key in .env")

c = OpenAI(base_url=base_url, api_key=api_key)
r = c.chat.completions.create(model="dusk-study", stream=True,
                              messages=[{"role": "user", "content": "hi"}])
for chunk in r:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()
