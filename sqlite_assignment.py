import sqlite3
 #get personal data and insert into a tuple
firstName= input("Enter your first name: ")
lastName= input("Enter your last name: ")
age= int(input("Enter your age: "))
personData=(firstName, lastName, age)

#execute insert statement for supplied person data
with sqlite3.connect("test_database.db") as connection:
    c=connection.cursor()
    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)

#select all first and last name form people over age of 25
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 25")
    while True: 
        row=c.fetchone()
        if row is None:
            break
        print(row)
