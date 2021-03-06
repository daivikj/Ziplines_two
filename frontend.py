from tkinter import *
from tkinter.ttk import *
from connector import *

LARGE_FONT=("Verdana",20)

class Ziplines(Tk):
	

	def __init__(self,*args,**kwargs):

		Tk.__init__(self,*args,**kwargs)

		Tk.configure(self)
		
		container=Frame(self)

		container.grid()
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)
		

		self.geometry("800x600")
		self.frames={}
		#initialization of frames in the dictionary with key as the frame name and object returned as the value
		for F in (Home,Seller_info,Add_Products,Add_Employees,Add_Customers,Add_Orders,Display,display_prod_name_price,emp_search_by_name,emp_search_by_dob,display_address,Login):
			frame=F(parent=container,controller=self)
			self.frames[F]=frame
			frame.grid(row=0,column=0,sticky="nsew")
			
		
		self.show_frame(Login)
		#code to display the frame required 
	def show_frame(self,cont):
		frame=self.frames[cont]
		frame.tkraise()


class Login(Frame):

	def __init__(self,parent,controller):

		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Login", font=LARGE_FONT )
		label.grid(row=1, column=2, padx=10,pady=10)

		self.password=Entry(self,width=30,show="*")
		self.password.grid(row=3,column=3,padx=10,pady=10)


		button1=Button(self,text="Login",command=self.access)
		button1.grid(row =4, column = 3, padx=20, pady =20)
		

	def access(self):

		self.passwd=self.password.get()
		self.password.delete(0,"end")

		if self.passwd == "root":

			self.controller.show_frame(Home)

		else:
			 self.controller.show_frame(Login)	
		



class Home(Frame):

	def __init__(self,parent,controller):

		Frame.__init__(self,parent)
		self.controller=controller


		label = Label(self, text="Home", font=LARGE_FONT )
		label.grid(row=1, column=2, padx=10,pady=10)
		
		
		button1=Button(self,text="Products",command=lambda:controller.show_frame(Add_Products))
		button2=Button(self,text="Employees",command=lambda:controller.show_frame(Add_Employees))
		# button3=Button(self,text="Add Products",command=lambda:controller.show_frame(Add_Products))
		button4=Button(self,text="Customers",command=lambda:controller.show_frame(Add_Customers))		
		button5=Button(self,text="Orders",command=lambda:controller.show_frame(Add_Orders))
		button6=Button(self,text="Seller info",command=lambda:controller.show_frame(Seller_info))

		button7=Button(self,text="Logout",command=lambda:controller.show_frame(Login))


		button1.grid(row =2, column = 1, padx=20, pady =20)
		button2.grid(row = 3, column = 1, padx=20, pady =20)
		# button3.grid(row = 8,column =1,padx=20, pady =20 )
		button4.grid(row = 4,column =1,padx=20, pady =20 )
		button5.grid(row = 5,column =1,padx=20, pady =20 )
		button6.grid(row=6,column=1,padx=20,pady=20)
		button7.grid(row=7,column=1,padx=20,pady=20)

class Seller_info(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Seller Info", font=LARGE_FONT )
		label.grid(row=1, column=2, padx=10,pady=10)

		self.seller_id_label = Label(self, text="Seller ID").grid(row=3,column=1,padx=10,pady=10)

		self.seller_name_label = Label(self, text="Seller Name").grid(row=4,column=1,padx=10,pady=10)

		self.seller_id=Text(self,height=1,width=30)
		self.seller_name=Text(self,height=1,width=30)
		
		self.seller_id.grid(row=3,column=2,padx=10,pady=10)
		self.seller_name.grid(row=4,column=2,padx=10,pady=10)

		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=5,column=1,padx=20,pady=20)	

		self.submit_button=Button(self,text="Submit",command=self.add_seller)
		self.submit_button.grid(row=5,column=2,padx=20,pady=20)

		self.select_button=Button(self,text="Delete",command=self.select_item)
		self.select_button.grid(row=5,column=3,padx=10,pady=10)
	    
		self.tree=Treeview( self, columns=('#1','#2'))
		self.tree.heading('#1',text='ID')
		self.tree.heading('#2',text='Name')
		
		self.tree.column('#1',stretch=YES,anchor=CENTER)
		self.tree.column('#2',stretch=YES,anchor=CENTER)
		self.tree.grid(row=2, column=1 ,padx=300,pady=10,columnspan=3, sticky='nsew')
		self.tree['show']='headings'

		self.treeview=self.tree

		sellers=get_seller()

		for i in sellers:

			self.tree.insert("",'end',values=i)

	def select_item(self):
		 
		self.curItem = self.tree.focus()
		self.dict_item=self.tree.item(self.curItem)
		self.seller_list=[]
		self.seller_list=self.dict_item.get('values')
		self.seller_id=self.seller_list[0]
		

		delete_seller(self.seller_id)	

		selected_items = self.treeview.selection()
		
		for selected_item in selected_items:
			self.treeview.delete(selected_item)

	def add_seller(self):

		self.sid=self.seller_id.get("1.0","end-1c")
		self.sname=self.seller_name.get("1.0","end-1c")
		
		self.seller_id.delete("1.0","end")
		self.seller_name.delete("1.0","end")

		create_seller(self.sid,self.sname)
		self.treeview.insert("",'end',values=(self.sid,self.sname))


