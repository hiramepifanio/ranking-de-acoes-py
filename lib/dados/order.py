from lib.dados import rank


def by_item(item, titulos, dados):
    return order(dados, rank.by_item(item, titulos, dados))


def by_item_desc(item, titulos, dados):
    return order(dados, rank.by_item_desc(item, titulos, dados))


def order(dados, column_with_order):
    ordered_dados = []
    for i in range(len(dados)):
        ordered_dados.append([])

    for i in range(len(dados)):
        ordered_dados[column_with_order[i]] = dados[i]

    return ordered_dados
