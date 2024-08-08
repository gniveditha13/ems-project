#how to import your package 

import mysql.connector

#how to connect your mysql connector

mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="ems")
print(mydb)

#how to run different sql commads:
#cursor():it is used to run different sql commands in python.

c=mydb.cursor()

#retrieve data from mysql server in python program.
c.execute("select * from emp_details")

#to see column names
print(c.column_names)

#to see all data in your table
print(c.fetchall())

#--------------------------------------------------------------------------

#how to build a login form with the help of id and password:

#c.execute("select * from emp_details")
#empid=input("Enter employee id: ")
#pwd=input("Enter employee password: ")
#islogin=False
#mycolumn=c.column_names
#mydata=c.fetchall()
#for k in mydata:
#    if(k[0]==empid and k[1]==pwd):
#        islogin=True
#        break
#if(not islogin):
#    print("Incorrect ID or Password.")
#if(islogin):
#    print("Login successful.")


#--------------------------------------------------------------------------

#Insertion of data
#import datetime
#empid=input("Enter employee id: ")
#dt=str(datetime.datetime.now())
#status=input("Enter status present/absent: ")

#c.execute("insert into emp_attendance values(%s,%s,%s)",(empid,dt,status))
#whenever you are inserting some data into the database then you need to commit it which
#means you are saving the data and is it compulsory.
#mydb.commit()
#print("Attendance recorded successfully.")


#--------------------------------------------------------------------------

#Update the salary:
#empid=input("Enter employee id: ")
#salary=input("Enter updated salary: ")
#c.execute("update emp_details set emp_salary=%s where emp_id=%s",(salary,empid))
#mydb.commit()
#print("Salary updated successfully.")

#--------------------------------------------------------------------------

#View profile:

empid=input("Enter employee id: ")
c.execute("select * from emp_details where emp_id=%s",(empid,))
#res=c.fetchall()
#print(res)

#or

res=c.fetchall()[0]
print("Employee Id: ",res[0])
print("Employee Password: ",res[1])
print("Employee Name: ",res[2])
print("Employee Salary: ",res[3])













