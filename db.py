from Connection import conn

cur = conn.cursor()

create_cust = "create table Customer(BillNo integer primary key auto_increment,Name text,Phone bigint)"

create_pr = "create table Product(Id integer primary key auto_increment, BillNo integer, Item_Name text, Price Decimal(10, 2), Quantity integer, foreign key(BillNo) references Customer(BillNo) ON DELETE CASCADE)"
try:
    cur.execute(create_cust)
    cur.execute(create_pr)
    conn.commit()
    print("Table Created...")
except Exception as e:
    print(e)





