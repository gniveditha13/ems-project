#import streamlit as st
#st.title("EMPLOYEE MANAGEMENT SYSTEM")

#st.image("https://img.freepik.com/premium-vector/recruitment-concept-idea-employment-human_277904-2607.jpg")
#st.video("https://www.youtube.com/watch?v=laYOmEgZojw")

#how to build a menu , this means that dividing your entire application into smaller smaller sections
#like home,download page ,emp page section, adimin page section etc..
#selectbox(): is used for creating a dropdown menu
#navbar=st.selectbox("Menu",("Home","Employee","Admin"))
#st.write(navbar) #this wrte is not mandatory here jzt to show wht user has clicked it has been specified.

#Ex:
#navbar=st.selectbox("Menu",("Home","Employee","Admin"))
#if(navbar=="Home"):
#    st.image("https://img.freepik.com/premium-vector/recruitment-concept-idea-employment-human_277904-2607.jpg")
#elif(navbar=="Employee"):
#    st.video("https://www.youtube.com/watch?v=laYOmEgZojw")
#elif(navbar=="Admin"):
#    st.markdown("# welcome to admin page!")
    

#how to build side menu:
#navbar=st.sidebar.selectbox("Menu",("Home","Employee","Admin"))
#if(navbar=="Home"):
#    st.image("https://img.freepik.com/premium-vector/recruitment-concept-idea-employment-human_277904-2607.jpg")
#elif(navbar=="Employee"):
#    st.video("https://www.youtube.com/watch?v=laYOmEgZojw")
#elif(navbar=="Admin"):
#    st.markdown("# welcome to admin page!")  


#how to take the input from the user:
#st.text_input("Enter name: ")

#-----------------------------------------------------------------------------------------------------------------------------------------------

#ems project:

import streamlit as st
#to connect mysql
import mysql.connector
#to give present date and time
import datetime

st.title("EMPLOYEE MANAGEMENT SYSTEM")

#how to build login form:

navbar=st.selectbox("Menu",("Home","Employee","Admin"))
if(navbar=="Home"):
    st.image("https://img.freepik.com/premium-vector/recruitment-concept-idea-employment-human_277904-2607.jpg")

elif(navbar=="Employee"):
    if "islogin" not in st.session_state:
        st.session_state["islogin"]=False
    empid=st.text_input("Enter employee id: ")
    pwd=st.text_input("Enter password: ")
    btn=st.button("Login")

    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="ems")
        c=mydb.cursor()
        c.execute("select * from emp_details")
        mydata=c.fetchall()
        for k in mydata:
            if(k[0]==empid and k[1]==pwd):
                st.session_state["islogin"]=True
                break
        if(not st.session_state["islogin"]):
                st.write("Incorrect ID or Password.")
    if(st.session_state["islogin"]):
            st.write("Login successful.")
            navbar2=st.selectbox("Features",("None","View Profile","Leave Application"))
#view profile:
            if(navbar2=="View Profile"):
                mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="ems")
                c=mydb.cursor()
                c.execute("select * from emp_details where emp_id=%s",(empid,))
                res=c.fetchall()[0]
                st.write("Employee Id: ",res[0])
                st.write("Employee Password: ",res[1])
                st.write("Employee Name: ",res[2])
                st.write("Employee Salary: ",res[3])
#leave application:
            elif(navbar2=="Leave Application"):
                    leave_appl_details=st.text_input("Enter leave application details: ")
                    btn2=st.button("Apply for leave.")
                    if btn2:
                        appl_id=str(datetime.datetime.now())
                        mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="ems")
                        c=mydb.cursor()
                        c.execute("insert into emp_leave values(%s,%s,%s)",(appl_id,empid,leave_appl_details))
                        mydb.commit()
                        st.write("Leave applied successfully.")
elif(navbar=="Admin"):
    st.markdown("# welcome to admin page!")




































