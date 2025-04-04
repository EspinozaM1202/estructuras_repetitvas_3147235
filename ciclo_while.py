#Variable contadora
#Imprimir la tabla de multiplicar del número que un usuario
#ingrese utilizando un ciclo while.
numero = int(input("Ingrese un número: "))
i= 10
while i > 1 : 
  resultado = numero * i
  print( numero, "X", i, "=", resultado )
  i = i - 1