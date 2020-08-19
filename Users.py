from Db import close_connection
from Logger import logger
from Logger import LoggerUserDB
import os
import time


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
    def save_user_db(cls, user, con):
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO users (name, last_name, username, phone) VALUES ('{}',  '{}', '{}', '{}'); ".format(user.name,
                                                                                                                         user.last_name,
                                                                                                                         user.username,
                                                                                                                         user.phone
                                                                                                                         ))

            con.commit()
            close_connection(con, cur)
        except Exception as e:
            LoggerUserDB().write_error_user_db(e)

    @classmethod
    def search_user_db(cls, con):
        cur = con.cursor()
        id_user = UserMethods.get_id()
        sql = "SELECT * FROM users WHERE codigo={}".format(id_user)
        cur.execute(sql)
        user = cur.fetchone()
        if user is not None:
            print("---------------------------------")
            print("Código: {} | Usuario: {} | Nombre: {} | Apellido: {} | Teléfono: {}".format(
                user[0],
                user[1],
                user[2],
                user[3],
                user[4]
            ))
            print("---------------------------------")
            time.sleep(3)
        else:
            print("---------------------------------")
            print("No existe Ningún usuario con ese código")
            print("---------------------------------")
            time.sleep(3)

    @classmethod
    def show_all_users_db(cls, con):
        try:
            cur = con.cursor()
            cur.execute("SELECT * FROM users;")
            users = cur.fetchall()
            cls.to_list_users(users)
            close_connection(con, cur)
        except Exception as e:
            LoggerUserDB().write_error_user_db(e)

    @classmethod
    def to_list_users(cls, users):
        os.system("clear")
        if users:
            for user in users:
                print("Identificador: {}".format(user[0]))
                print("Nombre: {}".format(user[1]))
                print("Apellido: {}".format(user[2]))
                print("Usuario: {}".format(user[3]))
                print("Teléfono: {}".format(user[4]))
                print("-----------------------------------")
            time.sleep(3)
        else:
            print("No hay usuarios registrados por el momento")
            time.sleep(3)

    @classmethod
    def delete_user_db(cls, con):
        cur = con.cursor()
        id_user = UserMethods.get_id()
        sql = "DELETE FROM users WHERE codigo={}".format(id_user)
        cur.execute(sql)
        try:
            con.commit()
            print("Usuario Eliminado")

        except Exception as e:
            print("El usuario no puede eliminarse: {}".format(e))
