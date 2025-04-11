from .tarea_base import Tarea

class TareaImportante(Tarea):
    def completar(self):
        self.completada = True

    def mostrar(self):
        estado = "✔" if self.completada else "✘"
        return f"[{estado}] ⚠️ Tarea IMPORTANTE: {self.descripcion}"
