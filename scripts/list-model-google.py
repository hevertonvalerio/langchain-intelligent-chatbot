from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.environ["API_KEY_GOOGLE"])

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)