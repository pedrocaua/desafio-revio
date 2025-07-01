import bs4

def listar_produtos() -> list:
    """Extrai nome, nota e valor dos produtos do HTML com base nas classes reais."""

    with open("page/revio-e-commerce.html", encoding="utf-8") as html_pagina:
        soup = bs4.BeautifulSoup(html_pagina, "html.parser")

    grid_de_produtos = soup.find("div", class_="products-grid")  # Encontra a grid principal
    produtos = grid_de_produtos.find_all("div", class_="product-card")  # Todos os produtos na página

    lista_produtos = []

    for produto in produtos:
        # Extrai o nome
        nome = produto.find("h3").text.strip()

        # Extrai o preço atual (dentro da span com classe 'current-price')
        preco_tag = produto.find("span", class_="current-price")
        preco_texto = preco_tag.text.strip().replace("R$", "").replace(".", "").replace(",", ".") if preco_tag else "0.0"
        preco = float(preco_texto)

        # Extrai a nota (valor numérico da avaliação)
        nota_tag = produto.find("span", class_="rating-value")
        nota = float(nota_tag.text.strip()) if nota_tag else 0.0

        # Monta o dicionário do produto
        lista_produtos.append({
            "nome": nome,
            "nota": nota,
            "valor": preco
        })

    return lista_produtos






    """Método de exemplo para interção com o html da página do e-commerce

    html_pagina = open("page/revio-e-commerce.html")    # Carrega o arquivo html
    soup = bs4.BeautifulSoup(html_pagina, "html.parser")    #Parsea o arquivo
    grid_de_produtos = soup.find("div", class_="products-grid")    #Captura o grid html com todos os produtos
    produtos = grid_de_produtos.find_all("div", attrs={"class":"product-card"})    #Cria uma lista apenas com html específico dos produtos
    nomes_de_produtos = [produto.find("h3").text for produto in produtos]    #Cria uma lista apenas com o atributo do nome dos produtos

    return nomes_de_produtos
    
if __name__ == "__main__":
    resultado = listar_produtos()
    print(resultado)"""

    '''
    produto 1 Geladeira Brastemp Inverse BRE80AK 573L Inox R$ 2.804,15 4.0
    produto 2 Geladeira Consul Frost Free CRM55AK 437L Inox R$ 2.199,00 5.0
    produto 3 Geladeira Samsung Side by Side RS27T5200S9 617L Inox Look R$ 4.299,00 4.2
    produto 4 Geladeira Electrolux Frost Free TF55S 431L Prata R$ 2.899,00 3.5
    produto 5 Geladeira LG French Door GR-X247CSZ 507L Inox R$ 4.799,20 4.8
    produto 6 Geladeira Panasonic Econavi NR-BT50BD3X 435L Inox R$ 3.199,00 3.8
    '''