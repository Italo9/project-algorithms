#  referencia bibliografica:
# https://joaoarthurbm.github.io/eda/posts/quick-sort/
# https://stackoverflow.com/questions/18262306/quicksort-with-python


def quicksort(lista, left, right):
    if len(lista) == 1:
        return lista

    if left < right:
        index = partition(lista, left, right)
        quicksort(lista, left, index - 1)
        quicksort(lista, index + 1, right)


def partition(lista, left, right):
    pivot = lista[right]
    i = left - 1

    for j in range(left, right):
        if lista[j] <= pivot:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[right] = lista[right], lista[i + 1]

    return i + 1


def is_anagram(first_string, second_string):
    primeira = first_string.lower()
    segunda = second_string.lower()

    if primeira == segunda:
        return (primeira, segunda, True)

    lista_primeira = [primeira]
    lista_segunda = [segunda]

    quicksort(lista_primeira, 0, len(lista_primeira) - 1)
    quicksort(lista_segunda, 0, len(lista_segunda) - 1)

    join_lista_primeira = "".join(lista_primeira)
    join_lista_segunda = "".join(lista_segunda)

    if primeira == "" and segunda == "":
        return (join_lista_primeira, join_lista_segunda, False)
    if lista_primeira == lista_segunda:
        return (join_lista_primeira, join_lista_segunda, True)
    return (join_lista_primeira, join_lista_segunda, False)
