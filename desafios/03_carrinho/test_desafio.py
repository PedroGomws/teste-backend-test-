from desafio import calcular_total_carrinho


def test_calcular_total_carrinho():
    carrinho = [
        {"item": "Teclado", "preco": 100.00, "quantidade": 2},
        {"item": "Mouse", "preco": 50.00, "quantidade": 1},
    ]

    resultado = calcular_total_carrinho(carrinho)

    # (100 * 2) + (50 * 1) = 250.00
    assert resultado == 250.00

    # Carrinho vazio deve custar 0
    assert calcular_total_carrinho([]) == 0.0
