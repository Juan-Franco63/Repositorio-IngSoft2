from Windows_dialog import Windows_Dialog
from HTML_dialog import HTML_dialog

DIALOG_TYPES = {
        "windows": Windows_Dialog,
        "html": HTML_dialog
}

def main():

    dialog = None

    system_type = input("Elija el boton que va a crear (Opciones = Windows/html)").strip().lower()
    # SOLUCION UTILIZANDO IF/ELSE
    # if system_type == "windows":
    #     dialog = Windows_Dialog()
    # elif system_type == "html":
    #     dialog = HTML_dialog()
    # else:
    #     # If the input is not valid, print a message and return
    #     print("Por favor elija una opcion de las dadas")
    #     return

    DialogClass = DIALOG_TYPES.get(system_type)

    if DialogClass is None:
        print("Por favor elija una opcion de las dadas")
        return
    
    dialog = DialogClass()
    dialog.render()



if __name__ == "__main__":
    main()