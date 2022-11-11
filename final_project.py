#BLL
import pickle
import tkinter
import tkinter.messagebox
import re

class Customer:
    listCus = []

    def __init__(self):
        self.id = 0
        self.name = ""
        self.age = 0
        self.mob = ""

    @staticmethod
    def saveCustomerinFile():
        fs = open("CusMgt.txt", "wb")
        pickle.dump(Customer.listCus, fs)

    @staticmethod
    def loadCustomerfromFile():
        fs = open("CusMgt.txt", "rb")
        Customer.listCus = pickle.load(fs)

    def addCustomer(self):
        Customer.listCus.append(self)

    def searchCustomer(self, id):
        for i in range(len(Customer.listCus)):
            if (id == Customer.listCus[i].id):
                self.name = Customer.listCus[i].name
                self.age = Customer.listCus[i].age
                self.mob = Customer.listCus[i].mob
                return 1
        return 0

    def modifyCustomer(self):
        for i in range(len(Customer.listCus)):
            if (self.id == Customer.listCus[i].id):
                Customer.listCus[i] = self
                return 1
        return 0

    def deleteCustomer(self, id):
        for i in range(len(Customer.listCus)):
            if (id == Customer.listCus[i].id):
                Customer.listCus.pop(i)
                return 1
        return 0

    @staticmethod
    def showAllCustomer():

        import tkinter
        top = tkinter.Tk()
        top.title("SHOW-DATA")
        top.minsize(200, 300)
        top.configure(background='grey60')

        tkinter.Label(top, text="ID", width=12, bg="skyblue",font=16).grid(row=0, column=0)
        tkinter.Label(top, text="Name", width=12, bg="green",font=16).grid(row=0, column=1)
        tkinter.Label(top, text="Age", width=12, bg="gray",font=16).grid(row=0, column=2)
        tkinter.Label(top, text="Mobile", width=12, bg="pink",font=16).grid(row=0, column=3)

        for i in range(len(Customer.listCus)):
            for k in range(4):
                if k == 0:
                    lblvalueid = tkinter.Label(top, text=Customer.listCus[i].id, width=12,font=12)
                    lblvalueid.grid(row=i + 1, column=k)
                elif k == 1:
                    lblvaluename = tkinter.Label(top, text=Customer.listCus[i].name, width=12,font=12)
                    lblvaluename.grid(row=i + 1, column=k)
                elif k == 2:
                    lblvalueage = tkinter.Label(top, text=Customer.listCus[i].age, width=12,font=12)
                    lblvalueage.grid(row=i + 1, column=k)
                elif k == 3:
                    lblvaluemob = tkinter.Label(top, text=Customer.listCus[i].mob, width=12,font=12)
                    lblvaluemob.grid(row=i + 1, column=k)

        top.mainloop()
        
  
        
        
        

#PL


def btnadd_click():
    
        def btnAdd_Click():
            regex = re.compile(r'\d{10}')
            mob = regex.search(txtMob.get())==None
            
            regex2 = re.compile(r'\d{11,}')
            mob2 = regex2.search(txtMob.get())==None
            
            if(mob2==False):
                mesg = "mobile number must be of 10 digits \nenter the details again\nwith correct mobile number"
                tkinter.messagebox.showinfo("try again",mesg)
            elif(mob==False):
                cus = Customer()
                cus.id = txtId.get()
                cus.name = txtName.get()
                cus.age = txtAge.get()
                cus.mob = txtMob.get()
                cus.addCustomer()
                mes = len(Customer.listCus), "Customer Added Sucessfully"
                tkinter.messagebox.showinfo("Added", mes)
            else:
                mesg = "mobile number must be of 10 digits \nenter the details again\nwith correct mobile number"
                tkinter.messagebox.showinfo("try again",mesg)
    
        add = tkinter.Tk()
        add.title("ADD CUSTOMER")
        add.minsize(250, 250)
        
        
        lblId = tkinter.Label(add, text="ID", width=12,height=2,font=16)
        lblId.grid(row=0, column=0, columnspan=2)

        lblName = tkinter.Label(add, text="Name", width=12,height=2,font=16)
        lblName.grid(row=1, column=0, columnspan=2)

        lblAge = tkinter.Label(add, text="Age", width=12,height=2,font=16)
        lblAge.grid(row=2, column=0, columnspan=2)

        lblMob = tkinter.Label(add, text="Mobile No", width=12,height=2,font=16)
        lblMob.grid(row=3, column=0, columnspan=2)

        varID = tkinter.IntVar()
        txtId = tkinter.Entry(add, text="ID", width=12, textvariable=varID,font=16)
        txtId.grid(row=0, column=2, columnspan=2)

        varName = tkinter.StringVar()
        txtName = tkinter.Entry(add, text="Name", width=12, textvariable=varName,font=16)
        txtName.grid(row=1, column=2, columnspan=2)

        varAge = tkinter.IntVar()
        txtAge = tkinter.Entry(add, text="Age", width=12, textvariable=varAge,font=16)
        txtAge.grid(row=2, column=2, columnspan=2)

        varMob = tkinter.StringVar()
        txtMob = tkinter.Entry(add, text="Mobile No", width=12, textvariable=varMob,font=16)
        txtMob.grid(row=3, column=2, columnspan=2)
        
        btnAdd = tkinter.Button(add, text="Add", width=10, command=btnAdd_Click,height=2,font=16)
        btnAdd.grid(row=4, column=0,columnspan=4)

        

        add.mainloop()

