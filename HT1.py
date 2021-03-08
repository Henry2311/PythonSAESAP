print("--------HOJA DE TRABAJO 1--------")
print("-----------EJERCICIO 1-----------")
print("")
print("=======Triángulo Rectángulo=======")
num1=int(input("Ingrese la altura del triángulo: "))

for i in range(num1):
    for j in range(i+1):
        print("*",end=" ")
    print("")
print("==================================")
print("")

print("-----------EJERCICIO 2-----------")
print("========Cuenta Regresiva=========")
num2=int(input("Ingrese un número para la cuenta regresiva: "))
for i in range(num2+1):
    print(num2-i, end=",")
print("")
print("=============================================") 
print("")

print("-----------EJERCICIO 3-----------")
print("=====Validación número primo=====")
num = int(input("Ingrese un número entero positivo: "))
resto = num%2
if num>=0:
    if resto==0:
        print("El número: "+str(num)+" es par.")
    else:
        print("El número: "+str(num)+" es impar.")
else:
    print("Ingrese un número positivo")
print("==================================")