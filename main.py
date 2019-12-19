from io import open

texto="Vamos Vamos Penarol ,\n Hoy te vinimos a alentar,\n Para ser campeon , \n Hoy hay que ganar"


fichero=open("penarol.txt","w")
fichero.write(texto) 
fichero.close()
del(fichero)



