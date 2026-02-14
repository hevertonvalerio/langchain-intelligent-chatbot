import google.generativeai as genai
import os
from dotenv import load_dotenv
# import google.genai as genai

load_dotenv()

genai.configure(api_key=os.environ["API_KEY_GOOGLE"])


print("Modelos de embeddings disponíveis:")
for m in genai.list_models():
    if "embedContent" in m.supported_generation_methods:
        print(m.name)
