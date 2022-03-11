from lib.dados import find
from lib.dados import alter


def by_item(item, titulos, dados):
    col = find.index_of_item(item, titulos)
    rank, rank_inverso = [], []
    for i in range(len(dados)):
        rank.append(i)
        rank_inverso.append(0)
    for i in range(len(dados)):
        index_min = i
        for j in range(i + 1, len(dados)):
            if dados[rank[j]][col] < dados[rank[index_min]][col]:
                index_min = j
        rank[i], rank[index_min] = rank[index_min], rank[i]

    for i in range(len(dados)):
        rank_inverso[rank[i]] = i

    return rank_inverso


def by_item_desc(item, titulos, dados):
    dados_negativo = alter.minus_column(item, titulos, dados)

    return by_item(item, titulos, dados_negativo)
