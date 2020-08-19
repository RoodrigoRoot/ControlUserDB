from Users import User, UserMethods, UserDB
from Constans import *
from Db import connection_db


class Menu:

    @classmethod
    def selected_option(cls, option):
        con = connection_db()
        if option == ADD:
            user = UserMethods.create_user()
            UserDB.save_user(user, con)
        elif option == SEARCH:
            UserDB.search_user(con)
        elif option == UPDATE:
            pass
        elif option == DELETE:
            UserDB.delete_user_db(con)
        elif option == SHOW:
            UserDB.show_all_users_db(con)

    @classmethod
    def show_menu(cls):
        menu = """Control de Usuarios en DB
1.-Agregar Usuario
2.-Buscar Usuario
3.-Modificar Usuario
4.-Eliminar Usuario
5.-Mostrar los Usuarios
6.-Salir\n"""
        option = 0
        while option != 6:
            option = int(input(menu))
            cls.selected_option(option)
            if option > 6 or option <= 0:
                print("Solo se aceptan un número entre 1 y 6")
        else:
            print("Hasta Pronto")


# Menu.selected_option(5)
Menu.show_menu()
