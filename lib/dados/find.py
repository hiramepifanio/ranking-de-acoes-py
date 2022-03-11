def index_of_item(target, titulos):
    index = -1
    for i, titulo in enumerate(titulos):
        if titulo == target:
            index = i
            break
    if index < 0:
        raise Exception("Título inexistente: \"" + target + '\"')

    return index