class Add_Products(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Products", font=LARGE_FONT )
		label.grid(row=1, column=3, padx=10,pady=10)

		self.product_id_label=Label(self,text="ID of products")
		self.product_name_label=Label(self,text="Name of Product")
		self.product_price_label=Label(self,text="Price of Product")
		self.seller_id_label=Label(self,text="ID of seller")
		
		self.product_id=Text(self,height=1,width=30)
		self.product_name=Text(self,height=1,width=30)
		self.product_price=Text(self,height=1,width=30)
		# self.seller_id=Text(self,height=1,width=30)

		option=['']
		seller_ids=get_seller_id()

		for r in seller_ids:
			option.append(r)

		options = list(set(option))		#to obtain only unique events 
		self.variable = StringVar(self)
		self.variable.set(options[0])		#Setting the default event
		self.select = OptionMenu(self, self.variable,*options,command=self.get_value).grid(row =8,column =3,padx=10,pady=10)
		
	
		self.product_id_label.grid(row=5,column=2,padx=10,pady=10)
		self.product_name_label.grid(row=6,column=2,padx=10,pady=10)
		self.product_price_label.grid(row=7,column=2,padx=10,pady=10)
		self.seller_id_label.grid(row=8,column=2,padx=10,pady=10)

		self.product_id.grid(row=5,column=3,padx=10,pady=10)
		self.product_name.grid(row=6,column=3,padx=10,pady=10)
		self.product_price.grid(row=7,column=3,padx=10,pady=10)
		# self.seller_id.grid(row=6,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=9,column=2,padx=20,pady=20)

		self.display_button=Button(self,text="Display Seller Name",command=lambda:controller.show_frame(Display))
		self.display_button.grid(row=8,column=4,padx=10, pady=10)

		self.submit_button=Button(self,text="Submit",command=self.add_product)
		self.submit_button.grid(row=9,column=3,padx=20,pady=20)

		self.select_button=Button(self,text="Delete",command=self.select_item)
		self.select_button.grid(row=5,column=4,padx=10,pady=10)

		self.search_button=Button(self,text="Search",command=lambda:controller.show_frame(display_prod_name_price))
		self.search_button.grid(row=2,column=4,padx=10,pady=10)

		self.update_button=Button(self,text="Update",command=self.update_products)
		self.update_button.grid(row=6,column=4,padx=10,pady=10)

		self.apply_button=Button(self,text="Apply Changes",command=self.apply_update)
		self.apply_button.grid(row=7,column=4,padx=10,pady=10)



		self.tree=Treeview( self, columns=('#1','#2','#3', '#4'))
		self.tree.heading('#1',text='ID')
		self.tree.heading('#2',text='Name')
		self.tree.heading('#3',text='seller id')
		self.tree.heading('#4',text='Price')

		self.tree.column('#1',stretch=YES,anchor=CENTER)
		self.tree.column('#2',stretch=YES,anchor=CENTER)
		self.tree.column('#3', stretch=YES,anchor=CENTER)
		self.tree.column('#4', stretch=YES,anchor=CENTER)
		self.tree.grid(row=2, column=2 ,padx=10,pady=10,columnspan=2, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree


		products=get_products()

		for i in products:
			self.tree.insert("",END,values=i)

			

		

	def get_value(self,value):

		self.id=value[0]
		
			
	def add_product(self):

		if (len(self.product_id.get('1.0','end-1c')) or len(self.product_name.get("1.0","end-1c")) 
			or len(self.product_price.get("1.0","end-1c")) ) == 0:

			self.popup=messagebox.showwarning('warning','incomplete info')



		else:	

			self.pid=self.product_id.get("1.0","end-1c")
			self.pname=self.product_name.get("1.0","end-1c")
			self.pprice=self.product_price.get("1.0","end-1c")
			self.sid=self.id
			
			self.p_price=int(self.pprice)


			self.product_id.delete("1.0","end")
			self.product_name.delete("1.0","end")
			self.product_price.delete("1.0","end")
					# self.seller_id.delete("1.0","end")

			if self.p_price<0:
				self.p_price=0

			self.pprice=str(self.p_price)

			create_products(self.pid,self.pname,self.pprice,self.sid)
				
							

			self.treeview.insert('', 'end', values=( self.pid,self.pname,self.sid,self.pprice))

	def select_item(self):
		 
		self.curItem = self.tree.focus()
		print (self.tree.item(self.curItem))
		self.dict_item=self.tree.item(self.curItem)
		print(type(self.dict_item))
		self.product_list=[]
		self.product_list=self.dict_item.get('values')
		print(self.product_list)
		self.product_id=self.product_list[0]
		

		delete_product(self.product_id)	

		selected_items = self.treeview.selection()
		
		for selected_item in selected_items:
			self.treeview.delete(selected_item)

	def update_products(self):

		self.curItem = self.tree.focus()
		print (self.tree.item(self.curItem))
		self.dict_item=self.tree.item(self.curItem)
		print(type(self.dict_item))
		self.product_list=[]
		self.product_list=self.dict_item.get('values')
		print(self.product_list)
		self.prod_id=self.product_list[0]
		self.prod_name=self.product_list[1]
		self.prod_seller_id=self.product_list[2]
		self.prod_price=self.product_list[3]

		self.product_id.insert('end',self.prod_id)
		self.product_name.insert('end',self.prod_name)
		self.product_price.insert('end',self.prod_price)
	
	def apply_update(self):

		self.pid=self.product_id.get("1.0","end-1c")
		self.pname=self.product_name.get("1.0","end-1c")
		self.pprice=self.product_price.get("1.0","end-1c")
		self.sid=self.id

		self.product_id.delete("1.0","end")
		self.product_name.delete("1.0","end")
		self.product_price.delete("1.0","end")

		self.new_product=update_product(self.pid,self.pname,self.pprice,self.sid)
		print(self.new_product)

		selected_items = self.treeview.selection()
		
		for selected_item in selected_items:
			self.treeview.delete(selected_item)

		self.treeview.insert('', 'end', values=( self.pid,self.pname,self.sid,self.pprice))	

class display_prod_name_price(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Search Products", font=LARGE_FONT )
		label.grid(row=1, column=2, padx=10,pady=10)

		self.product_name_label=Label(self,text="Product name").grid(row=2,column=1,padx=10,pady=10)
		self.product_price_label=Label(self,text="Product price").grid(row=3,column=1,padx=10,pady=10)

		self.prod_name=Text(self,height=1,width=15)
		self.prod_price=Text(self,height=1,width=15)

		self.prod_name.grid(row=2,column=2,padx=10,pady=10)
		self.prod_price.grid(row=3,column=2,padx=10,pady=10)

		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Add_Products))
		self.back_button.grid(row=4,column=1,padx=20,pady=20)	

		self.submit_button=Button(self,text="Submit",command=self.display)
		self.submit_button.grid(row=4,column=2,padx=20,pady=20)

	def display(self):

		self.prodname=self.prod_name.get("1.0","end-1c")
		self.prodprice=self.prod_price.get("1.0","end-1c")

		self.prod_name.delete("1.0","end")
		self.prod_price.delete("1.0","end")

		self.tree=Treeview( self, columns=('#1','#2','#3', '#4'))
		self.tree.heading('#1',text='ID')
		self.tree.heading('#2',text='Name')
		self.tree.heading('#3',text='Seller ID')
		self.tree.heading('#4',text='Price')

		self.tree.column('#1',stretch=YES,anchor=CENTER)
		self.tree.column('#2',stretch=YES,anchor=CENTER)
		self.tree.column('#3', stretch=YES,anchor=CENTER)
		self.tree.column('#4', stretch=YES,anchor=CENTER)


		self.tree.grid(row=10, column=4 ,padx=10,pady=10,columnspan=2, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree

		prods=search_products(self.prodname,self.prodprice)
		
		for i in prods:
			self.tree.insert('','end',values=i)



class Display(Frame):
	
	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Product Seller Name", font=LARGE_FONT )
		label.grid(row=1, column=2, padx=10,pady=10)

		self.tree=Treeview( self, columns=('#1','#2','#3', '#4'))
		self.tree.heading('#1',text='Product ID')
		self.tree.heading('#2',text='Product Name')
		self.tree.heading('#3',text='Seller ID')
		self.tree.heading('#4',text='Seller Name')

		self.tree.column('#1',stretch=YES,anchor=CENTER)
		self.tree.column('#2',stretch=YES,anchor=CENTER)
		self.tree.column('#3', stretch=YES,anchor=CENTER)
		self.tree.column('#4', stretch=YES,anchor=CENTER)

		self.tree.grid(row=1, column=1 ,padx=10,pady=10,columnspan=2, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree

		join=get_seller_product()
		
		for i in join:
			self.tree.insert("",END,values=i)

		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Add_Products))
		self.back_button.grid(row=2,column=2,padx=20,pady=20)


		
class Add_Employees(Frame):
	
	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Employees", font=LARGE_FONT )
		label.grid(row=1, column=1, padx=100,pady=10)

		self.emp_id_label=Label(self,text="Id of Employee")
		self.emp_name_label=Label(self,text="Name of Employee")
		self.emp_gender_label=Label(self,text="Employee Gender")
		self.emp_dob_label=Label(self,text="Employee Date of Birth")
		self.emp_salary_label=Label(self,text="Employee salary")
		self.emp_phno_label=Label(self,text="Phone Number")
		
		self.emp_id=Text(self,height=1,width=30)
		self.emp_name=Text(self,height=1,width=30)

		self.var=StringVar()

		self.r1=Radiobutton(self,text="Male",variable=self.var,value="M",command=self.selected).grid(row=5,column=2,padx=10,pady=10)
		self.r2=Radiobutton(self,text="Female",variable=self.var,value="F",command=self.selected).grid(row=6,column=2,padx=10,pady=10)

		self.emp_dob=Text(self,height=1,width=30)
		self.emp_salary=Text(self,height=1,width=30)
		self.emp_phno=Text(self,height=1,width=30)
		
		self.emp_id_label.grid(row=3,column=1,padx=10,pady=10)
		self.emp_name_label.grid(row=4,column=1,padx=10,pady=10)
		self.emp_gender_label.grid(row=5,column=1,padx=10,pady=10)
		self.emp_dob_label.grid(row=7,column=1,padx=10,pady=10)
		self.emp_salary_label.grid(row=8,column=1,padx=10,pady=10)
		self.emp_phno_label.grid(row=9,column=1,padx=10,pady=10)

		self.emp_id.grid(row=3,column=2,padx=10,pady=10)
		self.emp_name.grid(row=4,column=2,padx=10,pady=10)
		self.emp_dob.grid(row=7,column=2,padx=10,pady=10)
		self.emp_salary.grid(row=8,column=2,padx=10,pady=10)
		self.emp_phno.grid(row=9,column=2,padx=10,pady=10)
		# self.dob_button.grid(row=5,column=2, sticky='w')


		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=10,column=1,padx=20,pady=20)	

		self.submit_button=Button(self,text="Submit",command=self.add_employee)
		self.submit_button.grid(row=10,column=2,padx=20,pady=20)

		self.select_button=Button(self,text="Delete",command=self.select_item)
		self.select_button.grid(row=3,column=3,padx=20,pady=20)

		self.search_by_name=Button(self,text="Search by name",command=lambda:controller.show_frame(emp_search_by_name))
		self.search_by_name.grid(row=6,column=3,padx=20,pady=20)

		self.search_by_dob=Button(self,text="Search by name and DOB",command=lambda:controller.show_frame(emp_search_by_dob))
		self.search_by_dob.grid(row=7,column=3,padx=20,pady=20)

		self.update_button=Button(self,text="Update",command=self.update_employee)
		self.update_button.grid(row=4,column=3,padx=10,pady=10)

		self.apply_button=Button(self,text="Apply Changes",command=self.apply_emp_update)
		self.apply_button.grid(row=5,column=3,padx=10,pady=10)

		self.tree=Treeview( self, columns=('#1','#2','#3', '#4','#5','#6'))
		self.tree.heading('#1',text='ID')
		self.tree.heading('#2',text='Name')
		self.tree.heading('#3',text='Gender')
		self.tree.heading('#4',text='DOB')
		self.tree.heading('#5',text='Salary')
		self.tree.heading('#6',text='Phone')

		self.tree.column('#1',stretch=YES,anchor=CENTER)
		self.tree.column('#2',stretch=YES,anchor=CENTER)
		self.tree.column('#3', stretch=YES,anchor=CENTER)
		self.tree.column('#4', stretch=YES,anchor=CENTER)
		self.tree.column('#5', stretch=YES,anchor=CENTER)
		self.tree.column('#6', stretch=YES,anchor=CENTER)

		self.tree.grid(row=2, column=1 ,padx=50,pady=10,columnspan=2, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree

		employees=get_employees()
		
		for i in employees:
			self.tree.insert("",END,values=i)

	def selected(self):
		
		self.gender=self.var.get()		

	def add_employee(self):

			
		self.eid=self.emp_id.get("1.0","end-1c")
		self.ename=self.emp_name.get("1.0","end-1c")
		# self.egender=self.emp_gender.get("1.0","end-1c")
		self.edob=self.emp_dob.get("1.0","end-1c")
		self.esalary=self.emp_salary.get("1.0","end-1c")
		self.esal=int(self.esalary)

		
		self.ephno=self.emp_phno.get("1.0","end-1c")
		self.egender=self.gender

		self.emp_id.delete("1.0","end")
		self.emp_name.delete("1.0","end")
		# self.emp_gender.delete("1.0","end")
		self.emp_dob.delete("1.0","end")
		self.emp_salary.delete("1.0","end")
		self.emp_phno.delete("1.0","end")


		if self.esal<10000:
			self.esal=10000

		self.esalary=str(self.esal)	

		create_employees(self.eid, self.ename, self.egender, self.edob, self.esalary, self.ephno)
		self.treeview.insert("",'end',values=(self.eid, self.ename, self.egender, self.edob, self.esalary, self.ephno))

	def select_item(self):
		 
		self.curItem = self.tree.focus()
		print (self.tree.item(self.curItem))
		self.dict_item=self.tree.item(self.curItem)
		print(type(self.dict_item))
		self.employee_list=[]
		self.employee_list=self.dict_item.get('values')
		print(self.employee_list)
		self.employee_id=self.employee_list[0]
		
		delete_employee(self.employee_id)
		
		selected_items = self.treeview.selection()
		
		for selected_item in selected_items:
			self.treeview.delete(selected_item)

	def update_employee(self):

		self.curItem = self.tree.focus()
		print (self.tree.item(self.curItem))
		self.dict_item=self.tree.item(self.curItem)
		print(type(self.dict_item))
		self.employee_list=[]
		self.employee_list=self.dict_item.get('values')
		print(self.employee_list)
		self.employee_id=self.employee_list[0]
		self.employee_name=self.employee_list[1]
		self.employee_gender=self.employee_list[2]
		self.employee_dob=self.employee_list[3]
		self.employee_salary=self.employee_list[4]
		self.employee_phno=self.employee_list[5]

		self.emp_id.insert('end',self.employee_id)
		self.emp_name.insert('end',self.employee_name)
		self.emp_dob.insert('end',self.employee_dob)
		self.emp_salary.insert('end',self.employee_salary)
		self.emp_phno.insert('end',self.employee_phno)
	
	def apply_emp_update(self):

		self.eid=self.emp_id.get("1.0","end-1c")
		self.ename=self.emp_name.get("1.0","end-1c")
		# self.egender=self.emp_gender.get("1.0","end-1c")
		self.edob=self.emp_dob.get("1.0","end-1c")
		self.esalary=self.emp_salary.get("1.0","end-1c")
		self.ephno=self.emp_phno.get("1.0","end-1c")
		self.egender=self.gender

		self.emp_id.delete("1.0","end")
		self.emp_name.delete("1.0","end")
		# self.emp_gender.delete("1.0","end")
		self.emp_dob.delete("1.0","end")
		self.emp_salary.delete("1.0","end")
		self.emp_phno.delete("1.0","end")

		update_employee(self.eid,self.ename,self.egender,self.edob,self.esalary,self.ephno)

		selected_items = self.treeview.selection()
		
		for selected_item in selected_items:
			self.treeview.delete(selected_item)

		self.treeview.insert('', 'end', values=( self.eid,self.ename,self.egender,self.edob,self.esalary,self.ephno))			


class emp_search_by_name(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		self.search_label=Label(self,text="Enter the name")
		self.search=Text(self,height=1,width=30)

		self.search_label.grid(row=1,column=1,padx=10,pady=10)
		self.search.grid(row=1,column=2,padx=10,pady=10)

		self.search_by_name=Button(self,text="Search",command=self.search_name)
		self.search_by_name.grid(row=2,column=2,padx=20,pady=20)

		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Add_Employees))
		self.back_button.grid(row=3,column=2,padx=20,pady=20)

	def search_name(self):

		self.ename=self.search.get("1.0","end-1c")
		self.search.delete("1.0","end")

		self.tree=Treeview( self, columns=('#1','#2','#3', '#4','#5','#6'))
		self.tree.heading('#1',text='ID')
		self.tree.heading('#2',text='Name')
		self.tree.heading('#3',text='Gender')
		self.tree.heading('#4',text='dob')
		self.tree.heading('#5',text='salary')
		self.tree.heading('#6',text='Phone')

		self.tree.column('#1',stretch=YES,anchor=CENTER)
		self.tree.column('#2',stretch=YES,anchor=CENTER)
		self.tree.column('#3', stretch=YES,anchor=CENTER)
		self.tree.column('#4', stretch=YES,anchor=CENTER)
		self.tree.column('#5', stretch=YES,anchor=CENTER)
		self.tree.column('#6', stretch=YES,anchor=CENTER)

		self.tree.grid(row=4, column=1 ,padx=10,pady=10,columnspan=2, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree

		employees=emp_search_name(self.ename)
		
		for i in employees:
			self.tree.insert("",END,values=i)

		self.treeview.insert("",'end',values=(self.eid, self.ename, self.egender, self.edob, self.esalary, self.ephno))

class emp_search_by_dob(Frame):

	def __init__(self,parent,controller):

		Frame.__init__(self,parent)
		self.controller=controller

		self.name_label=Label(self,text="Enter the name")
		self.name=Text(self,height=1,width=30)

		self.dob_label=Label(self,text="Enter the DOB")
		self.dob=Text(self,height=1,width=30)

		self.name_label.grid(row=1,column=1,padx=10,pady=10)
		self.dob_label.grid(row=2,column=1,padx=10,pady=10)

		self.name.grid(row=1,column=2,padx=10,pady=10)
		self.dob.grid(row=2,column=2,padx=10,pady=10)

		self.search=Button(self,text="Search",command=self.search_dob)
		self.search.grid(row=3,column=2,padx=20,pady=20)

		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Add_Employees))
		self.back_button.grid(row=3,column=1,padx=20,pady=20)

	def search_dob(self):

		self.ename=self.name.get("1.0","end-1c")
		self.name.delete("1.0","end")
		self.edob=self.dob.get("1.0","end-1c")
		self.dob.delete("1.0","end")

		self.tree=Treeview( self, columns=('#1','#2','#3', '#4','#5','#6'))
		self.tree.heading('#1',text='ID')
		self.tree.heading('#2',text='Name')
		self.tree.heading('#3',text='Gender')
		self.tree.heading('#4',text='dob')
		self.tree.heading('#5',text='salary')
		self.tree.heading('#6',text='Phone')

		self.tree.column('#1',stretch=YES,anchor=CENTER)
		self.tree.column('#2',stretch=YES,anchor=CENTER)
		self.tree.column('#3', stretch=YES,anchor=CENTER)
		self.tree.column('#4', stretch=YES,anchor=CENTER)
		self.tree.column('#5', stretch=YES,anchor=CENTER)
		self.tree.column('#6', stretch=YES,anchor=CENTER)

		self.tree.grid(row=4, column=1 ,padx=10,pady=10,columnspan=2, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree

		employees=emp_search_dob(self.ename, self.edob)
		
		for i in employees:
			self.tree.insert("",END,values=i)

		self.treeview.insert("",'end',values=(self.eid, self.ename, self.egender, self.edob, self.esalary, self.ephno))


class Add_Customers(Frame):

	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Customers", font=LARGE_FONT )
		label.grid(row=1, column=2, padx=10,pady=10)

		self.cust_id_label=Label(self,text="ID of customer")
		self.cust_name_label=Label(self,text="Name of customer")
		self.cust_phno_label=Label(self,text="Phone Number")
		self.cust_address_label=Label(self,text="Address")
		
		self.cust_id=Text(self,height=1,width=30)
		self.cust_name=Text(self,height=1,width=30)
		self.cust_phno=Text(self,height=1,width=30)
		self.cust_address=Text(self,height=10,width=30)
		
		self.cust_id_label.grid(row=3,column=1,padx=10,pady=10)
		self.cust_name_label.grid(row=4,column=1,padx=10,pady=10)
		self.cust_phno_label.grid(row=5,column=1,padx=10,pady=10)
		self.cust_address_label.grid(row=6,column=1,padx=10,pady=10)

		self.cust_id.grid(row=3,column=2,padx=10,pady=10)
		self.cust_name.grid(row=4,column=2,padx=10,pady=10)
		self.cust_phno.grid(row=5,column=2,padx=10,pady=10)
		self.cust_address.grid(row=6,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=7,column=1,padx=20,pady=20) 		

		self.submit_button = Button(self,text="Submit",command=self.add_customer)
		self.submit_button.grid(row=7,column=2,padx=20,pady=20)

		self.update_button=Button(self,text="Update",command=self.update_customer)
		self.update_button.grid(row=3,column=3,padx=10,pady=10)

		self.apply_button=Button(self,text="Apply Changes",command=self.apply_cust_update)
		self.apply_button.grid(row=4,column=3,padx=10,pady=10)

		self.select_button=Button(self,text="Delete",command=self.select_item)
		self.select_button.grid(row=5,column=3,padx=20,pady=20)

		self.tree=Treeview( self, columns=('#1','#2','#3', '#4'))
		self.tree.heading('#1',text='ID')
		self.tree.heading('#2',text='Name')
		self.tree.heading('#3',text='Phone')
		self.tree.heading('#4',text='Address')

		self.tree.column('#1',stretch=YES,anchor=CENTER)
		self.tree.column('#2',stretch=YES,anchor=CENTER)
		self.tree.column('#3', stretch=YES,anchor=CENTER)
		self.tree.column('#4', stretch=YES,anchor=CENTER)


		self.tree.grid(row=2, column=1,padx=100,pady=10,columnspan=2, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree

		customers=get_customers()

		for i in customers:

			self.tree.insert("",END,values=i)


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
		self.treeview.insert("",'end',values=(self.cid,self.cname,self.cphno,self.caddress))

	def select_item(self):
		 
		self.curItem = self.tree.focus()
		print (self.tree.item(self.curItem))
		self.dict_item=self.tree.item(self.curItem)
		print(type(self.dict_item))
		self.customer_list=[]
		self.customer_list=self.dict_item.get('values')
		print(self.customer_list)
		self.customer_id=self.customer_list[0]
		
		delete_customers(self.customer_id)
		
		selected_items = self.treeview.selection()
		
		for selected_item in selected_items:
			self.treeview.delete(selected_item)
	
	def update_customer(self):

		self.curItem = self.tree.focus()
		print (self.tree.item(self.curItem))
		self.dict_item=self.tree.item(self.curItem)
		print(type(self.dict_item))
		self.customer_list=[]
		self.customer_list=self.dict_item.get('values')
		print(self.customer_list)
		
		self.cus_id=self.customer_list[0]
		self.cus_name=self.customer_list[1]
		self.cus_phno=self.customer_list[2]
		self.cus_addres=self.customer_list[3]


		self.cust_id.insert('end',self.cus_id)
		self.cust_name.insert('end',self.cus_name)
		self.cust_phno.insert('end',self.cus_phno)
		self.cust_address.insert('end',self.cus_addres)
		
	
	def apply_cust_update(self):

		self.cid = self.cust_id.get("1.0","end-1c")
		self.cname = self.cust_name.get("1.0","end-1c")
		self.cphno = self.cust_phno.get("1.0","end-1c")
		self.caddress = self.cust_address.get("1.0","end-1c")

		self.cust_id.delete("1.0","end")
		self.cust_name.delete("1.0","end")
		self.cust_phno.delete("1.0","end")
		self.cust_address.delete("1.0","end")

		update_customer(self.cid, self.cname, self.cphno, self.caddress)
		
		selected_items = self.treeview.selection()
		
		for selected_item in selected_items:
			self.treeview.delete(selected_item)

		self.treeview.insert('', 'end', values=( self.cid, self.cname, self.cphno, self.caddress))		


class Add_Orders(Frame):
	
	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Orders", font=LARGE_FONT )
		label.grid(row=1, column=3, padx=10,pady=10)

		self.order_id_label=Label(self,text="Id of Order")
		self.product_id_label=Label(self,text="Id of Product")
		self.product_name_label=Label(self,text="Name of Product")
		self.seller_id_label=Label(self,text="Id of Seller")
		self.seller_name_label=Label(self,text="Name of Seller")
		self.price_label=Label(self,text="Price of the Product")
		self.customer_id_label=Label(self,text="Id of Customer")
		self.customer_name_label=Label(self,text="Name of Customer")
		self.status_label=Label(self,text="Status")
		self.employee_name_label=Label(self,text="Name of Employee")
		

		self.order_id=Text(self,height=1,width=30)
		# self.product_id=Text(self,height=1,width=30)
		self.product_name=Text(self,height=1,width=30)
		# self.seller_id=Text(self,height=1,width=30)
		self.seller_name=Text(self,height=1,width=30)
		self.price=Text(self,height=1,width=30)
		# self.customer_id=Text(self,height=1,width=30)
		self.customer_name=Text(self,height=1,width=30)
		self.status=Text(self,height=1,width=30)
		self.employee_name=Text(self,height=1,width=30)
		
		self.order_id_label.grid(row=3,column=1,padx=10,pady=10)
		self.product_id_label.grid(row=4,column=1,padx=10,pady=10)
		self.product_name_label.grid(row=5,column=1,padx=10,pady=10)
		self.seller_id_label.grid(row=6,column=1,padx=10,pady=10)
		self.seller_name_label.grid(row=7,column=1,padx=10,pady=10)
		self.price_label.grid(row=8,column=1,padx=10,pady=10)
		self.customer_id_label.grid(row=9,column=1,padx=10,pady=10)
		self.customer_name_label.grid(row=10,column=1,padx=10,pady=10)
		self.status_label.grid(row=11,column=1,padx=10,pady=10)
		self.employee_name_label.grid(row=12,column=1,padx=10,pady=10)

		self.order_id.grid(row=3,column=2,padx=10,pady=10)
		# self.product_id.grid(row=3,column=2,padx=10,pady=10)
		self.product_name.grid(row=5,column=2,padx=10,pady=10)
		# self.seller_id.grid(row=5,column=2,padx=10,pady=10)
		self.seller_name.grid(row=7,column=2,padx=10,pady=10)
		self.price.grid(row=8,column=2,padx=10,pady=10)
		# self.customer_id.grid(row=8,column=2,padx=10,pady=10)
		self.customer_name.grid(row=10,column=2,padx=10,pady=10)
		self.status.grid(row=11,column=2,padx=10,pady=10)
		self.employee_name.grid(row=12,column=2,padx=10,pady=10)
	
		self.back_button=Button(self,text="Back",command=lambda:controller.show_frame(Home))
		self.back_button.grid(row=12,column=5,padx=20,pady=20)	

		self.submit_button=Button(self,text="Submit",command=self.add_orders)
		self.submit_button.grid(row=11,column=5,padx=20,pady=20)

		self.select_button=Button(self,text="Delete",command=self.select_item)
		self.select_button.grid(row=3,column=5,padx=20,pady=20)

		self.update_button=Button(self,text="Update",command=self.update_order)
		self.update_button.grid(row=5,column=5,padx=10,pady=10)

		self.apply_button=Button(self,text="Apply Changes",command=self.apply_order_update)
		self.apply_button.grid(row=7,column=5,padx=10,pady=10)

		self.display_address_button=Button(self,text="Display Address",command=lambda:controller.show_frame(display_address))
		self.display_address_button.grid(row=9,column=5,padx=20,pady=20)

		'''product_id option menu'''

		product_option=['']
		product_ids=get_product_id()

		for r in product_ids:
			product_option.append(r)

		product_options = list(set(product_option))		#to obtain only unique events 
		self.product_variable = StringVar(self)
		self.product_variable.set(product_options[0])		#Setting the default event
		self.product_select = OptionMenu(self, self.product_variable,*product_options,command=self.product_get_value).grid(row =4,column =2,padx=10,pady=10)

		'''seller_id option menu'''

		option=['']
		seller_ids=get_seller_id()

		for r in seller_ids:
			option.append(r)

		options = list(set(option))		#to obtain only unique events 
		self.variable = StringVar(self)
		self.variable.set(options[0])		#Setting the default event
		self.select = OptionMenu(self, self.variable,*options,command=self.get_value).grid(row =6,column =2,padx=10,pady=10)

		'''customer_id option menu'''

		customer_option=['']
		customer_ids=get_customer_id()

		for r in customer_ids:
			customer_option.append(r)

		customer_options = list(set(customer_option))		#to obtain only unique events 
		self.customer_variable = StringVar(self)
		self.customer_variable.set(options[0])		#Setting the default event
		self.customer_select = OptionMenu(self, self.customer_variable,*customer_options,command=self.customer_get_value).grid(row =9,column =2,padx=10,pady=10)


		self.tree=Treeview( self, columns=('#1','#2','#3', '#4','#5','#6', '#7', '#8', '#9', '#10'))
		self.tree.heading('#1',text=' Order ID')
		self.tree.heading('#2',text='Product ID')
		self.tree.heading('#3',text='Product Name')
		self.tree.heading('#4',text='Seller ID')
		self.tree.heading('#5',text='Seller Name')
		self.tree.heading('#6',text='Price')
		self.tree.heading('#7',text='Customer ID')
		self.tree.heading('#8',text='Customer Name')
		self.tree.heading('#9',text='Status')
		self.tree.heading('#10',text='Employee Name')

		self.tree.column('#1',stretch=YES,minwidth=0,width=70,anchor=CENTER)
		self.tree.column('#2',stretch=YES,minwidth=0,width=70,anchor=CENTER)
		self.tree.column('#3', stretch=YES,minwidth=0,width=200,anchor=CENTER)
		self.tree.column('#4', stretch=YES,minwidth=0,width=70,anchor=CENTER)
		self.tree.column('#5', stretch=YES,minwidth=0,width=200,anchor=CENTER)
		self.tree.column('#6', stretch=YES,minwidth=0,width=70,anchor=CENTER)
		self.tree.column('#7', stretch=YES,minwidth=0,width=100,anchor=CENTER)
		self.tree.column('#8', stretch=YES,minwidth=0,width=200,anchor=CENTER)
		self.tree.column('#9', stretch=YES,minwidth=0,width=100,anchor=CENTER)
		self.tree.column('#10', stretch=YES,minwidth=0,width=200,anchor=CENTER)

		self.tree.grid(row=2, column=1 ,padx=100,pady=5,columnspan=8, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree

		orders=get_orders()
		
		for i in orders:
			self.tree.insert("",END,values=i)

	def product_get_value(self,value):

		self.prod_id=value[0]
		
		self.prod_name=get_product_name(self.prod_id)
		self.product_name.delete('1.0','end')
		self.product_name.insert('end',self.prod_name)

		self.prod_price=get_product_price(self.prod_id)
		self.price.delete('1.0','end')
		self.price.insert('end',self.prod_price)

	def get_value(self,value):

		self.id=value[0]

		self.sell_name=get_seller_name(self.id)
		self.seller_name.delete('1.0','end')
		self.seller_name.insert('end',self.sell_name)
		
	def customer_get_value(self,value):

		self.cust_id=value[0]	

		self.cust_name=get_customer_name(self.cust_id)
		self.customer_name.delete('1.0','end')
		self.customer_name.insert('end',self.cust_name)

	def add_orders(self):

		self.oid = self.order_id.get("1.0","end-1c")
		# self.pid = self.product_id.get("1.0","end-1c")
		self.pid=self.prod_id
		self.pname = self.product_name.get("1.0","end-1c")
		# self.sid = self.seller_id.get("1.0","end-1c")
		self.sid=self.id
		self.sname = self.seller_name.get("1.0","end-1c")
		self.pprice = self.price.get("1.0","end-1c")
		# self.cid = self.customer_id.get("1.0","end-1c")
		self.cid=self.cust_id
		self.cname = self.customer_name.get("1.0","end-1c")
		self.stat = self.status.get("1.0","end-1c")
		self.ename = self.employee_name.get("1.0","end-1c")

		self.order_id.delete("1.0","end")
		# self.product_id.delete("1.0","end")
		self.product_name.delete("1.0","end")
		# self.seller_id.delete("1.0","end")
		self.seller_name.delete("1.0","end")
		self.price.delete("1.0","end")
		# self.customer_id.delete("1.0","end")
		self.customer_name.delete("1.0","end")
		self.status.delete("1.0","end")
		self.employee_name.delete("1.0","end")

		create_orders(self.oid, self.pid, self.pname, self.sid, self.sname, self.pprice, self.cid, self.cname, self.stat, self.ename)
		self.treeview.insert("",'end',values=(self.oid, self.pid, self.pname, self.sid, self.sname, self.pprice, self.cid, self.cname, self.stat, self.ename))

	def select_item(self):
		 
		self.curItem = self.tree.focus()
		print (self.tree.item(self.curItem))
		self.dict_item=self.tree.item(self.curItem)
		print(type(self.dict_item))
		self.order_list=[]
		self.order_list=self.dict_item.get('values')
		print(self.order_list)
		self.order_id=self.order_list[0]
		
		delete_order(self.order_id)
		
		selected_items = self.treeview.selection()
		
		for selected_item in selected_items:
			self.treeview.delete(selected_item)

	
	def update_order(self):

		self.curItem = self.tree.focus()
		print (self.tree.item(self.curItem))
		self.dict_item=self.tree.item(self.curItem)
		print(type(self.dict_item))
		self.order_list=[]
		self.order_list=self.dict_item.get('values')
		print(self.order_list)
		
		self.ord_id=self.order_list[0]
		self.prod_id=self.order_list[1]
		self.prod_name=self.order_list[2]
		self.sell_id=self.order_list[3]
		self.sell_name=self.order_list[4]
		self.prod_price=self.order_list[5]
		self.cust_id=self.order_list[6]
		self.cust_name=self.order_list[7]
		self.ord_status=self.order_list[8]
		self.emp_name=self.order_list[9]

		self.order_id.insert('end',self.ord_id)
		self.product_name.insert('end',self.prod_name)
		self.seller_name.insert('end',self.sell_name)
		self.price.insert('end',self.prod_price)
		self.customer_name.insert('end',self.cust_name)
		self.status.insert('end',self.ord_status)
		self.employee_name.insert('end',self.emp_name)
		
	
	def apply_order_update(self):

		self.oid = self.order_id.get("1.0","end-1c")
		# self.pid = self.product_id.get("1.0","end-1c")
		self.pid=self.prod_id
		self.pname = self.product_name.get("1.0","end-1c")
		# self.sid = self.seller_id.get("1.0","end-1c")
		self.sid=self.id
		self.sname = self.seller_name.get("1.0","end-1c")
		self.pprice = self.price.get("1.0","end-1c")
		# self.cid = self.customer_id.get("1.0","end-1c")
		self.cid=self.cust_id
		self.cname = self.customer_name.get("1.0","end-1c")
		self.stat = self.status.get("1.0","end-1c")
		self.ename = self.employee_name.get("1.0","end-1c")

		self.order_id.delete("1.0","end")
		# self.product_id.delete("1.0","end")
		self.product_name.delete("1.0","end")
		# self.seller_id.delete("1.0","end")
		self.seller_name.delete("1.0","end")
		self.price.delete("1.0","end")
		# self.customer_id.delete("1.0","end")
		self.customer_name.delete("1.0","end")
		self.status.delete("1.0","end")
		self.employee_name.delete("1.0","end")



		update_order(self.oid, self.pid, self.pname, self.sid, self.sname, self.pprice, self.cid, self.cname, self.stat, self.ename)
		
		selected_items = self.treeview.selection()
		
		for selected_item in selected_items:
			self.treeview.delete(selected_item)

		self.treeview.insert('', 'end', values=(self.oid, self.pid, self.pname, self.sid, self.sname, self.pprice, self.cid, self.cname, self.stat, self.ename))	



class display_address(Frame):
	
	def __init__(self,parent,controller):


		Frame.__init__(self,parent)
		self.controller=controller

		label = Label(self, text="Orders Address", font=LARGE_FONT )
		label.grid(row=1, column=2, padx=10,pady=10)

		self.tree=Treeview( self, columns=('#1','#2','#3', '#4','#5','#6', '#7', '#8', '#9', '#10'))
		self.tree.heading('#1',text=' Order ID')
		self.tree.heading('#2',text='Product Name')
		self.tree.heading('#3',text='Seller Name')
		self.tree.heading('#4',text='Price')
		self.tree.heading('#5',text='Customer Name')
		self.tree.heading('#6',text='Status')
		self.tree.heading('#7',text='Customer Address')

		self.tree.column('#1',stretch=YES,width=0,minwidth=70)
		self.tree.column('#2',stretch=YES,width=0,minwidth=100)
		self.tree.column('#3', stretch=YES,width=0,minwidth=100)
		self.tree.column('#4', stretch=YES,width=0,minwidth=100)
		self.tree.column('#5', stretch=YES,width=0,minwidth=100)
		self.tree.column('#6', stretch=YES,width=0,minwidth=100)
		self.tree.column('#7', stretch=YES)

		self.tree.grid(row=2, column=1 ,padx=200,pady=10,columnspan=4, sticky='nsew')
		self.tree['show']='headings'
		# self.tree.bind('<Button-1>', self.select_item)

		self.treeview = self.tree

		order=get_orders_address()
		
		for i in order:
			self.tree.insert("",END,values=i)

		self.back_button=Button(self,text='Back',command=lambda:controller.show_frame(Add_Orders))
		self.back_button.grid(row=3,column=2,padx=10,pady=10)

app=Ziplines()
app.mainloop()		