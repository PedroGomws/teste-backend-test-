def filtrar_usuarios_ativos(usuarios):
    nomes = []

    for usuario in usuarios:
        if usuario["ativo"]:
            nomes.append(usuario["nome"])

    return nomes
