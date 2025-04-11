def mal_codigo(lista):
    print("Bienvenido al gestor... (Spaghetti)")
    desc = input("Desc de tarea: ")
    tipo = input("¿Es importante? (s/n): ")
    if tipo == "s":
        lista.append({"desc": desc, "tipo": "importante", "comp": False})
        print("Tarea añadida.")
    else:
        lista.append({"desc": desc, "tipo": "normal", "comp": False})
        print("Tarea añadida.")
    for i, t in enumerate(lista):
        c = "✔" if t["comp"] else "✘"
        print(f"{i}: [{c}] {t['tipo'].capitalize()}: {t['desc']}")
