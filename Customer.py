from Connection import conn

class Customer:
    def __init__(self,name,phone):
        if conn is None:
            print("No database connection. Exiting...")
            return 
        self.name = name
        self.phone = phone
        self.conn = conn
        self.cur = self.conn.cursor()

    def add_customer(self):
        if self.conn is None: 
            print("Cannot add customer. No database connection.")
            return
        query = "insert into Customer(Name,Phone) values(%s,%s)"
        try:
            self.cur.execute(query,(self.name,self.phone))
            self.conn.commit()
            print("Customer Record Inserted...")
            return self.bill_no 
        except Exception as e:
            print(e)

