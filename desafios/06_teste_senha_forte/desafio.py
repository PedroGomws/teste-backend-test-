def senha_forte(senha):

    if len(senha) < 8:
        return False
    maiuscula = False
    minuscula = False
    numero = False

    for caractere in senha:
        if caractere.isupper():
            maiuscula = True
        if caractere.islower():
            minuscula = True
        if caractere.isdigit():
            numero = True

    return maiuscula and minuscula and numero
