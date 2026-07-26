from desafio import senha_forte


def test_senha_forte():
    # Casos de sucesso
    assert senha_forte("SenhaForte123") is True

    # Casos de falha
    assert senha_forte("senha123") is False  # Sem maiúscula
    assert senha_forte("SENHA123") is False  # Sem minúscula
    assert senha_forte("SenhaForte") is False  # Sem número
    assert senha_forte("Sen12") is False  # Menos de 8 caracteres
