from tp1.fila import Fila
from tp1.pilha import Pilha
import os
import time
from hashlib import sha256

from tp1.tabela_hash import TabelaHash


def start_tp1():
    caminho_lista_arquivos = "listagem_arquivos.txt"
    lista_arquivos = ler_lista_de_arquivos(caminho_lista_arquivos)

    caminho_arquivo_ordenado = "ordenada_listagem_arquivos.txt"
    ordenar_bubble_sort(caminho_arquivo_ordenado, lista_arquivos)

    arquivos, tempo = operacoes_tabela_hash(lista_arquivos)
    print(f"""Tempo de execução da operação de tabela hash: {tempo} segundos.
    Arquivos recuperados: {arquivos}
    -------------------""")

    arquivos, tempo = operacoes_pilha(lista_arquivos)

    for operacao, funcao in [("Tabela Hash", operacoes_tabela_hash),
                             ("Pilha", operacoes_pilha),
                             ("Fila", operacoes_fila)]:
        resultados = funcao(lista_arquivos)
        print(f"{operacao}:\n"
              f"  Recuperados: {resultados[0]}\n"
              f"  Tempo de Remoção: {resultados[1]} segundos\n")


def bubble_sort_ordena_nota(lista, index_fim):
    tudo_ordenado = True
    for i in range(index_fim):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            tudo_ordenado = False
    return lista, tudo_ordenado


def bubble_sort_completo(lista):
    index_fim = len(lista) - 1
    tudo_ordenado = False

    while not tudo_ordenado:
        tudo_ordenado = True
        lista, tudo_ordenado = bubble_sort_ordena_nota(lista, index_fim)
        index_fim -= 1
    return lista


def ler_lista_de_arquivos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        return [linha.strip() for linha in f.readlines()]


def ordenar_bubble_sort(file_path, lista_desordenada):
    lista_ordenada = bubble_sort_completo(lista_desordenada)
    with open(file_path, 'w') as f:
        f.write('\n'.join(lista_ordenada))
    return lista_ordenada


def operacoes_pilha(dados):
    pilha = Pilha(len(dados))
    for item in dados:
        pilha.push(item)

    posicoes = [1, 100, 1000, 5000]
    recuperados = []

    for pos in posicoes:
        if pos <= pilha.size():

            aux_pilha = Pilha(len(dados))
            for _ in range(pilha.size() - pos):
                aux_pilha.push(pilha.pop())
            recuperados.append(pilha.peek())
            while not aux_pilha.is_empty():
                pilha.push(aux_pilha.pop())

    inicio_remocao = time.time()
    for _ in range(100):
        pilha.pop()
    tempo_remocao = time.time() - inicio_remocao

    return recuperados, tempo_remocao


def operacoes_fila(dados):
    fila = Fila(len(dados))
    for item in dados:
        fila.enqueue(item)

    posicoes = [1, 100, 1000, 5000]
    recuperados = []

    for pos in posicoes:
        if pos <= fila.size():
            for _ in range(pos - 1):
                fila.enqueue(fila.dequeue())
            recuperados.append(fila.peek())
            fila.enqueue(fila.dequeue())

    inicio_remocao = time.time()
    for _ in range(100):
        fila.dequeue()
    tempo_remocao = time.time() - inicio_remocao

    return recuperados, tempo_remocao


def operacoes_tabela_hash(dados):
    tabela_hash = TabelaHash()
    for item in dados:
        tabela_hash.add(sha256(item.encode()).hexdigest(), item)

    posicoes = [1, 100, 1000, 5000, len(dados)]
    recuperados = [
        tabela_hash.get(sha256(dados[pos - 1].encode()).hexdigest())
        for pos in posicoes if pos <= len(dados)
    ]

    inicio_remocao = time.time()
    for chave in tabela_hash.keys()[:100]:
        tabela_hash.remove(chave)
    tempo_remocao = time.time() - inicio_remocao

    return recuperados, tempo_remocao
