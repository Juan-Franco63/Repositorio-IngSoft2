from tareas.fabrica import TareaNormalFactory, TareaImportanteFactory
from comandos.agregar_tarea import AgregarTarea
from comandos.completar_tarea import CompletarTarea
from comandos.listar_tareas import ListarTareas
from comandos.ejecutor import EjecutorComandos

def main():
    tareas = []
    ejecutor = EjecutorComandos()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea normal")
        print("2. Agregar tarea importante")
        print("3. Completar tarea")
        print("4. Listar tareas")
        print("5. Salir")
        opc = input("Opción: ")

        if opc == "1":
            desc = input("Descripción: ")
            tarea = TareaNormalFactory().crear_tarea(desc)
            ejecutor.ejecutar(AgregarTarea(tareas, tarea))
        elif opc == "2":
            desc = input("Descripción: ")
            tarea = TareaImportanteFactory().crear_tarea(desc)
            ejecutor.ejecutar(AgregarTarea(tareas, tarea))
        elif opc == "3":
            index = int(input("Índice tarea a completar: "))
            ejecutor.ejecutar(CompletarTarea(tareas, index))
        elif opc == "4":
            ejecutor.ejecutar(ListarTareas(tareas))
        elif opc == "5":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
