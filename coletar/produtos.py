import bs4  # importa a biblioteca BeautifulSoup para análise e extração de dados do HTML

def listar_produtos() -> list:
    """
    Ler um arquivo HTML e extrair dados estruturados (nome, nota e valor) dos produtos usando a biblioteca BeautifulSoup."""

    with open("page/revio-e-commerce.html") as html_pagina: 
        soup = bs4.BeautifulSoup(html_pagina, "html.parser") 
        '''
        Abre e lê o arquivo HTML com segurança (fecha automaticamente após o bloco) e analisa o HTML com BeautifulSoup'''

    grid_de_produtos = soup.find("div", class_="products-grid")   
    '''
    Encontra a grid principal'''
    
    produtos = grid_de_produtos.find_all("div", class_="product-card")  
    ''' 
    Todos os produtos na página'''

    lista_produtos = []

    for produto in produtos:
        
        nome = produto.find("h3").text.strip()      
        '''
        Extrai o nome'''
        
        preco_tag = produto.find("span", class_="current-price")            
        preco_texto = preco_tag.text.strip().replace("R$", "").replace(".", "").replace(",", ".") if preco_tag else "0.0"
        preco = float(preco_texto)
        ''' 
        Extrai o preço atual (dentro da span com classe 'current-price')'''

        nota_tag = produto.find("span", class_="rating-value")       
        nota = float(nota_tag.text.strip()) if nota_tag else 0.0
        '''
        Extrai a nota (avaliação)'''

        lista_produtos.append({
            "nome": nome,                     
            "nota": nota,             
            "valor": preco
        })
        '''
        Cria um dicionário com as informações do produto (nome, nota e valor)  
        e adiciona esse dicionário à lista de produtos'''

    return lista_produtos
    
    '''
    produto 1 Geladeira Brastemp Inverse BRE80AK 573L Inox | R$ 2.804,15 | 4.0
    produto 2 Geladeira Consul Frost Free CRM55AK 437L Inox | R$ 2.199,00 | 5.0
    produto 3 Geladeira Samsung Side by Side RS27T5200S9 617L Inox Look | R$ 4.299,00 | 4.2
    produto 4 Geladeira Electrolux Frost Free TF55S 431L Prata | R$ 2.899,00 | 3.5
    produto 5 Geladeira LG French Door GR-X247CSZ 507L Inox | R$ 4.799,20 | 4.8
    produto 6 Geladeira Panasonic Econavi NR-BT50BD3X 435L Inox | R$ 3.199,00 | 3.8
    '''