class public():
  def __init__(self):
    self.datopersona={
    "nombre":None,
    "apellido":None,
    "edad":None,
    "sexo":None
    }
    
  def almacenar_datos():
    private.almacenar(public.datopersona)
    
  def recibir_dato(lista):
    return private.devolver_dato_get(lista)

class private():
  def __init__(self):
    self.almacenador = []
    
  def almacenar(self,dato):
    b=0
    contador = self.almacenador
    for a in contador:
      b+=1
    private.almacenador[b]= dato
    
  def devolver_dato_get(lista):
    return private.almacenador[lista]
