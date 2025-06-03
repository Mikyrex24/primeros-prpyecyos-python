# Calculadora simple

print("Elige la operación que quieres realizar:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

operacion = input("Ingresa el número de la operación (1-4): ")
#Resolviendo
num1 = float(input("Ingresar el primer numero: "))
num2 = float(input("Ingresar el segundo numero: "))

if operacion == "1":
    resultado = num1 + num2 
    print("La suma de este resultado es: ", resultado)
elif operacion == "2":
    resultado = num1 - num2
    print("El resultado de esta resta es: ", resultado)
elif operacion == "3":
    resultado = num1 * num2
    print("El resultado de esta multiplicacion es: ", resultado)
elif operacion == "4":
    if  num2 != 0:
      resultado = num1 / num2
      print("El resultado de esta division es: ", resultado)
    else:
         print("Error: No se puede dividir entre cero.")

else : 
    print("Ingrese un valor valido")



