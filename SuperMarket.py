import sqlite3
import time


class Product():
    def __init__(self, Name, Price, Amount):
        self.Name = Name
        self.Price = Price
        self.Amount = Amount

    def __str__(self):
        return "Name--> {}\nPrice--> {}\nAmount--> {}".format(self.Name, self.Price, self.Amount)


class Database:
    def __init__(self):
        self.createconnection()

    def createconnection(self):
        self.connection = sqlite3.connect("basem.db")
        self.cursor = self.connection.cursor()
        command = "Create Table if not exists SuperMarket(Name Text,Price INT,Amount INT)"
        self.cursor.execute(command)
        self.connection.commit()

    def dropconnection(self):
        self.connection.close()

    def showproducts(self):
        command = "SELECT * FROM SuperMarket"
        self.cursor.execute(command, )
        data = self.cursor.fetchall()
        if len(data) == 0:
            print("Error")
        else:
            for row in data:
                data = Product(row[0], row[1], row[2])
                print(data)

    def addproduct(self, Product):
        command = "INSERT INTO Supermarket Values(?,?,?)"
        self.cursor.execute(command, (Product.Name, Product.Price, Product.Amount))
        self.connection.commit()

    def deleteproduct(self, Name):
        command = "Delete From SuperMarket Where Name = ?"
        self.cursor.execute(command, (Name,))
        print("Deleted")

    def findproduct(self, Name):
        command = "Select * From Supermarket Where Name = ?"
        self.cursor.execute(command, (Name,))
        Data = self.cursor.fetchall()
        if len(Data) == 0:
            print("Failed")
        else:
            for i in Data:
                Data = Product(i[0], i[1], i[2])
                print(Data)

    def totalproductvalue(self):
        command = "Select SUM(Price) From SuperMarket"
        self.cursor.execute(command)
        data = self.cursor.fetchone()
        self.cursor.execute("SELECT SUM(AMOUNT) FROM SuperMarket")
        data2 = self.cursor.fetchone()
        print("Price {}\nAmount {}".format(data,data2))


d = Database()
while True:
    i = input("Please Select Your Operation;")
    if i == "q":
        d.dropconnection()
        break
    elif i == "1":
        d.showproducts()

    elif i == "2":
        Name = input("Name; ")
        Price = int(input("Price; "))
        Amount = int(input("Amount; "))
        Take = Product(Name, Price, Amount)
        d.addproduct(Take)
    elif i == "3":
        Name = input("Product Name; ")
        d.findproduct(Name)
    elif i == "4":
        Name = input("Product Name")
        d.deleteproduct(Name)
    elif i == "5":
        d.totalproductvalue()














