from Connection import conn

class Product:
    def __init__(self, bill_no, item_name, price, quantity):
        if conn is None:
            print("No database connection. Exiting...")
            return  
        self.bill_no = bill_no
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        self.conn = conn
        self.cur = self.conn.cursor()

    def add_product(self):
        if self.conn is None:  
            print("Cannot add product. No database connection.")
            return
        query = "insert into Product(BillNo, Item_Name, Price, Quantity) values (%s, %s, %s, %s)"
        try:
            self.cur.execute(query, (self.bill_no, self.item_name, self.price, self.quantity))
            self.conn.commit()
            print(f"Product {self.item_name} added to BillNo {self.bill_no}.")
        except Exception as e:
            print(e)
