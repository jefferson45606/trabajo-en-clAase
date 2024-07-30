class Controlador:
    def __init__(self):
        self.public = Public()
        self.private = Private()

    def almacenar_datos(self, nombre, apellido, edad, sexo):
        self.public.datopersona["nombre"] = nombre
        self.public.datopersona["apellido"] = apellido
        self.public.datopersona["edad"] = edad
        self.public.datopersona["sexo"] = sexo
        self.public.almacenar_datos()

    def obtener_datos(self):
        datos = []
        for i in range(len(self.private.almacenador)):
            datos.append(self.private.devolver_dato_get(i))
        return datos

