import csv
from lib.dados import find


def import_from_csv(file_name, get_titles=True):
    path = "data/"
    dados = []

    with open(path + file_name, newline='') as csv_file:
        spam_reader = csv.reader(csv_file, delimiter='\t')
        for row in spam_reader:
            new_row = []
            for item in row:
                new_row.append(item)
            dados.append(new_row)

    if get_titles:
        titulos = dados[0]
        return titulos, dados[1:]

    return dados[1:]


def tratar_numeros(dados, indice):
    dados_tratados = []
    for row in dados:
        new_row = []
        for i, item in enumerate(row):
            item_tratado = item
            if i < indice:
                new_row.append(item_tratado)
            else:
                item_tratado = item_tratado.replace('%', '')
                item_tratado = item_tratado.replace('.', '')
                item_tratado = item_tratado.replace(',', '.')
                new_row.append(float(item_tratado))
        dados_tratados.append(new_row)

    return dados_tratados


def import_from_fundamentus(file_name):
    path = "data/"
    titulos = []
    dados = []
    with open(path + file_name, newline='') as csvFile:
        spamReader = csv.reader(csvFile, delimiter='\t')
        primeiraLinha = True
        for row in spamReader:
            if primeiraLinha:
                for titulo in row:
                    titulos.append(titulo)
                primeiraLinha = False
            else:
                newRow = []
                primeiroItem = True
                for item in row:
                    if primeiroItem:
                        newRow.append(item)
                        primeiroItem = False
                    else:
                        itemTratado = item
                        itemTratado = itemTratado.replace('%', '')
                        itemTratado = itemTratado.replace('.', '')
                        itemTratado = itemTratado.replace(',', '.')
                        newRow.append(float(itemTratado))
                dados.append(newRow)
    return titulos, dados


def print_dados_filtrando_itens(items, titulos, dados):
    for row in dados:
        for item in items:
            print(tamanho(str(row[find.index_of_item(item, titulos)])), end='')
        print()
    print()
    for item in items:
        print(tamanho(item), end='')


def tamanho(palavra, letras = 10, espaco = 2):
    if len(palavra) > letras:
        return palavra[0:letras] + espaco*' '
    return palavra + (espaco + (letras - len(palavra)))*' '
