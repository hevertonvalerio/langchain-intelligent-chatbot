from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import Pinecone
from pinecone import Pinecone as PineconeClient
from pinecone import ServerlessSpec

import documento_empresa_exemplo as doc_empresa


# carregar variáveis de ambiente
load_dotenv()
API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")


# Definido variáveis
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", google_api_key=API_KEY_GOOGLE)
d = 3072
# index_hnsw = faiss.IndexHNSWFlat(d, 32)
index_name = "langchain-pinecone-db"
pinecone_client = PineconeClient(api_key=os.environ["PINECONE_API_KEY"])
spec = ServerlessSpec(cloud='aws', region='us-east-1')


# Instanciando Banco de Dados Pinecone
if index_name not in pinecone_client.list_indexes().names():
    pinecone_client.create_index(
        name=index_name, 
        dimension=d, 
        metric="cosine", 
        spec=spec)
    print(f"Banco de dados pinecone criado...{index_name}")

    # Criar base de dados a partir dos documentos da empresa
    db = Pinecone.from_documents(
        documents=doc_empresa.documentos_empresa, 
        embedding=embeddings, 
        index_name=index_name
        )
    print("Banco de dados Montado: PineconeDB")
else:
    print(f"Conectando banco de dados pinecone já existente...{index_name}")
    db = Pinecone.from_existing_index(
        index_name=index_name, 
        embedding=embeddings
    )



# Define pergunta e resposta para busca por similaridade
pergunta = "Como montar uma VPN?"
# pergunta = input("Digite sua pergunta: ")

# resposta = db.similarity_search(pergunta, k=3)
resposta = db.similarity_search("Como funciona?", k=3, filter={"$and": [{"departamento": "TI"}, {"tipo": "tutorial"}]})


# Apresentação
print(f"\n\nPergunta: {pergunta}\n")
for doc in resposta:
    print(f"Resposta: {doc.page_content}")
    print(f"Metadados: {doc.metadata}\n")


#print(resposta)
print(pinecone_client.list_indexes().names())