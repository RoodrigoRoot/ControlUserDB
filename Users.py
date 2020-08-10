from Db import connection_db
from Logger import logger
from Logger import LoggerUserDB
class User:
    
    def __init__(self, username, name, last_name, phone):
        self.__username = username
        self.__name = name
        self.__last_name = last_name
        self.__phone = phone
    
    
    def __str__(self):
        return "User"
    
    def get_username(self):
        return self.__username
    
    def set_username(self, username):
        self.__username = username
    
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    
    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_phone(self):
        return self.__phone
    
    def set_phone(self, phone):
        self.__phone = phone
    
    username = property(get_username, set_username)
    name = property(get_name, set_name)
    last_name = property(get_last_name, set_last_name)
    phone = property(get_phone, set_phone)


class UserMethods:
    
    @classmethod
    def create_user(cls):
        name = input("Nombre: ")
        last_name = input("Apellido: ")
        username = input("Usuario: ")
        phone = input("Teléfono: ")
        user = User(username, name, last_name, phone)
        return user
    
    @classmethod
    def get_id(cls):
        id_user = input("Ingrese el identificador del usuario: ")
        id_user = int(id_user)
        return id_user

class UserDB:    
    
    @classmethod
    def save_user(cls, user):
        con = connection_db()
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO users VALUES ('{}',  '{}', '{}', '{}'); ".                                                                        format(user.name,
                                                                                            user.last_name,
                                                                                            user.username,
                                                                                            user.phone
                                                                                            ))
            con.commit()
            cur.close()
            con.close()
        except Exception as e:
            LoggerUserDB().write_error_user_db(e)
    
    @classmethod
    def search_user(cls, id_user):
        pass

    @classmethod
    def show_all_users(cls):
        try:
            con = connection_db()
            cur = con.cursor()
            cur.execute("SELECT * FROM USERS;")
            print(cur.fetchall())
            cur.close()
            con.close()
        except Exception as e:
            LoggerUserDB().write_error_user_db(e)
        
