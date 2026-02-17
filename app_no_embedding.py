from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


# carregar variáveis de ambiente
load_dotenv()

API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")


# Definir modelo llm
llm = ChatGoogleGenerativeAI(model="gemini-flash-lite-latest", temperature=0, google_api_key=API_KEY_GOOGLE)


# criar variáveis prompt teamplate e pergunta
pergunta = "Qual é a política de home office da nossa empresa?"

prompt_template = ChatPromptTemplate.from_template("Responda essa pergunta: {pergunta}")


# criar cadeia da langchain
chain = prompt_template | llm


# invokar resposta
resposta = chain.invoke({"pergunta": pergunta})


# Exibir resposta
print(resposta.content)