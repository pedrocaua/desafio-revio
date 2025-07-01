# 🚀 Desafio Revio

Projeto desenvolvido para o processo seletivo da Revio. 
O objetivo é realizar scraping de um HTML e disponibilizar os dados por uma API.

Funcionalidades
- /listar_produtos: retorna todos os produtos
- /buscar_por_nome: busca por nome
- /buscar_por_preco: filtra por preço
- /buscar_por_nota: filtra por avaliação

Tecnologias
- Python
- FastAPI
- BeautifulSoup
- Uvicorn

Como rodar ?
1. Clone o repositório
  2. Instale as dependências ->  pip install -r requirements.txt
    4. Execute a API -> uvicorn api.app:app --reload
      5. Acesse em http://127.0.0.1:8000/docs
