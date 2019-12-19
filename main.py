from io import open

texto="Vamos Vamos Penarol ,\n Hoy te vinimos a alentar,\n Para ser campeon , \n Hoy hay que ganar"

fichero=open("penarol.txt","w")
fichero.write(texto) 
fichero.close()

##################################################################################################

fichero=open("penarol.txt","r")
#el metodo read() lee todas las lineas del fichero 
texto=fichero.read()
#Siempre hay que cerrar el fichero despues de haberlo utilizado
fichero.close()
print(texto) 

##################################################################################################

fichero=open("penarol.txt","r")
#readlines() lee cada linea y la guarda como elemento de una lista
texto=fichero.readlines()
fichero.close()

print("")

for idx,line in enumerate(texto): 
  print("Linea ",idx+1,"=> ",line)

##################################################################################################


fichero=open("penarol.txt","a")

fichero.write("\n Carbone , Carbone, Carbone.....")
fichero.close()
fichero=open("penarol.txt","r")
lineas=fichero.readlines()
fichero.close()

print(lineas)

print("")

for idx,lin in enumerate(lineas): 
  print(idx+1,lin)

#################################################################################################
#Otro metodo para leer linea por linea 
print("")
with open("penarol.txt","r") as lineas: 
  print(type(lineas)) #devuelve la clase
  print(lineas) #Devuelve la clase y detalles del objeto ? averiguar 
  #No es una lista, pero lo estoy indexando con enumerate
  for idx,linea in enumerate(lineas): 
    print(idx," ",linea)












