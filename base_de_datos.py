import sqlite3

conn=sqlite3.connect("base_de_datos.db")
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(50) UNIQUE, birthDay VARCHAR(10), email VARCHAR(50) UNIQUE, password VARCHAR(50))")

def save_data(username,birthday,email,password):
  cursor.execute("INSERT INTO usuarios VALUES(NULL,?,?,?,?)",(username,birthday,email,password))
  conn.commit()


def login_data(username,password):
  cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?",(username,password))
  if cursor.fetchone() is not None:
    return True
  else:
    return False