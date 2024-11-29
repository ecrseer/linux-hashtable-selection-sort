import time
from hashlib import sha256

from tp1_parte_um import ler_lista_de_arquivos
from utils.tabela_hash import TabelaHash
from utils.fila import Fila
from utils.pilha import Pilha


def tp1_parte_dois():
    caminho_lista_arquivos = "listagem_arquivos.txt"
    lista_arquivos = ler_lista_de_arquivos(caminho_lista_arquivos)

    arquivos, tempo = operacoes_tabela_hash(lista_arquivos)
    print(f"""Tempo de execução da operação de tabela hash: {tempo} segundos.
    Arquivos recuperados: {arquivos}
    -------------------""")

    for operacao, funcao in [("Tabela Hash", operacoes_tabela_hash),
                             ("Pilha", operacoes_pilha),
                             ("Fila", operacoes_fila)]:
        resultados = funcao(lista_arquivos)
        print(f"{operacao}:\n"
              f"  Recuperados: {resultados[0]}\n"
              f"  Tempo de Remoção: {resultados[1]} segundos\n")


def operacoes_pilha(dados):
    pilha = Pilha(len(dados))
    for item in dados:
        pilha.push(item)

    posicoes = [1, 100, 1000, 5000]
    recuperados = []

    inicio_remocao = time.time()
    posicao_atual = 0
    while len(posicoes) > 0:
        atual = pilha.pop()
        posicao_atual += 1
        if posicao_atual in posicoes:
            recuperados.append(atual)
            posicoes.pop(0)

    tempo_remocao = time.time() - inicio_remocao

    return recuperados, tempo_remocao


def operacoes_fila(dados):
    fila = Fila(len(dados))
    for item in dados:
        fila.enqueue(item)

    posicoes = [1, 100, 1000, 5000]
    recuperados = []

    for pos in posicoes:
        if pos <= fila.tamanho_atual:
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
