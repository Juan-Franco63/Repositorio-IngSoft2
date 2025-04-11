from .tarea_base import Tarea

class TareaNormal(Tarea):
    def completar(self):
        self.completada = True

    def mostrar(self):
        estado = "✔" if self.completada else "✘"
        return f"[{estado}] Tarea normal: {self.descripcion}"
