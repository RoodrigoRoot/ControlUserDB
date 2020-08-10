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
            pass
        elif option == SHOW:
            UserDB.show_all_users(con)

Menu().selected_option(5)