import tkinter as tk
import base_de_datos
from tkinter import messagebox
import utils
import base64

window = tk.Tk()
window.title("Registro")
window.geometry("400x300")
window.config(bg="gray95")
window.resizable(0, 0)
window.iconbitmap("./imagenes/favicon.ico")

#ETIQUETAS
label_birth = tk.Label(text = "Fecha de nacimiento:", font="Rockwell 11")
label_birth.place(x = 20, y = 50)
entry_birth = tk.Entry(border = 3,
                    foreground="gray16", 
                    width = 25)
entry_birth.place(x = 220, y = 50)

label_mail = tk.Label(text = "Mail:", font="Rockwell 11")
label_mail.place(x = 20, y = 90)
entry_mail = tk.Entry(border = 3,
                    foreground="gray16", 
                    width = 25)
entry_mail.place(x = 220, y = 90)

user_label = tk.Label(text = "Nombre de usuario:", font="Rockwell 11")
user_label.place(x = 20, y = 130)
entry_user = tk.Entry(border = 3,
                    foreground="gray16", 
                    width = 25)
entry_user.place(x = 220, y = 130)

label_password = tk.Label(text = "Contraseña:", font="Rockwell 11")
label_password.place(x = 20, y = 170)
entry_password = tk.Entry(show = "*",
                    border = 3,
                    foreground="gray16", 
                    width = 25)
entry_password.place(x = 220, y = 170)


def check_password():
  password = entry_password.get()
  password = password.encode('ascii')
  password = base64.b64encode(password)
  if len(password)<8:
        messagebox.showinfo("Mensaje", "La contraseña debe tener al menos 8 caracteres")
        clean_form()

def save():
    username= entry_user.get()
    email = entry_mail.get()
    birth = entry_birth.get()
    password = entry_password.get()
    
    if utils.name_validator(username):
        if utils.date_validator(birth):
            if utils.email_validator(email):
                try:
                    base_de_datos.save_data(username,birth,email,password)
                    messagebox.showinfo("Mensaje", "Usuario registrado exitosamente")
                    clean_form()
                except:
                    messagebox.showinfo("Mensaje","El usuario no pudo ser registrado")
            else:
                messagebox.showinfo("Mensaje", "Correo electrónico con formato inválido")
        else:
            messagebox.showinfo("Mensaje", "Fecha con formato inválido")
    else:
        messagebox.showinfo("Mensaje","Nombre de usuario con formato inválido")
        clean_form()


def clean_form():
  entry_user.delete(0,tk.END)
  entry_birth.delete(0,tk.END)
  entry_mail.delete(0,tk.END)
  entry_password.delete(0,tk.END)


boton = tk.Button(text = "Registrar",
                 bg = "deepskyblue2", 
                fg = "gray16",
                font=("Rockwell", 14),
                border = 3,
                cursor = "hand2",
                width = 24,
                command = save)
boton.place(x = 65, y = 240)

tk.mainloop()