from menu import products  # Corrigido: importar 'products' em vez de 'menu'

def calculate_tab(consumptions):
    """
    Calcula o subtotal de uma mesa com base nos produtos consumidos.
    """
    subtotal = 0

    for item in consumptions:
        product = next((p for p in products if p["_id"] == item["_id"]), None)
        if product:
            subtotal += product["price"] * item["amount"]

    return {"subtotal": f"${round(subtotal, 2)}"}
