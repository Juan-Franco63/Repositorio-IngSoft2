class EjecutorComandos:
    def __init__(self):
        self.historial = []

    def ejecutar(self, comando):
        comando.ejecutar()
        self.historial.append(comando)
