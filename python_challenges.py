import sqlite3



def create_db():
    conn=sqlite3.connect('python_chall.db')
    with conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS roster(\
                    Name TEXT, Species TEXT, IQ INT);")
        conn.commit()
    conn.close()

def add_items():
    conn=sqlite3.connect('python_chall.db')
    with conn:
        c=conn.cursor()
        c.execute("INSERT INTO roster(Name, Species, IQ) VALUES (?, ?, ?)", \
                  ('Jean-Baptiste Zorg', 'Human', 122))
        c.execute("INSERT INTO roster(Name, Species, IQ) VALUES (?, ?, ?)", \
                  ('Korben Dallas', 'Meat Popsicle', 100))
        c.execute("INSERT INTO roster(Name, Species, IQ) VALUES (?, ?, ?)", \
                  ('Ak\'not', 'Mangalore', -5))
        conn.commit()
    conn.close()

def update():
    conn=sqlite3.connect('python_chall.db')
    with conn:
        c=conn.cursor()
        c.execute("UPDATE roster SET Species= 'Human' WHERE Name='Korben Dallas'")
        conn.commit()
    conn.close()

def get_humans():
    conn=sqlite3.connect('python_chall.db')
    with conn:
        c=conn.cursor()
        c.execute("SELECT * FROM roster WHERE Species='Human'")
        myresult=c.fetchall()
        for x in myresult:
            print(x)
        conn.commit()
    conn.close()

        
if __name__=="__main__":
    get_humans()
