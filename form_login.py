import tkinter as tk
import base_de_datos
from tkinter import messagebox
import base64

#Creación de la ventana principal
window = tk.Tk()
window.title("Inicio de sesión")
window.geometry("400x200")
window.config(bg="gray95")
window.resizable(0, 0)
window.iconbitmap("./imagenes/favicon.ico")

#Creacion de etiquetas y entradas de datos
label_user = tk.Label(text = "Nombre de usuario:",
                    font=("Rockwell", 12),
                    fg = "gray16")
label_user.place(x = 10, y = 20)
entry_user = tk.Entry(background = "gray99", 
                    border = 3,
                    foreground="gray16", 
                    width = 30,
                    )
entry_user.place(x = 200, y = 20)

label_password = tk.Label(text = "Contraseña:",
                        font=("Rockwell", 12),
                        fg = "gray16")
label_password.place(x = 10, y = 70)
entry_password = tk.Entry(show = "*",
                    background = "gray99", 
                    border = 3, 
                    foreground="gray16", 
                    width = 30,
                    )
entry_password.place(x = 200, y = 70)

#funcion para comprobar la contraseña
def check_password():
  password = entry_password.get()
  password = password.encode('ascii')
  password = base64.b64encode(password)
  if len(password)<8:
        messagebox.showinfo("Mensaje", "La contraseña debe tener al menos 8 caracteres")
        clean()


#funcion para la entrada de datos
def login():
    username = entry_user.get()
    password = entry_password.get()
    if base_de_datos.login_data(username,password):
        messagebox.showinfo("Mensaje","Bienvenido a la aplicación")
    else:
        messagebox.showinfo("Mensaje","Usuario o contraseña incorrectos")
    clean()

#función para limpiar las entradas
def clean():
    entry_user.delete(0, tk.END)
    entry_password.delete(0, tk.END)

#Botón para ingresar datos
button_login = tk.Button(text = "Entrar", 
                                bg = "deepskyblue2", 
                                fg = "gray16",
                                font=("Rockwell", 14),
                                border = 3,
                                padx = 30, 
                                pady = 10,
                                cursor = "hand2",
                                command = login)
button_login.place(x = 120, y = 130)

#Bucle de ejecución
tk.mainloop()