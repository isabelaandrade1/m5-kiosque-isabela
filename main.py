from management.product_handler import get_product_by_id, get_products_by_type

if __name__ == "__main__":
    # Teste da função get_product_by_id
    print(get_product_by_id(28))  # Deve exibir o produto com ID 28

    # Teste da função get_products_by_type
    print(get_products_by_type('drink'))  # Deve exibir todos os produtos do tipo 'drink'
