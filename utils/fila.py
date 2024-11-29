class Fila:
    def __init__(self, tamanho_maximo):
        self.inicio = 0
        self.fim = 0
        self.tamanho_max = tamanho_maximo
        self.tamanho_atual = 0
        self.itens = [None] * tamanho_maximo

    def is_empty(self):
        return self.tamanho_atual == 0

    def is_full(self):
        return self.tamanho_atual == self.tamanho_max

    def enqueue(self, item):
        if self.is_full():
            print("Erro: A fila está cheia")
            return

        self.itens[self.fim] = item
        self.fim = (self.fim + 1) % self.tamanho_max
        self.tamanho_atual += 1

    def dequeue(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None

        item = self.itens[self.inicio]
        self.itens[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.tamanho_max
        self.tamanho_atual -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        return self.itens[self.inicio]

    def display(self):
        if self.is_empty():
            print("A fila está vazia")
        else:
            print("Fila:", [self.itens[(self.inicio + i) % self.tamanho_max] for i in range(self.tamanho_atual)])
