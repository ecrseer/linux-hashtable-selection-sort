def tp1_parte_um():
    caminho_lista_arquivos = "listagem_arquivos.txt"
    lista_arquivos = ler_lista_de_arquivos(caminho_lista_arquivos)

    caminho_arquivo_ordenado = "ordenada_listagem_arquivos.txt"
    ordenar_bubble_sort(caminho_arquivo_ordenado, lista_arquivos)


def ler_lista_de_arquivos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        return [linha.strip() for linha in f.readlines()]


def ordenar_bubble_sort(file_path, lista_desordenada):
    lista_ordenada = bubble_sort_completo(lista_desordenada)
    with open(file_path, 'w') as f:
        f.write('\n'.join(lista_ordenada))
    return lista_ordenada


def bubble_sort_completo(lista):
    index_fim = len(lista) - 1
    tudo_ordenado = False

    while not tudo_ordenado:
        tudo_ordenado = True
        lista, tudo_ordenado = bubble_sort_ordena_nota(lista, index_fim)
        index_fim -= 1
    return lista


def bubble_sort_ordena_nota(lista, index_fim):
    tudo_ordenado = True
    for i in range(index_fim):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            tudo_ordenado = False
    return lista, tudo_ordenado
