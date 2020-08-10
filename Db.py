import psycopg2

def connection_db():
    try:
        con = psycopg2.connect("dbname='agenda' user='rod' password='forever11' host='localhost' ")
        return con
    except Exception as e:
        print(e)
