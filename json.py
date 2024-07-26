import json


datopersona1={
  "nombre":"NELSON",
  "apellido":"RINCON",
  "edad":37,
  "sexo":"MASCULINO"
}

datopersona = {
  "idCliente":["NELSON","RINCON",37,"MASCULINO"],
  "dato_trabajos":["direccion1","direccion2","direccion3"],
  "idFacturas":{
    "idFactura":"F001","Fecha":"20/05/2022","valor":"$100.000.000"
  }
}


personaDato_Json = json.dumps(datopersona)
print("Datos son: ",personaDato_Json)
print("longitud: ",len(personaDato_Json))
personaDato_Sin_Json = json.loads(personaDato_Json)
print("longitud: ",len(personaDato_Sin_Json))

def hacerDocumentoJson():
  datos= {"nombre":"Juan","edad":30}
  #serializar a json
  json_dato = json.dumps(datos)
  print(json_dato)
  #serializar y escribir en un archivo
  with open("datos.txt","w") as archivo:
    json.dump(datos,archivo)
    
hacerDocumentoJson()
