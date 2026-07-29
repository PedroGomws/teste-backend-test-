def calcular_total_carrinho(carrinho):
    total = 0
    for item in carrinho:
        total += item["preco"] * item["quantidade"]

    return total
