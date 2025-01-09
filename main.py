from management.product_handler import get_product_by_id, get_products_by_type, menu_report, add_product, add_product_extra
from menu import products

if __name__ == "__main__":
    # Teste das funções
    print(get_product_by_id(28))  # Produto com ID 28
    print(get_products_by_type("drink"))  # Produtos do tipo "drink"
    print(menu_report())  # Relatório do menu

    # Adicionando um produto
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduíche de Python",
        "type": "fast-food"
    }
    print(add_product(products, **new_product))

    # Adicionando um produto com verificações extras
    required_keys = ("title", "price", "rating", "description", "type")
    print(add_product_extra(products, *required_keys, **new_product))
