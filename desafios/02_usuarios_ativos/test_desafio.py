from desafio import filtrar_usuarios_ativos


def test_filtrar_usuarios_ativos():
    usuarios = [
        {"nome": "Alice", "ativo": True},
        {"nome": "Bob", "ativo": False},
        {"nome": "Carlos", "ativo": True},
    ]

    resultado = filtrar_usuarios_ativos(usuarios)

    # Deve retornar apenas uma lista de strings com os nomes
    assert resultado == ["Alice", "Carlos"]

    # Edge case: lista sem nenhum ativo
    usuarios_inativos = [{"nome": "Ana", "ativo": False}]
    assert filtrar_usuarios_ativos(usuarios_inativos) == []
