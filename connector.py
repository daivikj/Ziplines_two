import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="Ziplines"
)

mycursor = mydb.cursor()

def create_seller(sid, sname):

	sql = "INSERT INTO seller(seller_id, seller_name) values (%s, %s)"
	val = (sid, sname)

	mycursor.execute(sql, val)
	mydb.commit()

def create_product(pid, pname, sid, pprice):

	sql = "INSERT INTO products(product_id, product_name, seller_id, price) values (%s, %s, %s, %s)"
	val = (pid, pname, sid, pprice)

	mycursor.execute(sql,val)
	mydb.commit()

def create_employee(eid, ename, egender, edob, esalary, ephno):

	sql = "INSERT INTO employee(employee_id, employee_name, employee_gender, employee_dob, employee_salary, employee_phno) values (%s, %s, %s, %s, %s, %s)"
	val = (eid, ename, egender, edob, esalary, ephno)

	mycursor.execute(sql,val)
	mydb.commit()

def create_customer(cid, cname, cphno, caddress):

	sql = "INSERT INTO customer(customer_id, customer_name, customer_phno, customer_address) values (%s, %s, %s, %s)"
	val = (cid, cname, cphno, caddress)

	mycursor.execute(sql,val)
	mydb.commit()

def get_products():

	sql = "SELECT * FROM products"
	mycursor.execute(sql)
	products=mycursor.fetchall()

	return products