from fastapi import FastAPI
import sys
sys.path.append("..")
from exemplo.codigo_de_exemplo import listar_produtos

app = FastAPI()

@app.get("/listar_produtos")
def listar_produtos_e_commerce():

    """Lista todos os produtos encontrados na página de e-commerce"""
    
    lista_de_produtos = listar_produtos()
    resposta = dict(produtos=lista_de_produtos)
    return resposta

