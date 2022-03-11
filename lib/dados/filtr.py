from lib.dados import find
from lib.io import io


def greater_than(item, value, titulos, dados):
    filtered_fados = []
    col = find.index_of_item(item, titulos)
    for row in dados:
        if row[col] > value:
            filtered_fados.append(row)
    return filtered_fados


def less_than(item, value, titulos, dados):
    filtered_fados = []
    col = find.index_of_item(item, titulos)
    for row in dados:
        if row[col] < value:
            filtered_fados.append(row)
    return filtered_fados


def greater_or_equal_to(item, value, titulos, dados):
    filtered_fados = []
    col = find.index_of_item(item, titulos)
    for row in dados:
        if row[col] >= value:
            filtered_fados.append(row)
    return filtered_fados


def distinct(titulos, dados):
    titulos_permitidos = io.import_from_csv("filtro_distintos.csv", get_titles=False)

    papel = find.index_of_item("Papel", titulos)
    filtered_fados = []
    for i in range(len(dados)):
        permitido = True
        for j in range(len(titulos_permitidos)):
            if dados[i][papel][:4] == titulos_permitidos[j][0]:
                if int(dados[i][papel][4:]) != int(titulos_permitidos[j][1]):
                    permitido = False
        if permitido:
            filtered_fados.append(dados[i])

    return filtered_fados


def filtrar_papel(titulos, dados, file_name):
    titulos_permitidos = io.import_from_csv(file_name, get_titles=False)

    papel = find.index_of_item("Papel", titulos)
    filtered_fados = []
    for i in range(len(dados)):
        permitido = True
        for j in range(len(titulos_permitidos)):
            if dados[i][papel][:4] == titulos_permitidos[j][0]:
                permitido = False
        if permitido:
            filtered_fados.append(dados[i])

    return filtered_fados


def invalidos(titulos, dados):
    return filtrar_papel(titulos, dados, "filtro_invalidos.csv")


def dividendos_irregulares(titulos, dados):
    return filtrar_papel(titulos, dados, "filtro_dividendos_irregulares.csv")
