import mysql.connector
import datetime
from tabulate import tabulate
db=input("Enter name of your database:")
mydb=mysql.connector.connect(host='localhost',user='root',password='root',auth_plugin='mysql_native_password')
mycursor=mydb.cursor()
sql="Create database if not exists %s"%(db)
mycursor.execute(sql)
print("Database created Successfully..")
mycursor=mydb.cursor()
mycursor.execute("Use "+db)
TableName=input("Name of table to be created:")
query="Create table if not exists "+TableName+"\
(empno int primary key,\
name varchar(15) not null,\
job varchar(15),\
BasicSalary int,\
DA float,\
HRA float,\
GrossSalary float,\
Tax float,\
NetSalary float)"
print("Table "+TableName+" created successfully....")
mycursor.execute(query)
def insertion():
    try:
            print("Enter employee information....")
            mempno=int(input("Enter employee no:"))
            mname=input("Enter employee name:")
            mjob=input("Enter employee job:")
            mbasic=float(input("Enter basic salary:"))
            if mjob.upper()=='OFFICER':
              mda=mbasic*0.5
              mhra=mbasic*0.35
              mtax=mbasic*0.2
            elif mjob.upper()=='MANAGER':
                mda=mbasic*0.45
                mhra=mbasic*0.38
                mtax=mbasic*0.15
            else:
                mda=mbasic*0.40
                mhra=mbasic*0.25
                mtax=mbasic*0.1
            mgross=mbasic+mda+mhra
            mnet=mgross-mtax
            rec=(mempno,mname,mjob,mbasic,mda,mhra,mgross,mtax,mnet)
            query="insert into "+TableName+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,rec)
            mydb.commit()
            print('Record added successfuly....')
    except Exception as e:
            print('Something went wrong',e)
def display():
    try:
            query='select * from '+TableName
            mycursor.execute(query)
            print(tabulate(mycursor,headers=['EmpNo','Name','Job','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary']))
            '''myrecords=mycursor.fetchall()
            for rec in myrecords:
               print(rec)'''
    except Exception as e:
        print('Something went wrong',e)
def particular():
    try:
            en=input('Enter emplyee no. of the record to be displayed...')
            query="select*from "+TableName+" where empno="+en
            print(query)
            mycursor.execute(query)
            myrecord=mycursor.fetchone()
            print("\n\nRecord of Employee No.:"+en)
            print(myrecord)
            c=mycursor.rowcount
            if c==1:
                print('Nothing to display')
    except Exception as e:
        print("Something went wrong",e)
def delete():
    try:
            ch=input('Do you want to delete all the records(y/n)')
            if ch.upper()=='Y':
                mycursor.execute('delete from '+TableName)
                mydb.commit()
                print('All the records are deleted')
    except Exception as e:
        print('Something went wrong',e)
def par_del():
    try:
            en=input('Enter employee no. of the record to be deleted...')
            query='delete from '+TableName+' where empno='+en
            mycursor.execute(query)
            mydb.commit()
            c=mycursor.rowcount
            if c>0:
                print("Deletion done")
            else:
                print('Employee no',en,'not found')
    except:
            print('Something went wrong')
def modify():
    try:
        mempno=int(input("Enter employee no. to be changed:"))
        mempno1=int(input("Enter new employee no.:"))
        mname=input("Enter employee name:")
        mjob=input("Enter employee job:")
        mbasic=float(input("Enter basic salary:"))
        if mjob.upper()=='OFFICER':
              mda=mbasic*0.5
              mhra=mbasic*0.35
              mtax=mbasic*0.2
        elif mjob.upper()=='MANAGER':
                mda=mbasic*0.45
                mhra=mbasic*0.38
                mtax=mbasic*0.15
        else:
                mda=mbasic*0.40
                mhra=mbasic*0.25
                mtax=mbasic*0.1
        mgross=mbasic+mda+mhra
        mnet=mgross-mtax
        mycursor.execute("update "+TableName+" set empno=%d,Name='%s',job='%s',BasicSalary=%d,DA=%d,HRA=%d,GrossSalary=%d,tax=%d,netsalary=%d where EmpNo=%d"%(mempno1,mname,mjob,mbasic,mda,mhra,mgross,mtax,mnet,mempno))
        print()
        mydb.commit()
        mycursor.execute("select * from %s;"%(TableName))
        for i in mycursor.fetchall():
            print(i)  
    except Exception as e:
                print('Something went wrong',e)
