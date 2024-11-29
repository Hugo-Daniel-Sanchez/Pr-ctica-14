print("Programa desarrollado por: Sánchez Vázquez Hugo Daniel")
n = int(input("Dime hasta que numero de formula deseas llegar:  "))

x = 0
z = 1
i = 2
temp = None

while i < n:
    temp = z
    z += x
    x = temp
    i += 1
    
print(f"El termino {n} de la serie fibonacci es: {z}")