def btnsearch_click():
    
        
        def btnSearch_Click():
            
            id = txtId.get()
            cus = Customer()
            flag=cus.searchCustomer(id)
            
            if (flag == 1):
                varName1=cus.name
                varAge1=cus.age
                varMob1=cus.mob
                
                details = tkinter.Tk()
                details.title("customer details")
                details.minsize(250,250)
                
                
                lblName = tkinter.Label(details, text="Name :", width=12,height=2,font=16)
                lblName.grid(row=1, column=0, columnspan=2)

                lblAge = tkinter.Label(details, text="Age :", width=12,height=2,font=16)
                lblAge.grid(row=2, column=0, columnspan=2)
                
                lblMob = tkinter.Label(details, text="Mobile No :", width=12,height=2,font=16)
                lblMob.grid(row=3, column=0, columnspan=2)
                
                lblName1 = tkinter.Label(details, text=varName1, width=12,height=2,font=16)
                lblName1.grid(row=1, column=2, columnspan=2)

                lblAge1 = tkinter.Label(details, text=varAge1, width=12,height=2,font=16)
                lblAge1.grid(row=2, column=2, columnspan=2)
                
                lblMob1 = tkinter.Label(details, text=varMob1, width=12,height=2,font=16)
                lblMob1.grid(row=3, column=2, columnspan=2)
               
                details.mainloop()
                
                
            else:
                tkinter.messagebox.showinfo("Failed", "Customer with given ID Not Found")
    
        search = tkinter.Tk()
        search.title("SEARCH CUSTOMER")
        search.minsize(250, 250)
        
        
        lblId = tkinter.Label(search, text="ID", width=12,height=2,font=16)
        lblId.grid(row=0, column=0, columnspan=2)

        varID = tkinter.IntVar()
        txtId = tkinter.Entry(search, text="ID", width=12, textvariable=varID,font=16)
        txtId.grid(row=0, column=2, columnspan=2)

        btnSearch = tkinter.Button(search, text="Search", width=10, command=btnSearch_Click,height=2,font=16)
        btnSearch.grid(row=2, column=0,columnspan=4)

        search.mainloop()

def btndelete_click():
    
        def btnDelete_Click():
            id = txtId.get()
            cus = Customer()
            flag=cus.deleteCustomer(id)
            if(flag==1):
                tkinter.messagebox.showinfo("Sucess", "Customer Deleted Sucessfully")
            else:
                tkinter.messagebox.showinfo("Failed", "Customer with given ID Not Found")
    
    
        delete = tkinter.Tk()
        delete.title("DELETE CUSTOMER")
        delete.minsize(250, 250)
        
        
        lblId = tkinter.Label(delete, text="ID", width=12,height=2,font=16)
        lblId.grid(row=0, column=0, columnspan=2)

        varID = tkinter.IntVar()
        txtId = tkinter.Entry(delete, text="ID", width=12, textvariable=varID,font=16)
        txtId.grid(row=0, column=2, columnspan=2)

        btnDelete = tkinter.Button(delete, text="Delete", width=10, command=btnDelete_Click,height=2,font=16)
        btnDelete.grid(row=2, column=0,columnspan=4)

        delete.mainloop()
        
