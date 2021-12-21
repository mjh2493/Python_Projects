import sqlite3

conn= sqlite3.connect('db_assignment.db')

#creates table
with conn:
    cur= conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    conn.commit()
conn.close()

#reconnects to database
conn= sqlite3.connect('db_assignment.db')


#creates my tuple with files
files_tuple=('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.png', 'World.txt', 'data.pdf', 'myPhoto.jpg')


#loop that looks for files that end in txt to add to table
for x in files_tuple:
    if x.endswith('.txt'):
        with conn:
            cur=conn.cursor()
            cur.execute("INSERT INTO tbl_files (file_name) VALUES (?)", (x,))
            print(x)
conn.close()
