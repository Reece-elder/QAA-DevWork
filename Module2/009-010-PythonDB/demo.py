# Install and set up Microsoft SQL Express (Free specialised version, grab the Express)
# https://www.microsoft.com/en-gb/sql-server/sql-server-downloads
# Download the installer and install MSQL, will go through how to install 
# Install Microsoft SQL Server Management Tool as well to connect to the Server
# If you are unable to install MSQL you can access it through the GoToMyPC link where it is already installed and setup  

# SQL Recap
# SHOW DATABASES;
# USE <DATABASE NAME>; 
# Select * from sys.databases
# DESCRIBE <table name>;
# SELECT * FROM <table name>
# INSERT INTO table_name (column1, column2, column3, ...)VALUES (value1, value2, value3, ...); 


# SQL Exercise answers
# 1 - SELECT * FROM job ORDER BY min_salary;
# 2 - SELECT * FROM job WHERE max_salary >= 30000 ORDER BY max_salary DESC;
# 3 - SELECT dept_no, last_name, annual_salary, hire_date FROM employee WHERE hire_date BETWEEN '1991-01-01' AND '1992-12-31' ORDER BY dept_no, last_name;
# 4 - SELECT last_name, monthly_salary = annual_salary / 12 FROM employee WHERE dept_no = 90;
# 5 - SELECT COUNT(*) as number_of_employees FROM employee;


# Basic pyodbc reading data from a database

# Install pyodbc to project with `pip install pyodbc` in terminal

# Must be at top of python file
import pyodbc

# use this to see the drivers on your system, select ODBC
# print(pyodbc.drivers())
# server = server_name when booting up Microsoft SQL
conx_string = "DRIVER={ODBC DRIVER 17 for SQL Server};SERVER=DESKTOP-SB94ROJ\SQLEXPRESS01;DATABASE=qastore; trusted_connection=YES"
# What we are wanting to pull from the database
query = "SELECT * FROM company"
# Connecting to our database and creating a connection object (which includes functions to interact)
conn = pyodbc.connect(conx_string)
# Creating a cursor object which is our locator or method of interacting with our data (like a real mouse cursor)
cursor = conn.cursor()
# Running our query with our cursor
cursor.execute(query)
# Fetching all of the data from our cursor query and assigning it to an object called data
data = cursor.fetchall()
# Printing our Data to the screen
print(data)


# Reading rows with a filter
query = "SELECT * FROM dept"

def queryDb(query):
    conn = pyodbc.connect(conx_string)
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

print(queryDb(query))
for row in queryDb(query):
    print(row)

# Exception Handling 
# When working with complex data it is important to handle exceptions properly, as all errors may not be apparent

def queryDbSimpleException(query):
    try:
        conn = pyodbc.connect(conx_string)
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except:
        return None

def queryDbBetterException(query):
    try:
        conn = pyodbc.connect(conx_string)
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as ex:
        print("Error: ", ex)
        return None

print(queryDbSimpleException(query))
for row in queryDbSimpleException(query):
    print(row)

for row in queryDbBetterException(query):
    print(row)

# Creating a table
def dataManipulationQuery(query):
    try:
        conn = pyodbc.connect(conx_string)
        cursor = conn.cursor()
        cursor.execute(query)
        print(query)
        conn.commit()
        return True
    except Exception as ex:
        print("Error: ", ex)
        return False

createTable = "CREATE TABLE students (student_id int IDENTITY(1,1) PRIMARY KEY, first_name VARCHAR(40) NOT NULL, last_name VARCHAR(30) NOT NULL, course VARCHAR(30), city VARCHAR(30));"

print(dataManipulationQuery(createTable))

# Inserting data
insertData = "INSERT INTO students(first_name, last_name, course, city) VALUES('Thomas', 'Anderson', 'Basic Programming', 'Zion')"
dataManipulationQuery(insertData)


