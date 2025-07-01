from fastapi import FastAPI, Query
import sys
sys.path.append("..")
from coletar.produtos import listar_produtos

app = FastAPI()

@app.get("/listar_produtos")
def listar_produtos_e_commerce():

    """Lista e filtrar os produtos encontrados na página de e-commerce """
    
    lista_de_produtos = listar_produtos()
    resposta = dict(produtos=lista_de_produtos)
    return resposta

@app.get("/buscar_por_nome")
def buscar_por_nome(nome: str):
    produtos = listar_produtos()
    resultado = [p for p in produtos if nome.lower() in p["nome"].lower()]
    return {"resultado": resultado}
    """obs
    Busca produtos cujo nome contenha o texto informado (case-insensitive).
    Parâmetro:
    - nome: string a ser buscada no nome do produto
    Retorna:
    - lista de produtos que contenham o texto no nome"""

@app.get("/buscar_por_preco")
def buscar_por_preco(min: float = Query(0), max: float = Query(9999999)):
    produtos = listar_produtos()
    resultado = [p for p in produtos if min <= p["valor"] <= max]
    return {"resultado": resultado}
    """obs
    Busca produtos cujo valor esteja dentro do intervalo informado.
    Parâmetros:
    - min: valor mínimo (inclusivo)
    - max: valor máximo (inclusivo)
    Retorna:
    - lista de produtos que estejam dentro do intervalo de preço"""

@app.get("/buscar_por_nota")
def buscar_por_nota(min: float = Query(0), max: float = Query(5)):
    
    produtos = listar_produtos()
    resultado = [p for p in produtos if min <= p["nota"] <= max]
    return {"resultado": resultado}
    """obs
    Busca produtos cuja nota esteja dentro do intervalo informado.
    Parâmetros:
    - min: nota mínima (inclusivo)
    - max: nota máxima (inclusivo)
    Retorna:
    - lista de produtos que estejam dentro do intervalo de nota"""