from .tarea_normal import TareaNormal
from .tarea_importante import TareaImportante

class TareaFactory:
    def crear_tarea(self, descripcion):
        pass

class TareaNormalFactory(TareaFactory):
    def crear_tarea(self, descripcion):
        return TareaNormal(descripcion)

class TareaImportanteFactory(TareaFactory):
    def crear_tarea(self, descripcion):
        return TareaImportante(descripcion)
