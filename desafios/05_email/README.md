# Teste 5 — Validador de e-mail

**Função:** `email_valido(email)`

Sem expressões regulares. Regras:

- Não pode conter espaços
- Deve ter exatamente um `@`
- Deve ter pelo menos um `.`

Retorna `True` ou `False`.

```python
email_valido("estagiario@empresa.com")   # True
email_valido("estagiario@@empresa.com")  # False
email_valido("estagiario @ empresa.com") # False
```

Implemente em `desafio.py`.
