print("=============================")
print("---INDICE DE MASA CORPORAL---")
p = input("¿Cuál es tu peso?")
a = input("¿Cuál es tu estatura?")
div = float(a)*float(a)
imc=round((float(p)/div),2)
print("Tu IMC es: "+ str(imc))
print("=============================")