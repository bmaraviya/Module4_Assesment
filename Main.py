from Customer import Customer
from Product import Product

def menu():
    customer_bill_no = None

    while True:
        print("\n\tBilling system Menu")
        print("\n\t1. Add Customer")
        print("\t2. Add Product")
        print("\t3. Generate Bill")
        print("\t4. Exit")
        print()

        choice = input("Enter your Choice:")

        if choice == "1":
            name = input("Enter your Name:")
            phone = input("Enter your PhoneNo:")
            customer = Customer(name,phone)
            customer.add_customer()
            customer_bill_no = customer.add_customer()
        elif choice == "2":
            if customer_bill_no is not None:
                bill_no = input("Enter Bill No: ")
                item_name = input("Enter Item Name: ")
                price = float(input("Enter Price: "))
                quantity = int(input("Enter Quantity: "))
                product = Product(bill_no, item_name, price, quantity)
                product.add_product()
            else:
                print("Please add a customer first.")
        elif choice == "3":
            pass
        elif choice == "4":
            print("Exit...")
            break
        else:
            print("Invalid Choice")

menu()
    