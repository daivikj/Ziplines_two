from tkinter import *
from tkinter.ttk import *
from connector import create_seller, create_product, create_employee, create_customer

LARGE_FONT=("Verdana",20)


class Ziplines(Tk):

	def __init__(self,*args,**kwargs):

		Tk.__init__(self,*args,**kwargs)

		container=Frame(self)
		container.grid()
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		self.geometry("800x600")
		self.frames={}
		#initialization of frames in the dictionary with key as the frame name and object returned as the value
		for F in (Home,Seller_info,Products,Add_Products,Employees,Add_Employees,Customers,Add_Customers):
			frame=F(parent=container,controller=self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")
		
		self.show_frame(Home)
		#code to display the frame required 
	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()


class Home(Frame):

	def __init__(self,parent,controller):

		Frame.__init__(self,parent)
		self.controller=controller
		label = Label(self, text="Home", font=LARGE_FONT)
		label.grid(row=2, column=2, padx=10,pady=10)
		button1=Button(self,text="Products",command=lambda:controller.show_frame(Products))
		button2=Button(self,text="Employees",command=lambda:controller.show_frame(Employees))
		button3=Button(self,text="Add_Orders",command=lambda:controller.show_frame(Add_Orders))
		button4=Button(self,text="Customers",command=lambda:controller.show_frame(Customers))		
		button5=Button(self,text="Track_Orders",command=lambda:controller.show_frame(View_Participants))
		button6=Button(self,text="Seller info",command=lambda:controller.show_frame(Seller_info))
		

		button1.grid(row = 3, column = 1, padx=20, pady =20)
		button2.grid(row = 4, column = 1, padx=20, pady =20)
		button3.grid(row = 5, column =1, padx=20, pady =20 )
		button4.grid(row = 6, column =1, padx=20, pady =20 )
		button5.grid(row = 7, column =1, padx=20, pady =20 )
		button6.grid(row = 8, column =1, padx=20, pady=20)


class Products(Frame):

	def __init__(self,parent,controller):
		'''

		'''

		Frame.__init__(self,parent)
		self.controller  = controller
		button1=Button(self,text="Add Product",command=lambda:controller.show_frame(Add_Products))
		button2=Button(self,text="Delete Product",command=lambda:controller.show_frame(View_Participants))
		button3=Button(self,text="display",command=lambda:controller.show_frame(View_Participants))
		button4=Button(self,text="seller info",command=lambda:controller.show_frame(View_Participants))
		
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))#button when pressed, moves back to the startPage
		self.back_button.grid(row=5,column=3,padx=20,pady=20)
		
		button1.grid(row = 1,column =2,padx=20, pady =20 )
		button2.grid(row = 2,column =2,padx=20, pady =20 )
		button3.grid(row = 3,column =2,padx=20, pady =20 )
		button4.grid(row = 4,column =2,padx=20, pady =20 )


class Employees(Frame):

	def __init__(self,parent,controller):
		'''

		'''

		Frame.__init__(self,parent)
		self.controller  = controller
		button1=Button(self,text="Add Employees",command=lambda:controller.show_frame(Add_Employees))
		button2=Button(self,text="Delete Employees",command=lambda:controller.show_frame(View_Participants))
		button3=Button(self,text="Employee Details",command=lambda:controller.show_frame(View_Participants))
		
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))#button when pressed, moves back to the startPage
		self.back_button.grid(row=5,column=6,padx=20,pady=20)
		
		button1.grid(row = 1,column =5,padx=20, pady =20 )
		button2.grid(row = 2,column =5,padx=20, pady =20 )
		button3.grid(row = 3,column =5,padx=20, pady =20 )

