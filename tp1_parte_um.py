import time
import matplotlib.pyplot as plt
import matplotlib
import numpy as np



def tp1_parte_um():
    caminho_lista_arquivos = "listagem_arquivos.txt"
    lista_arquivos = ler_lista_de_arquivos(caminho_lista_arquivos)
    bubble = mostra_media_bubble_sort(lista_arquivos[:700])
    quick = mostra_media_quick_sort(lista_arquivos[:700])
    criar_grafico(lista_arquivos)


def ler_lista_de_arquivos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        return [linha.strip() for linha in f.readlines()]


def mostra_media_bubble_sort(lista_arquivos):
    arquivo_escrever = "ordenada_listagem_arquivos.txt"
    lista, tempo_total = BubbleSort().ordenar_bubble_sort(
        arquivo_escrever, lista_arquivos)
    lista_dois, tempo_total_dois = BubbleSort().ordenar_bubble_sort(
        arquivo_escrever, lista_arquivos)

    media_tempo = (tempo_total + tempo_total_dois) / 2
    print(f"""Bubble Sort - Ordenando lista de arquivos:
    Média de tempo: {media_tempo} segundos.
    -------------------""")
    return media_tempo


class BubbleSort:
    linha_do_tempo = [time.time()]

    def ordenar_bubble_sort(self, file_path, lista_desordenada):
        tempo_inicio = time.time()
        lista_ordenada = self.bubble_sort_completo(lista_desordenada)
        tempo_total = time.time() - tempo_inicio

        with open(file_path, 'w') as f:
            f.write('\n'.join(lista_ordenada))
        return lista_ordenada, tempo_total

    def bubble_sort_completo(self, lista):
        index_fim = len(lista) - 1
        tudo_ordenado = False

        while not tudo_ordenado:
            tudo_ordenado = True
            lista, tudo_ordenado = self.bubble_sort_ordena_asc(lista, index_fim)
            index_fim -= 1
        return lista

    def bubble_sort_ordena_asc(self, lista, index_fim):
        tudo_ordenado = True
        for i in range(index_fim):
            if lista[i] < lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                atual = time.time()
                self.linha_do_tempo.append(atual - self.linha_do_tempo[-1])
                tudo_ordenado = False
        return lista, tudo_ordenado


def mostra_media_quick_sort(lista_arquivos):
    lista, tempo_total = QuickSort().ordenar_quick_sort(
        lista_arquivos)
    lista_dois, tempo_total_dois = QuickSort().ordenar_quick_sort(
        lista_arquivos)

    media_tempo = (tempo_total + tempo_total_dois) / 2
    print(f"""Quick Sort - Ordenando lista de arquivos:
    Média de tempo: {media_tempo} segundos.
    -------------------""")
    return media_tempo


class QuickSort:
    def ordenar_quick_sort(self, lista_desordenada):
        inicio = time.time()
        lista_ordenada = self.quick_sort_completo(lista_desordenada)
        tempo_total = time.time() - inicio
        return lista_ordenada, tempo_total

    def quick_sort_completo(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivo = lista.pop()

        menores, maiores = [], []
        for item in lista:
            if item < pivo:
                menores.append(item)
            else:
                maiores.append(item)

        return self.quick_sort_completo(menores) + [pivo] + self.quick_sort_completo(maiores)


class SelectionSort:
    def ordenar_selection_sort(self, lista_desordenada):
        inicio = time.time()
        lista_ordenada = self.selection_sort_completo(lista_desordenada)
        tempo_total = time.time() - inicio
        return lista_ordenada, tempo_total

    def selection_sort_completo(self, lista):
        for i in range(len(lista)):
            menor = i
            for j in range(i + 1, len(lista)):
                if lista[j] < lista[menor]:
                    menor = j


def criar_grafico(lista_arquivos):
    tamanho_lista = [30, 70, 200, 500, 700]
    tempos_bubble = []
    tempos_quick = []
    for tamanho in tamanho_lista:
        bubble, quick = gera_dados_grafico(lista_arquivos,tamanho)
        tempos_bubble.append(bubble)
        tempos_quick.append(quick)

    print(f"tamanho qq {len(tempos_quick)}")
    print(f"tamanho bb {len(tempos_bubble)}")

    plt.figure(figsize=(10, 6))
    plt.plot(tamanho_lista, tempos_bubble, label="Bubble Sort", marker='x')
    plt.plot(tamanho_lista, tempos_quick, label="Quick Sort", marker='o')
    plt.xlabel("Array Size (Power of 2)")
    plt.ylabel("Execution Time")
    plt.title("Execution Time Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig("plot.png")


def gera_dados_grafico(lista_arquivos, tamanho=700):
    bubble = mostra_media_bubble_sort(lista_arquivos[:tamanho])
    quick = mostra_media_quick_sort(lista_arquivos[:tamanho])
    return bubble, quick
