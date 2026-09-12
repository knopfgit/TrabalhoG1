def insertion_sort(produtos):
    produtos = produtos[:]

    for i in range(1, len(produtos)):
        atual = produtos[i]
        j = i - 1

        while j >= 0 and produtos[j].id > atual.id:
            produtos[j + 1] = produtos[j]
            j -= 1

        produtos[j + 1] = atual

    return produtos