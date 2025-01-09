from menu import products
from collections import Counter


def get_product_by_id(product_id):
    """
    Retorna o dicionário de um produto pelo seu ID.
    Se não encontrar, retorna um dicionário vazio.
    """
    if not isinstance(product_id, int):
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == product_id:
            return product
    return {}


def get_products_by_type(product_type):
    """
    Retorna uma lista de produtos de um determinado tipo.
    Se não encontrar, retorna uma lista vazia.
    """
    if not isinstance(product_type, str):
        raise TypeError("product type must be a str")

    return [product for product in products if product["type"] == product_type]


def menu_report():
    """
    Retorna um relatório sobre o menu de produtos.
    """
    product_count = len(products)
    average_price = round(sum(product["price"] for product in products) / product_count, 2)
    most_common_type = Counter(product["type"] for product in products).most_common(1)[0][0]

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"


def add_product(menu, **new_product):
    """
    Adiciona um novo produto ao menu.
    """
    # Gera um novo ID com base no maior ID existente ou define como 1 para um menu vazio
    if menu:
        new_id = max(product["_id"] for product in menu) + 1
    else:
        new_id = 1

    # Adiciona o novo ID ao produto
    new_product["_id"] = new_id

    # Adiciona o produto ao menu
    menu.append(new_product)

    # Retorna o produto adicionado
    return new_product


def add_product_extra(menu, *required_keys, **new_product):
    """
    Adiciona um novo produto ao menu com verificações extras.
    """
    # Verifica se todas as chaves obrigatórias estão presentes
    for key in required_keys:
        if key not in new_product:
            raise KeyError(f"field {key} is required")

    # Remove chaves extras
    filtered_product = {key: new_product[key] for key in required_keys}

    # Gera o novo ID
    if menu:
        new_id = max(product["_id"] for product in menu) + 1
    else:
        new_id = 1
    filtered_product["_id"] = new_id

    # Adiciona o produto ao menu
    menu.append(filtered_product)

    return filtered_product
 