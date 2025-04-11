from .comando_base import Comando

class CompletarTarea(Comando):
    def __init__(self, lista, index):
        self.lista = lista
        self.index = index

    def ejecutar(self):
        if 0 <= self.index < len(self.lista):
            self.lista[self.index].completar()