def btnmodify_click():
    
        def btnModify_Click():
            regex = re.compile(r'\d{10}')
            mob = regex.search(txtMob.get())==None
            
            regex2 = re.compile(r'\d{11,}')
            mob2 = regex2.search(txtMob.get())==None
            
            if(mob2==False):
                mesg = "mobile number must be of 10 digits \nenter the details again\nwith correct mobile number"
                tkinter.messagebox.showinfo("try again",mesg)
            elif(mob==False):
               cus = Customer()
               cus.id = txtId.get()
               cus.name = txtName.get()
               cus.age = txtAge.get()
               cus.mob = txtMob.get()
               flag=cus.modifyCustomer()
               if(flag==1):
                  tkinter.messagebox.showinfo("Success", "Customer Modified Successfully")
               else:
                  tkinter.messagebox.showinfo("Failed", "Customer with given ID Not Found")
            else:
                mesg = "mobile number must be of 10 digits \nenter the details again\nwith correct mobile number"
                tkinter.messagebox.showinfo("try again",mesg)
            
    
    
        modify = tkinter.Tk()
        modify.title("MODIFY CUSTOMER")
        modify.minsize(250, 250)
        
        
        lblId = tkinter.Label(modify, text="ID", width=12,height=2,font=16)
        lblId.grid(row=0, column=0, columnspan=2)

        lblName = tkinter.Label(modify, text="Name", width=12,height=2,font=16)
        lblName.grid(row=1, column=0, columnspan=2)

        lblAge = tkinter.Label(modify, text="Age", width=12,height=2,font=16)
        lblAge.grid(row=2, column=0, columnspan=2)

        lblMob = tkinter.Label(modify, text="Mobile No", width=12,height=2,font=16)
        lblMob.grid(row=3, column=0, columnspan=2)

        varID = tkinter.IntVar()
        txtId = tkinter.Entry(modify, text="ID", width=12, textvariable=varID,font=16)
        txtId.grid(row=0, column=2, columnspan=2)

        varName = tkinter.StringVar()
        txtName = tkinter.Entry(modify, text="Name", width=12, textvariable=varName,font=16)
        txtName.grid(row=1, column=2, columnspan=2)

        varAge = tkinter.IntVar()
        txtAge = tkinter.Entry(modify, text="Age", width=12, textvariable=varAge,font=16)
        txtAge.grid(row=2, column=2, columnspan=2)

        varMob = tkinter.StringVar()
        txtMob = tkinter.Entry(modify, text="Mobile No", width=12, textvariable=varMob,font=16)
        txtMob.grid(row=3, column=2, columnspan=2)
        
        btnModify = tkinter.Button(modify, text="Modify", width=10, command=btnModify_Click,height=2,font=16)
        btnModify.grid(row=4, column=0,columnspan=4)

        

        modify.mainloop()

def btnLoad_Click():
    Customer.loadCustomerfromFile()
    tkinter.messagebox.showinfo("Successes", "Customer Loaded Successfully")


def btnSave_Click():
    Customer.saveCustomerinFile()
    tkinter.messagebox.showinfo("Successes", "Customer Saved Successfully")

def btnShowall_click():
    Customer.showAllCustomer()

root = tkinter.Tk()
root.geometry("475x550+100+100")
root.title("CMS by ankurpal")
root.configure(background='black')

photo1 = tkinter.PhotoImage(file = r"Untitled-1.png")
lblcms = tkinter.Label(root,image=photo1)
lblcms.grid(row=0, column=0, columnspan=10)

photo2 = tkinter.PhotoImage(file = r"add-new-user.png")
btnadd = tkinter.Button(master=root, text="Add New Customer",command=btnadd_click,font=16,bg="skyblue",image=photo2)
btnadd.grid(row=3,column=0,columnspan=2)

photo3 = tkinter.PhotoImage(file = r"search.png")
btnsearch = tkinter.Button(master=root, text="search Customer",command=btnsearch_click,font=16,bg="skyblue",image=photo3)
btnsearch.grid(row=5,column=1,columnspan=2)

photo4 = tkinter.PhotoImage(file = r"user_delete.png")
btndelete = tkinter.Button(master=root, text="Delete Customer",command=btndelete_click,font=16,bg="skyblue",image=photo4)
btndelete.grid(row=3,column=4,columnspan=2)

photo5 = tkinter.PhotoImage(file = r"edit.png")
btnmodify = tkinter.Button(master=root, text="Modify Customer",command=btnmodify_click,font=16,bg="skyblue",image=photo5)
btnmodify.grid(row=3,column=2,columnspan=2)

photo6 = tkinter.PhotoImage(file = r"showusers.png")
btnShowall = tkinter.Button(master=root, text="Show All", command=btnShowall_click,font=16,bg="skyblue",image=photo6)
btnShowall.grid(row=5, column=3, columnspan=2)

btnLoad = tkinter.Button(root, text="Load Customers", width=18, command=btnLoad_Click,height=2,font=16)
btnLoad.grid(row=8, column=0, columnspan=4)

btnSave = tkinter.Button(root, text="Save Customers ", width=18, command=btnSave_Click,height=2,font=16)
btnSave.grid(row=8, column=2, columnspan=4)

root.mainloop()

