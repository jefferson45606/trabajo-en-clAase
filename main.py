from modelo import Modelo
from controlador import Controlador
from vista import Vista


modelo = Modelo()
controlador = Controlador(modelo)
vista = Vista(controlador)
vista.mainloop()
