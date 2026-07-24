# Teste 1 — Limpeza de CSV numérico

**Função:** `limpar_csv_numeros(linha)`

Em planilhas brasileiras, números usam vírgula como decimal (`10,50`). Em sistemas internacionais, o padrão é ponto (`10.50`).

Receba uma linha CSV delimitada por `;` e retorne a mesma linha com as vírgulas dos números convertidas em pontos. O delimitador `;` **não** deve ser alterado.

```python
limpar_csv_numeros("produto;10,50;2")
# -> "produto;10.50;2"
```

Implemente em `desafio.py`.
