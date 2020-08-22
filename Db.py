import psycopg2
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler("user.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def connection_db():
    try:
        con = psycopg2.connect("dbname='agenda' user='rod' password='forever11' host='localhost' ")
        return con
    except Exception as e:
        logger.error("connection_db {}".format(e))
        logger.debug(e)

def close_connection(con, cur):
    con.close()
    cur.close()