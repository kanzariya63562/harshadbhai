from user import User

class Manager(User):
    def __init__(self, name, pharmacy_name):
        super().__init__(name)s
        self.pharmacy_name = pharmacy_name
        self.__quantity = None  

    def add_medicine(self, db, medicine_name, price):
        query = "INSERT INTO medicines (name, price, added_by, pharmacy_name) VALUES (%s, %s, %s, %s)"
        params = (medicine_name, price, self.name, self.pharmacy_name)
        rows_affected = db.execute_query(query, params)
        if rows_affected > 0:
            print(f"Medicine '{medicine_name}' added successfully!")
        else:
            print("Adding medicine failed.")

    def view_medicines(self, db):
        query = "SELECT * FROM medicines WHERE pharmacy_name = %s"
        params = (self.pharmacy_name,)
        results = db.execute_query(query, params)
        if results:
            print("\nMedicines:")
            print("{:<20} {:<20} {:<10} {:<20}".format("Medicine Name", "Price", "Quantity", "Added By"))
            for medicine in results:
                print("{:<20} {:<20} {:<10} {:<20}".format(
                    medicine[1], medicine[4], self.get_quantity(db, medicine[0]), medicine[3]))
        else:
            print("No medicines found for your pharmacy.")

    def delete_medicine(self, db, medicine_id):
        query = "DELETE FROM medicines WHERE id = %s"
        params = (medicine_id,)
        rows_affected = db.execute_query(query, params)
        if rows_affected > 0:
            print(f"Medicine with ID {medicine_id} deleted successfully!")
        else:
            print(f"Medicine with ID {medicine_id} not found.")

    def get_quantity(self, db, medicine_id):  # Manager can access private quantity
        query = "SELECT quantity FROM medicines WHERE id = %s"
        params = (medicine_id,)
        result = db.execute_query(query, params)
        if result:
            return result[0][0]
        else:
            return 0

    # def set_quantity(self, db, medicine_id):