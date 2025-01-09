from menu import products  # Corrigido: importar 'products' em vez de 'menu'

def get_product_by_id(product_id):
    """
    Retorna o dicionário de um produto pelo seu ID.
    Se não encontrar, retorna um dicionário vazio.
    """
    for product in products:
        if product["_id"] == product_id:
            return product
    return {}

def get_products_by_type(product_type):
    """
    Retorna uma lista de produtos de um determinado tipo.
    Se não encontrar, retorna uma lista vazia.
    """
    return [product for product in products if product["type"] == product_type]

def add_product(products, **new_product):
    """
    Adiciona um novo produto ao menu com um ID único.
    """
    # Calcula o novo ID
    if products:
        new_id = max(product["_id"] for product in products) + 1
    else:
        new_id = 1

    # Adiciona o ID ao novo produto
    new_product["_id"] = new_id

    # Adiciona o produto ao menu
    products.append(new_product)

    # Retorna o novo produto
    return new_product
