import pymysql

def create_connection():
    try:
        conn = pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Billing")
        print("Database Connected")
        return conn
    except Exception as e:
        print(e)

conn = create_connection()
