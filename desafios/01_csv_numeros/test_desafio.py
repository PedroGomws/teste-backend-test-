from desafio import limpar_csv_numeros


def test_limpar_csv_numeros():
    # Caso básico: vírgula decimal vira ponto
    assert limpar_csv_numeros("produto;10,50;2") == "produto;10.50;2"

    # Vários campos numéricos
    assert limpar_csv_numeros("Teclado;100,00;2;Mouse;50,5;1") == (
        "Teclado;100.00;2;Mouse;50.5;1"
    )

    # Sem vírgulas: linha permanece igual
    assert limpar_csv_numeros("ok;123;abc") == "ok;123;abc"

    # Delimitador ';' não pode ser alterado
    resultado = limpar_csv_numeros("a;1,5;b;2,0")
    assert resultado.count(";") == 3
    assert "," not in resultado
