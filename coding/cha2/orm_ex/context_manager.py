import sqlite3

class DataConn:
    def __init__(self,db_name):
        self.db_name = db_name
        print("Input the DB")

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
        print("Connect to the DB")

    def __exit__(self,exc_type,exc_val,exc_tb):
        print("Disconnect to the DB")
        self.conn.close()
        if exc_val:
            raise

if __name__ == "__main__":
    db = "D:\\tutorial\\Architecture_Patterns_with_Python\\coding\\cha2\\db_tes.db"
    with DataConn(db) as conn:
        print("Manipulate the DB")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM test")
        for row in cursor:
            print(row[0], row[1], row[2])