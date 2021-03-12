#ejercicio 1
print("=====Ejercicio 1=====")
contraseña1="contraseña"
Contraseña2 =input("Ingrese una contraseña: ")
if contraseña1.lower()==Contraseña2.lower():
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
print("======================")

#EJERCICIO 2:
print("=====Ejercicio 2=====")
nombre1=input("Ingrese su nombre para saber su grupo: ")
nombre=nombre1.lower()
sexo=input("Ingrese su genero (hombre o mujer) para saber su grupo: ")
if sexo.lower()=="mujer":
    if nombre[0]=="a" or nombre[0]=="b" or nombre[0]=="c" or nombre[0]=="d" or nombre[0]=="e"or nombre[0]=="f" or nombre[0]=="g"or nombre[0]=="h" or nombre[0]=="i"or nombre[0]=="j" or nombre[0]=="k" or nombre[0]=="l":
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")
if sexo.lower()=="hombre":
    if nombre[0]=="ñ" or nombre[0]=="o" or nombre[0]=="p" or nombre[0]=="q" or nombre[0]=="r" or nombre[0]=="s" or nombre[0]=="t" or nombre[0]=="u" or nombre[0]=="v" or nombre[0]=="w" or nombre[0]=="x" or nombre[0]=="y" or nombre[0]=="z":
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")
print("======================")
