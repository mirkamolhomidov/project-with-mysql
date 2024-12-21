from mysql.connector import connect, DatabaseError

HOST = "localhost"
USER = "root"
PASSWORD = "Mirkamol2008!@#$"
DATABASE = "school"


def connect_db():
    try:
        conn = connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        
        return conn
    except DatabaseError as e:
        print(f"Xatolik: {e}")
    except Exception as error:
        print(error)