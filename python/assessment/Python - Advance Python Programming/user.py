class User:
    def __init__(self, name):
        self.name = name

    def register(self, db, password):
        query = "INSERT INTO users (name, password) VALUES (%s, %s)"
        params = (self.name, password)
        rows_affected = db.execute_query(query, params)
        if rows_affected > 0:
            print(f"User '{self.name}' registered successfully!")
        else:
            print("Registration failed.")

    def login(self, db, password):
        query = "SELECT * FROM users WHERE name = %s AND password = %s"
        params = (self.name, password)
        result = db.execute_query(query, params)
        if result:
            print(f"Welcome, {self.name}!")
            return True
        else:
            print("Invalid credentials.")
            return False