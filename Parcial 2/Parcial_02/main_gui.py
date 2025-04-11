import tkinter as tk
from tkinter import messagebox

from tareas.fabrica import TareaNormalFactory, TareaImportanteFactory
from comandos.agregar_tarea import AgregarTarea
from comandos.completar_tarea import CompletarTarea
from comandos.ejecutor import EjecutorComandos
from comandos.listar_tareas import ListarTareas
from persistencia import guardar_tareas, cargar_tareas


class GestorTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x500")

        # --- Cargar tareas guardadas ---
        self.tareas = cargar_tareas()
        self.ejecutor = EjecutorComandos()

        # --- Interfaz ---
        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=10)

        self.btn_normal = tk.Button(root, text="Agregar Tarea Normal", command=self.agregar_normal)
        self.btn_normal.pack()

        self.btn_importante = tk.Button(root, text="Agregar Tarea Importante", command=self.agregar_importante)
        self.btn_importante.pack()

        self.lista_tareas = tk.Listbox(root, width=50, height=15)
        self.lista_tareas.pack(pady=10)

        self.btn_completar = tk.Button(root, text="Completar tarea seleccionada", command=self.completar_tarea)
        self.btn_completar.pack()

        self.actualizar_lista()

    def agregar_normal(self):
        desc = self.entrada.get()
        if desc:
            tarea = TareaNormalFactory().crear_tarea(desc)
            self.ejecutor.ejecutar(AgregarTarea(self.tareas, tarea))
            guardar_tareas(self.tareas)  # 🔄 Guardar después de agregar
            self.actualizar_lista()
            self.entrada.delete(0, tk.END)

    def agregar_importante(self):
        desc = self.entrada.get()
        if desc:
            tarea = TareaImportanteFactory().crear_tarea(desc)
            self.ejecutor.ejecutar(AgregarTarea(self.tareas, tarea))
            guardar_tareas(self.tareas)  # 🔄 Guardar después de agregar
            self.actualizar_lista()
            self.entrada.delete(0, tk.END)

    def completar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            self.ejecutor.ejecutar(CompletarTarea(self.tareas, index))
            guardar_tareas(self.tareas)  # 🔄 Guardar después de completar
            self.actualizar_lista()
        else:
            messagebox.showwarning("Atención", "Selecciona una tarea para completar.")

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            self.lista_tareas.insert(tk.END, tarea.mostrar())


if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareasApp(root)
    root.mainloop()
