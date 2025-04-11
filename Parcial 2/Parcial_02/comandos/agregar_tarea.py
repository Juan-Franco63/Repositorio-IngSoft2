from .comando_base import Comando

class AgregarTarea(Comando):
    def __init__(self, lista, tarea):
        self.lista = lista
        self.tarea = tarea

    def ejecutar(self):
        self.lista.append(self.tarea)
