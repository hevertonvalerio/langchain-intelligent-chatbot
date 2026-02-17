from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


# carregar variáveis de ambiente
load_dotenv()

API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")


def processo():
    print("\nIniciando Intelligent Chatbot...\n")

    def selecao_processos():
        print("Seleção de Processos:")
        print("1 - Faiss App")
        print("2 - Chroma App")
        print("3 - Pinecone App")
        selecao = input("Digite o número do app que deseja utilizar: ")
        return selecao
    selecao = selecao_processos()

    def executar_processo(selecao):
        if selecao == "1":
            import app_faiss
        elif selecao == "2":
            import app_chroma
        elif selecao == "3":    
            import app_pinecone
        else:    
            print("Opção inválida. Encerrando o programa.")
            return False
        return True
    executar_processo(selecao)
processo()