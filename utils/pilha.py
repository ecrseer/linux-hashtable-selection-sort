class Pilha:
    def __init__(self, tamanho_maximo=10):
        self.topo = -1
        self.itens = [None] * tamanho_maximo
        self.tamanho_maximo = tamanho_maximo

    def is_full(self):
        return self.topo == self.tamanho_maximo - 1

    def is_empty(self):
        return self.topo == -1

    def push(self, item):
        if self.is_full():
            print("Pilha cheia")
            return
        self.topo += 1
        self.itens[self.topo] = item

    def pop(self):
        if self.is_empty():
            print("Pilha vazia")
            return
        item = self.itens[self.topo]
        self.itens[self.topo] = None
        self.topo -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Pilha vazia")
            return
        return self.itens[self.topo]

    def display(self):
        if self.is_empty():
            print("Pilha vazia")
        else:
            print("Pilha:", self.itens[:self.topo + 1])

