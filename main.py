from io import open

texto="Vamos Vamos Penarol ,\n Hoy te vinimos a alentar,\n Para ser campeon , \n Hoy hay que ganar"


fichero=open("penarol.txt","w")
fichero.write(texto) 
fichero.close()
del(fichero)
del(texto)
fichero=open("penarol.txt","r")
#el metodo read() lee todas las lineas del fichero 
texto=fichero.read()
#Siempre hay que cerrar el fichero despues de haberlo utilizado
fichero.close()

print(texto)

del(fichero)
del(texto)