class Customers(Frame):

	def __init__(self,parent,controller):
		'''

		'''

		Frame.__init__(self,parent)
		self.controller  = controller
		button1=Button(self,text="Add Customers",command=lambda:controller.show_frame(Add_Customers))
		button2=Button(self,text="Delete Customers",command=lambda:controller.show_frame(View_Participants))
		button3=Button(self,text="Customers Info",command=lambda:controller.show_frame(View_Participants))
		
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))#button when pressed, moves back to the startPage
		self.back_button.grid(row=4,column=6,padx=20,pady=20)
		
		button1.grid(row = 1,column =5,padx=20, pady =20 )
		button2.grid(row = 2,column =5,padx=20, pady =20 )
		button3.grid(row = 3,column =5,padx=20, pady =20 )


class Seller_info(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.seller_id_label = Label(self, text="Enter the seller id")		
		self.seller_name_label = Label(self, text="Enter the seller name")

		self.seller_id = Text(self,height=2,width=30)
		self.seller_name = Text(self,height=2,width=30)

		self.seller_id_label.grid(row=3,column=1,padx=10,pady=10)
		self.seller_name_label.grid(row=4,column=1,padx=10,pady=10)
		self.seller_id.grid(row=3,column=2,padx=10,pady=10)
		self.seller_name.grid(row=4,column=2,padx=10,pady=10)
		
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=5,column=2,padx=20,pady=20)	

		self.submit_button=Button(self,text="Submit",command=self.add_seller)
		self.submit_button.grid(row=5,column=3,padx=20,pady=20)
	
	def add_seller(self):

		self.sid = self.seller_id.get("1.0","end-1c")
		self.sname = self.seller_name.get("1.0","end-1c")

		self.seller_id.delete("1.0","end")
		self.seller_name.delete("1.0","end")

		create_seller(self.sid, self.sname)


class Add_Products(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.prod_id_label=Label(self,text="ID of the product")
		self.prod_name_label=Label(self,text="Name of Product")
		self.seller_id_label=Label(self,text="ID of seller")
		self.prod_price_label=Label(self,text="Price of Product")
		
		self.prod_id=Text(self,height=1,width=30)
		self.prod_name=Text(self,height=1,width=30)
		self.seller_id=Text(self,height=1,width=30)
		self.prod_price=Text(self,height=1,width=30)
		
		self.prod_id_label.grid(row=2,column=1,padx=10,pady=10)
		self.prod_name_label.grid(row=3,column=1,padx=10,pady=10)
		self.seller_id_label.grid(row=4,column=1,padx=10,pady=10)
		self.prod_price_label.grid(row=5,column=1,padx=10,pady=10)

		self.prod_id.grid(row=2,column=2,padx=10,pady=10)
		self.prod_name.grid(row=3,column=2,padx=10,pady=10)
		self.seller_id.grid(row=4,column=2,padx=10,pady=10)
		self.prod_price.grid(row=5,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Products))
		self.back_button.grid(row=6,column=3,padx=20,pady=20)

		self.submit_button=Button(self,text="Submit",command=self.add_product)
		self.submit_button.grid(row=6,column=2,padx=20,pady=20)

	def add_product(self):

		self.pid=self.prod_id.get("1.0","end-1c")
		self.pname=self.prod_name.get("1.0","end-1c")
		self.sid=self.seller_id.get("1.0","end-1c")
		self.pprice=self.prod_price.get("1.0","end-1c")

		self.prod_id.delete("1.0","end")
		self.prod_name.delete("1.0","end")
		self.seller_id.delete("1.0","end")
		self.prod_price.delete("1.0","end")

		create_product(self.pid,self.pname,self.sid,self.pprice)


