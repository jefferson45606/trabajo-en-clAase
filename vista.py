#vista
import tkinter as tk

class Vista(tk.Tk):
    def __init__(self,controlador):
        super().__init__()
        self.controlador = controlador
        self.title("principal")
        
        self 
