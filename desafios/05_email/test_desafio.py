from desafio import email_valido


def test_email_valido():
    # Casos de sucesso
    assert email_valido("estagiario@empresa.com") is True
    assert email_valido("nome.sobrenome@teste.com.br") is True

    # Casos de falha
    assert email_valido("estagiarioempresa.com") is False  # Falta @
    assert email_valido("estagiario@empresa") is False  # Falta .
    assert email_valido("estagiario @ empresa.com") is False  # Tem espaço
    assert email_valido("estagiario@@empresa.com") is False  # Mais de um @
