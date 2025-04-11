from .comando_base import Comando

class ListarTareas(Comando):
    def __init__(self, lista):
        self.lista = lista

    def ejecutar(self):
        for i, tarea in enumerate(self.lista):
            print(f"{i}. {tarea.mostrar()}")
