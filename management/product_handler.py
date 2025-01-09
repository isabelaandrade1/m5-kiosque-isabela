from menu import products

def get_product_by_id(id):
    if type(id) != int:
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == id:
            return product
    return {}

def get_products_by_type(types):
    if type(types) != str:
        raise TypeError("product type must be a str")
    products_type = []
    for product in products:
        if product["type"] == types:
            products_type.append(product)
    return products_type

def menu_report():
    product_count = len(products)

    price = 0.00
    for product in products:
        price = price + product["price"]
    average_price = round((price/product_count), 2)

    most_common_type = ''
    fruit = 0
    vegetable = 0
    drink = 0
    dairy = 0
    bakery = 0

    for product in products:
        if product["type"] == 'fruit':
            fruit += 1
        elif product["type"] == 'vegetable':
            vegetable += 1
        elif product["type"] == 'drink':
            drink += 1
        elif product["type"] == 'dairy':
            dairy += 1
        elif product["type"] == 'bakery':
            bakery += 1

    if fruit > vegetable and fruit > drink and fruit > dairy and fruit > bakery:
        most_common_type = 'fruit'
    elif vegetable > drink and vegetable > dairy and vegetable > bakery: 
        most_common_type = 'vegetable'
    elif drink > dairy and drink > bakery:
        most_common_type = 'drink'
    elif dairy > bakery:
        most_common_type = 'dairy'
    else:
        most_common_type = 'bakery'

    return f'Products Count: {product_count} - Average Price: {average_price} - Most Common Type: {most_common_type}'

def add_product(menu, **args):
    id_products_menu = 1
    if len(menu) > 0:
        for product in menu:
            if product["_id"] >= id_products_menu:
                id_products_menu = product["_id"] + 1
    
    args["_id"] = id_products_menu
    menu.append(args)

    return args
