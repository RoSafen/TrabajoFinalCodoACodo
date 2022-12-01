
import tkinter as tk

ventana = tk.Tk()
ventana.title("ABM Usuarios")
ventana.geometry("400x400")

etiqueta = tk.Label(text = "ABM de Usuarios")
etiqueta.place(x = 150, y = 20)

etiqueta1 = tk.Label(text = "Email:")
etiqueta1.place(x = 60, y = 60)

etiqueta2 = tk.Label(text = "Nombre:")
etiqueta2.place(x = 60, y = 90)

etiqueta3 = tk.Label(text = "Apellido:")
etiqueta3.place(x = 60, y = 120)

etiqueta4 = tk.Label(text = "Contraseña:")
etiqueta4.place(x = 60, y = 150)

etiqueta5 = tk.Label(text = "Fecha de nacimiento:")
etiqueta5.place(x = 60, y = 180)

etiqueta6 = tk.Label(text = "Dirección:")
etiqueta6.place(x = 60, y = 210)

cuadro1 = tk.Entry()
cuadro1.place(x = 230, y = 60)

cuadro2 = tk.Entry()
cuadro2.place(x = 230, y = 90)

cuadro3 = tk.Entry()
cuadro3.place(x = 230, y = 120)

cuadro4 = tk.Entry()
cuadro4.place(x = 230, y = 150)

cuadro5 = tk.Entry()
cuadro5.place(x = 230, y = 180)

cuadro6 = tk.Entry()
cuadro6.place(x = 230, y = 210)

boton = tk.Button(text = "Guardar")
boton.place(x = 120, y = 300)

boton = tk.Button(text = "Cancelar")
boton.place(x = 240, y = 300)

tk.mainloop()