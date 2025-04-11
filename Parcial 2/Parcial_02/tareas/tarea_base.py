from abc import ABC, abstractmethod

class Tarea(ABC):
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    @abstractmethod
    def completar(self):
        pass

    @abstractmethod
    def mostrar(self):
        pass
