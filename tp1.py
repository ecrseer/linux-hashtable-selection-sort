import time
from hashlib import sha256

from tp1_parte_dois import tp1_parte_dois
from tp1_parte_um import tp1_parte_um
from tp1_parte_um import ler_lista_de_arquivos
from utils.tabela_hash import TabelaHash
from utils.fila import Fila
from utils.pilha import Pilha


def start_tp1():
    tp1_parte_um()
    tp1_parte_dois()
