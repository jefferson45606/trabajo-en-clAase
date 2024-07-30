#vista
import tkinter as tk
from tkinter import messagebox
import json

class Public:
    def __init__(self):
        self.datopersona = {
            "nombre": None,
            "apellido": None,
            "edad": None,
            "sexo": None
        }

    def almacenar_datos(self):
        Private().almacenar(self.datopersona)

    def recibir_dato(self, index):
        return Private().devolver_dato_get(index)


class Private:
    def __init__(self):
        self.almacenador = []

    def almacenar(self, dato):
        self.almacenador.append(dato)

    def devolver_dato_get(self, index):
        if index < len(self.almacenador):
            return self.almacenador[index]
        else:
            return None


class App:
    def __init__(self, root):
        self.public = Public()

        self.root = root
        self.root.title("Gestión de Datos Personales")

        self.frame = tk.Frame(root, padx=10, pady=10)
        self.frame.pack()

        self.nombre_label = tk.Label(self.frame, text="Nombre:")
        self.nombre_label.grid(row=0, column=0, sticky="e")
        self.nombre_entry = tk.Entry(self.frame)
        self.nombre_entry.grid(row=0, column=1)

        self.apellido_label = tk.Label(self.frame, text="Apellido:")
        self.apellido_label.grid(row=1, column=0, sticky="e")
        self.apellido_entry = tk.Entry(self.frame)
        self.apellido_entry.grid(row=1, column=1)

        self.edad_label = tk.Label(self.frame, text="Edad:")
        self.edad_label.grid(row=2, column=0, sticky="e")
        self.edad_entry = tk.Entry(self.frame)
        self.edad_entry.grid(row=2, column=1)

        self.sexo_label = tk.Label(self.frame, text="Sexo:")
        self.sexo_label.grid(row=3, column=0, sticky="e")
        self.sexo_entry = tk.Entry(self.frame)
        self.sexo_entry.grid(row=3, column=1)

        self.save_button = tk.Button(self.frame, text="Guardar", command=self.save_data)
        self.save_button.grid(row=4, column=0, columnspan=2)

        self.display_button = tk.Button(self.frame, text="Mostrar Datos", command=self.display_data)
        self.display_button.grid(row=5, column=0, columnspan=2)

    def save_data(self):
        self.public.datopersona["nombre"] = self.nombre_entry.get()
        self.public.datopersona["apellido"] = self.apellido_entry.get()
        self.public.datopersona["edad"] = self.edad_entry.get()
        self.public.datopersona["sexo"] = self.sexo_entry.get()

        self.public.almacenar_datos()
        messagebox.showinfo("Información", "Datos guardados correctamente")

    def display_data(self):
        datos = []
        for i in range(len(Private().almacenador)):
            datos.append(Private().devolver_dato_get(i))
        messagebox.showinfo("Datos Almacenados", json.dumps(datos, indent=4))


root = tk.Tk()
app = App(root)
root.mainloop()


   
