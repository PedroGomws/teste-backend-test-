from desafio import padronizar_nomes


def test_padronizar_nomes():
    nomes_sujos = [" joão silva ", "MARIA SOUZA", "ana", "   pedro   "]

    resultado = padronizar_nomes(nomes_sujos)

    assert resultado == ["João Silva", "Maria Souza", "Ana", "Pedro"]
