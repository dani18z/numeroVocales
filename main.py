from typing import Union

from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


#Devuelve el numero introducido, y la cadena introducida (literalmente, sin cambios)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


#Devuelve la palabra introducida, el numero de vocales que contiene y el numero de letras
@app.get("/contar_vocales/{cadena}")
def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra in "aeiou":
			contador += 1
	return {"Palabra": cadena,"Numero de vocales":contador, "Numero de letras": len(cadena)}



