# Teste 6 — Senha forte

**Função:** `senha_forte(senha)`

Verifica se uma senha atende aos critérios mínimos de segurança. Regras:

- Deve ter pelo menos 8 caracteres
- Deve conter pelo menos uma letra maiúscula
- Deve conter pelo menos uma letra minúscula
- Deve conter pelo menos um número

Retorna `True` ou `False`.

```python
senha_forte("SenhaForte123")  # True
senha_forte("senha123")       # False (sem maiúscula)
senha_forte("SENHA123")       # False (sem minúscula)
senha_forte("SenhaForte")     # False (sem número)
senha_forte("Sen12")          # False (menos de 8 caracteres)
```

Implemente em `desafio.py`.
