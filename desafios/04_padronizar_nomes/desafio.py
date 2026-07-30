def padronizar_nomes(nomes_sujos):
    nomes_padronizados = []

    for nome in nomes_sujos:
        nomes_padronizados.append(nome.strip().title())

    return nomes_padronizados
