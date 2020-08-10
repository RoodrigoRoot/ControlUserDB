from Users import User, UserMethods, UserDB
from Constans import *

class Menu:
    
    @classmethod
    def selected_option(cls, option):
        if option == ADD:
            user = UserMethods.create_user()
            UserDB.save_user(user)
        elif option == SEARCH:
            pass
        elif option == SHOW:
            UserDB.show_all_users()

Menu().selected_option(5)