def disp_payroll():
    try:
                query='select * from '+TableName
                mycursor.execute(query)
                myrecords=mycursor.fetchall()
                print('\n\n\n')
                print(95*'*')
                print('Employee Payroll'.center(90))
                print(95*'*')
                now=datetime.datetime.now()
                print("Current Date and Time:",end=' ')
                print(now.strftime("%Y-%m-%d %H:%M:%S"))
                print()
                print(95*'-')
                print('%-5s %15s %-10s %-8s %-8s %-8s %-9s %-8s %-9s'\
                      %('Empno','Name','Job','Basic','DA','HRA','Gross','Tax','Net'))
                print(95*'-')
                for rec in myrecords:
                    print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
                print(95*'-')
    except Exception as e:
                print('Something went wrong',e)
def disp_salaryslip():
    try:
                query='select * from '+TableName
                mycursor.execute(query)
                now=datetime.datetime.now()
                print('\n\n\n')
                print(95*'-')
                print("\t\t\t\tSalary Slip")
                print(95*'-')
                print("Current Date and Time:",end=' ')
                print(now.strftime("%Y-%m-%d %H:%M:%S"))
                myrecords=mycursor.fetchall()
                for rec in myrecords:
                    print('%4d %-15s %-10s %8.2f %8.2f %8.2f %9.2f %8.2f %9.2f'%rec)
    except Exception as e:
                print('Something went wrong',e)
def par_disp_salaryslip():
    try:
                en=input("Enter employee number whose pay slip you want to retrieve:")
                query='select * from '+TableName+' where empno='+en
                mycursor.execute(query)
                now=datetime.datetime.now()
                print("\n\n\n\t\t\t\tSALARY SLIP")
                print("Current Date and Time:",end=' ')
                print(now.strftime("%Y-%m-%d %H:%M:%S"))
                print(tabulate(mycursor,headers=['Empno','Name','Job','Basic Salary','DA','HRA','Gross Salary','Tax','Net Salary']))
    except Exception as e:
                print('Something went wrong',e)
def menu():
  while True:
    print('\n\n\n')
    print("*"*95)
    print('\t\t\t\t\tMAIN MENU')
    print("*"*95)
    print('\t\t\t\t\t1. Adding Employee records')
    print('\t\t\t\t\t2. For Displaying Record of all the employees')
    print('\t\t\t\t\t3. For Displaying Record of particular employees')
    print('\t\t\t\t\t4. For Deleting Record of all the employees')
    print('\t\t\t\t\t5. For Deleting Record of a particular employee')
    print('\t\t\t\t\t6. For modification in a record')
    print('\t\t\t\t\t7. For Displaying payroll')
    print('\t\t\t\t\t8. For Displaying Salary slip of all the employees')
    print('\t\t\t\t\t9. For Displaying salary slip of particular employee')
    print('\t\t\t\t\t10.For Exit')
    print("Enter choice...",end='')
    choice=int(input())
    if choice==1:
        insertion()
        display()
    elif choice==2:
        display()
    elif choice==3:
        particular()
    elif choice==4:
        display()
        delete()
    elif choice==5:
        display()
        print()
        par_del()
        print()
        print("Do You Want To Delete More Records")
        c=input("Enter Your Choice")
        if c=='Yes':
            par_del()
        else:
            print("okay")
        display()
    elif choice==6:
        display()
        modify()
        print()
        print("Do You Want To Update more records")
        c=input("Enter Your Choice")
        if c=='Yes':
            modify()
        else:
            print("okay")
    elif choice==7:
        disp_payroll()
    elif choice==8:
        disp_salaryslip()
    elif choice==9:
        par_disp_salaryslip()
    elif choice==10:
        break
    else:
        print("Wrong choice...")
menu()
