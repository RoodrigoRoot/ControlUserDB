import logging
logger = logging.getLogger('')
from Db import connection_db

class Logger:
    
    def write_error(self, message):
        try:
            with open("Errors.log", "a") as file:
                content = "LoggerUserDB.write_error {}\n".format(message)
                file.write(content)           
        except Exceptionas as e:
            logger.error("Logger.Write_Error {}\n".format(e))
    

class LoggerUserDB(Logger):
    
    @classmethod 
    def write_error(self, message):
        try:
            with open("Error.log", "a") as file:
                content = "{}\n".format(message)
                print(message)
                print(content)
                file.write(content)           
        except Exceptionas as e:
            logger.error("LoggerUserDB.Write_Error {}\n".format(e))

            
    @classmethod
    def write_error_user_db(cls, error):
        try:
            message = "LoggerUserDB.write_error_user_db.{}".format(error)
            con = connection_db()
            cur = con.cursor()
            cur.execute("INSERT INTO errors (error) VALUES ('{}')".format(message))
            con.commit()
            cur.close()
            con.close()
            cls.write_error(message)
        except Exception as e:
            logger.error(str(e))