class Add_Employees(Frame):
	
	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.emp_id_label=Label(self,text="ID of Employee")
		self.emp_name_label=Label(self,text="Name of Employee")
		self.emp_gender_label=Label(self,text="Gender")
		self.emp_dob_label=Label(self,text="Employee Date of Birth")
		self.emp_salary_label=Label(self,text="Employee salary")
		self.emp_phno_label=Label(self,text="Phone Number")
		
		self.emp_id=Text(self,height=2,width=30)
		self.emp_name=Text(self,height=2,width=30)
		self.emp_gender=Text(self,height=2,width=30)
		self.emp_dob=Text(self,height=2,width=30)
		self.emp_salary=Text(self,height=2,width=30)
		self.emp_phno=Text(self,height=2,width=30)
		
		self.emp_id_label.grid(row=2,column=1,padx=10,pady=10)
		self.emp_name_label.grid(row=3,column=1,padx=10,pady=10)
		self.emp_gender_label.grid(row=4,column=1,padx=10,pady=10)
		self.emp_dob_label.grid(row=5,column=1,padx=10,pady=10)
		self.emp_salary_label.grid(row=6,column=1,padx=10,pady=10)
		self.emp_phno_label.grid(row=7,column=1,padx=10,pady=10)

		self.emp_id.grid(row=2,column=2,padx=10,pady=10)
		self.emp_name.grid(row=3,column=2,padx=10,pady=10)
		self.emp_gender.grid(row=4,column=2,padx=10,pady=10)
		self.emp_dob.grid(row=5,column=2,padx=10,pady=10)
		self.emp_salary.grid(row=6,column=2,padx=10,pady=10)
		self.emp_phno.grid(row=7,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Employees))
		self.back_button.grid(row=8,column=3,padx=20,pady=20)	

		self.submit_button = Button(self,text="Submit",command=self.add_employee)
		self.submit_button.grid(row=8,column=2,padx=20,pady=20)

	def add_employee(self):

		self.eid=self.emp_id.get("1.0","end-1c")
		self.ename=self.emp_name.get("1.0","end-1c")
		self.egender=self.emp_gender.get("1.0","end-1c")
		self.edob=self.emp_dob.get("1.0","end-1c")
		self.esalary=self.emp_salary.get("1.0","end-1c")
		self.ephno=self.emp_phno.get("1.0","end-1c")

		self.emp_id.delete("1.0","end")
		self.emp_name.delete("1.0","end")
		self.emp_gender.delete("1.0","end")
		self.emp_dob.delete("1.0","end")
		self.emp_salary.delete("1.0","end")
		self.emp_phno.delete("1.0","end")

		create_employee(self.eid,self.ename,self.egender,self.edob,self.esalary,self.ephno)

class Add_Customers(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.cust_id_label=Label(self,text="ID of customer")
		self.cust_name_label=Label(self,text="Name of customer")
		self.cust_phno_label=Label(self,text="Phone Number")
		self.cust_address_label=Label(self,text="Address")
		
		self.cust_id=Text(self,height=1,width=30)
		self.cust_name=Text(self,height=1,width=30)
		self.cust_phno=Text(self,height=1,width=30)
		self.cust_address=Text(self,height=10,width=30)
		
		self.cust_id_label.grid(row=2,column=1,padx=10,pady=10)
		self.cust_name_label.grid(row=3,column=1,padx=10,pady=10)
		self.cust_phno_label.grid(row=4,column=1,padx=10,pady=10)
		self.cust_address_label.grid(row=5,column=1,padx=10,pady=10)

		self.cust_id.grid(row=2,column=2,padx=10,pady=10)
		self.cust_name.grid(row=3,column=2,padx=10,pady=10)
		self.cust_phno.grid(row=4,column=2,padx=10,pady=10)
		self.cust_address.grid(row=5,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Customers))
		self.back_button.grid(row=6,column=3,padx=20,pady=20) 		

		self.submit_button = Button(self,text="Submit",command=self.add_customer)
		self.submit_button.grid(row=6,column=2,padx=20,pady=20)

	def add_customer(self):

		self.cid = self.cust_id.get("1.0","end-1c")
		self.cname = self.cust_name.get("1.0","end-1c")
		self.cphno = self.cust_phno.get("1.0","end-1c")
		self.caddress = self.cust_address.get("1.0","end-1c")

		self.cust_id.delete("1.0","end")
		self.cust_name.delete("1.0","end")
		self.cust_phno.delete("1.0","end")
		self.cust_address.delete("1.0","end")

		create_customer(self.cid,self.cname,self.cphno,self.caddress)


app=Ziplines()
app.mainloop()