#vista
import tkinter as tk
from tkinter import messagebox
import json

class Vista:
    def __init__(self, root):
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

        self.save_button = tk.Button(self.frame, text="Guardar", command=self.guardarDatos)
        self.save_button.grid(row=4, column=0, columnspan=2)

        self.display_button = tk.Button(self.frame, text="Mostrar Datos", command=self.mostrarDatos)
        self.display_button.grid(row=5, column=0, columnspan=2)

        self.datos_almacenados = []

    def guardarDatos(self):
        datos_persona = {
            "nombre": self.nombre_entry.get(),
            "apellido": self.apellido_entry.get(),
            "edad": self.edad_entry.get(),
            "sexo": self.sexo_entry.get()
        }
        return datos_persona
        
        self.datos_almacenados.append(datos_persona)
        messagebox.showinfo("Información", "Datos guardados correctamente")

    def mostrarDatos(self):
        datos_json = json.dumps(self.datos_almacenados, indent=4)
        messagebox.showinfo("Datos Almacenados", datos_json)
        

root = tk.Tk()
app = Vista(root)
root.mainloop()
