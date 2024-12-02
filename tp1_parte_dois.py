import time
import tracemalloc
from hashlib import sha256

from tp1_parte_um import ler_lista_de_arquivos
from utils.tabela_hash import TabelaHash
from utils.fila import Fila
from utils.pilha import Pilha


def tp1_parte_dois():
    caminho_lista_arquivos = "listagem_arquivos.txt"
    lista_arquivos = ler_lista_de_arquivos(caminho_lista_arquivos)
    operacoes_pilha(lista_arquivos)
    operacoes_fila(lista_arquivos)
    operacoes_tabela_hash(lista_arquivos)


def operacoes_pilha(dados):
    tracemalloc.start()
    pilha = inicializa_pilha(dados)

    posicoes = [1, 100, 1000, 5000]
    posicoes_solicitadas = []

    inicio_remocao = time.time()
    posicao_atual = 0
    while len(posicoes) > 0:
        atual = pilha.pop()
        posicao_atual += 1
        if posicao_atual in posicoes:
            posicoes_solicitadas.append(atual)
            posicoes.pop(0)

    tempo_remocao = time.time() - inicio_remocao
    _, maior_uso_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"""Pilha - Resgatando indices :
    tempo: {tempo_remocao} segundos.
    Arquivos solicitados: {posicoes_solicitadas}
    memoria usada: {maior_uso_mem / (1024 * 1024)} MB
    -------------------""")

    return posicoes_solicitadas, tempo_remocao, maior_uso_mem


def inicializa_pilha(dados):
    pilha = Pilha(len(dados))
    for item in dados:
        pilha.push(item)
    return pilha


def operacoes_fila(dados):
    tracemalloc.start()
    fila = inicializa_fila(dados)

    posicoes = [1, 100, 1000, 5000]
    posicoes_solicitadas = []
    posicao_atual = 0
    inicio_remocao = time.time()

    while len(posicoes) > 0:
        atual = fila.dequeue()
        posicao_atual += 1
        if posicao_atual in posicoes:
            posicoes_solicitadas.append(atual)
            posicoes.pop(0)

    tempo_remocao = time.time() - inicio_remocao
    _, maior_uso_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"""Fila - Resgatando indices:
    Tempo:{tempo_remocao} segundos.
    Arquivos solicitados: {posicoes_solicitadas}
    memoria usada: {maior_uso_mem / (1024 * 1024)} MB
    -------------------""")
    return posicoes_solicitadas, tempo_remocao, maior_uso_mem


def inicializa_fila(dados):
    fila = Fila(len(dados))
    for item in dados:
        fila.enqueue(item)
    return fila


def operacoes_tabela_hash(dados):
    tracemalloc.start()
    tabela_hash = inicializa_hashtable(dados)

    posicoes = [1, 100, 1000, 5000, len(dados)]
    arquivos = []

    inicio_remocao = time.time()

    for posicao in posicoes:
        arquivos.append(tabela_hash.get(posicao))

    tempo_remocao = time.time() - inicio_remocao
    _,maior_uso_memoria = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"""Tabela Hash - Resgatando indices:
    Tempo de execução: {tempo_remocao} segundos.
        Arquivos solicitados: {arquivos}
        memoria usada: {maior_uso_memoria / (1024 * 1024)} MB
        -------------------""")

    return arquivos, tempo_remocao


def inicializa_hashtable(dados):
    tabela_hash = TabelaHash()
    for chave, item in enumerate(dados):
        tabela_hash.add(chave, item)
    return tabela_hash
