import mysql
import mysql.connector
from prettytable import PrettyTable
import random
from mysql.connector import Error


class library:
    def add():
        try:
            x = PrettyTable()
            x.field_names = ['bookid','title','author','status']

            bookid = input("Enter the book ID: ")
            title = input("Enter the title: ")
            author = input("Enter the author name:")
            status = input("Enter the status (Available/Not):")
            mydb = mysql.connector.connect(host = "localhost", user = "root",password = "1133",database = "library")
            mycursor  = mydb.cursor()
            sql = "insert into books values(%s,%s,%s,%s)"
            d = (bookid,title,author,status)
            mycursor.execute(sql,d)
            mycursor.execute("select * from books;")
            myresult = mycursor.fetchall()
            mydb.commit()
            for row in myresult:
                x.add_row([row[0],row[1],row[2],row[3]])
            print(x)
            mydb.commit()
            mydb.close()
        except Error as e:
            print(e)
    def delete():
        try:
            x = PrettyTable()
            x.field_names = ['bookid','title','author','status']
            bookid = input("Enter the bookid:")
            mydb = mysql.connector.connect(host = "localhost", user = "root",password = "1133",database = "library")
            mycursor  = mydb.cursor()
            mycursor.execute("delete from books where bookid = %s"%(bookid))
            mydb.commit()
            print(bookid,"is deleted")
        except Error as e:
            print(e)
    def view():
        try:
            x = PrettyTable()
            x.field_names = ['bookid','title','author','status']
            bookid = input("Enter the bookid of the book you wanted:")
            mydb = mysql.connector.connect(host = "localhost", user = "root",password = "1133",database = "library")
            mycursor  = mydb.cursor()
            mycursor.execute("select * from books where bookid = %s"%bookid)
            myresult = mycursor.fetchall()
            mydb.commit()
            for row in myresult:
                x.add_row([row[0], row[1],row[2],row[3]])
            print(x)
        except Error as e:
            print(e)

    def issue():
        try:
            bookid = input("Enter the bookid:")
            name = input("Enter the name of student:")
            sid = input("Enter the student id:")
            bookname = input("Enter the bookname:")
            mydb = mysql.connector.connect(host = "localhost", user = "root",password = "1133",database = "library")
            mycursor  = mydb.cursor()
            mycursor.execute("insert into issued values(%s,%s,%s,%s)",(bookid,name,bookname,sid))
            mycursor.execute("insert into returnid values(%s,%s,%s,%s)",(bookid,name,sid,bookname))
            mydb.commit()
            mydb.close()
            
        except Error as e:
            print(e)
    def returnbook():
        try:
            x = PrettyTable()
            x.field_names = ['bookid','studentname','author','status']
            sid = input("Enter the student id:")
            mydb = mysql.connector.connect(host = "localhost", user = "root",password = "1133",database = "library")
            mycursor  = mydb.cursor()
            mycursor.execute("delete from issued where studentid = %s"%sid)
            mycursor.execute("delete from returnid where studentid = %s"%sid)
            mydb.commit()

        except Error as e:
            print(e)



#main
print("1.Add Book Details")
print("2.Delete Book")
print("3.View Book")
print("4.Issue book to students")
print("5.Return book")

n = int(input("Enter your choice: "))

if(n==1):
    library.add()
elif(n==2):
    library.delete()
elif(n==3):
    library.view()
elif(n==4):
    library.issue()
elif(n==5):
    library.returnbook()