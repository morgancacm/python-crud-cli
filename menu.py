import getpass

def get_hidden_password():
    try:
        hidden_password = getpass.getpass("Ingrese su contraseña: ")
    except Exception as error:
        print("Error: ", error)
        hidden_password = None

    return hidden_password

def show_info():
    print("Lista de registros:")
    # agregar lógica para mostrar en pantalla todos los registros.

def add_new_user():
    username = input("Ingrese su nombre de usuario: ")
    password = get_hidden_password()
    # agregar lógica para añadir al usuario y que se le agregue de manera automática un id de creación.

def remove_user():
    id_remove = input("Ingrese el id del usuario que desea eliminar: ")
    # agregar lógica para borrar el usuario.
    print(f"Usuario con el id: {id_remove} eliminado correctamente!.")

def edit_user():
    id_edit = input("Ingrese el id del usuario que desea editar: ")
    # agregar lógica para editar un usuario.
    print(f"Usuario con el id: {id_edit} editado correctamente!.")

def main():
    while True:
        print("Lista de opciones:")
        print("1) Ver todos los registros")
        print("2) Añadir un usuario nuevo al sistema")
        print("3) Eliminar un usuario del sistema")
        print("4) Editar un usuario del sistema")
        print("5) Salir del sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            show_info()
        elif opcion == "2":
            add_new_user()
        elif opcion == "3":
            remove_user()
        elif opcion == "4":
            edit_user()
        elif opcion == "5":
            exit()
        else:
            print("Esta opción no existe en el sistema.")