from lib.dados import find


def append_column(titulo_column, dados_column, titulos, dados):
    titulos.append(titulo_column)
    for i in range(len(dados)):
        dados[i].append(dados_column[i])


def minus_column(item, titulos, dados):
    dados_negativo = []
    for row in dados:
        new_row = []
        for item_aux in row:
            new_row.append(item_aux)
        dados_negativo.append(new_row)

    col = find.index_of_item(item, titulos)
    for i in range(len(dados)):
        dados_negativo[i][col] = - dados_negativo[i][col]

    return dados_negativo
