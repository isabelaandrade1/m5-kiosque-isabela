from management.product_handler import get_product_by_id, get_products_by_type, add_product
from management.tab_handler import calculate_tab
from menu import products  # Corrigido: importar 'products' em vez de 'menu'

if __name__ == "__main__":
    # Testando get_product_by_id com ID válido
    print(get_product_by_id(28))  # Deve retornar o produto com ID 28

    # Testando get_products_by_type
    print(get_products_by_type('drink'))  # Deve retornar todos os produtos do tipo 'drink'

    # Testando add_product
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduíche de Python",
        "type": "fast-food",
    }
    print(add_product(products, **new_product))  # Deve retornar o produto com o _id gerado

    # Testando add_product com menu vazio
    print(add_product([], **new_product))  # Deve gerar _id 1

    # Testando calculate_tab
    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [{"_id": 10, "amount": 3}, {"_id": 20, "amount": 2}, {"_id": 21, "amount": 5}]

    print(calculate_tab(table_1))  # Deve retornar {'subtotal': '$216.1'}
    print(calculate_tab(table_2))  # Deve retornar {'subtotal': '$188.29'}

    # Testando get_product_by_id com outro ID válido
    print(get_product_by_id(1))  # Deve retornar o produto com ID 1
