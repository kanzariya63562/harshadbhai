import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        if query.lower().startswith("select"):
            return self.cursor.fetchall()
        else:
            self.connection.commit()
            return self.cursor.rowcount

    def close(self):
        self.connection.close()