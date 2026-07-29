def limpar_csv_numeros(linha):
    partes = linha.split(";")

    for i in range(len(partes)):
        if "," in partes[i]:
            partes[i] = partes[i].replace(",", ".")

    resultado = ";".join(partes)
    return resultado
