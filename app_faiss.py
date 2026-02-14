from dotenv import load_dotenv
import os
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

import documento_empresa_exemplo as doc_empresa


# carregar variáveis de ambiente
load_dotenv()
API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")


# Definido modelo de embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=API_KEY_GOOGLE)
d = 768
index_hnsw = FAISS.IndexHNSWFlat(d, 32)

# Criar base de dados a partir dos documentos da empresa
db = FAISS.from_documents(doc_empresa.documentos_empresa, embeddings)
print("Base de dados utilizada: FaissDB")


# Define pergunta e resposta para busca por similaridade
# pergunta = "Qual é a política de home office da nossa empresa?"
pergunta = input("Digite sua pergunta: ")

resposta = db.similarity_search(pergunta, k=3)


# Apresentação
print(f"\n\nPergunta: {pergunta}\n")
for i, (doc) in enumerate(resposta):
    print(f"Resposta {i+1}: {doc.page_content}")
    print(f"Metadados {i+1}: {doc.metadata}\n")