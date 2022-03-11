from lib.dados import find


def add_columns(items, titulos, dados):
    new_column = []
    for i in range(len(dados)):
        value = 0
        for item in items:
            value += dados[i][find.index_of_item(item, titulos)]
        new_column.append(value)

    return new_column


def mult_columns(items, titulos, dados):
    new_column = []
    for i in range(len(dados)):
        value = 1
        for item in items:
            value *= dados[i][find.index_of_item(item, titulos)]
        new_column.append(round(value, 2))

    return new_column
