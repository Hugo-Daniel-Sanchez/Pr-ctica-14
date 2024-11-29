print("Programa realizado por: Sánchez Vázquez Hugo Daniel y Olvera Martinez Maximiliano")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def pascal(filas):
    for i in range(filas):
        print(" " * (filas - i - 1), end="")  
        for j in range(i + 1):
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
        print()

num_filas = int(input("Inserte el número de filas del Triángulo de Pascal: "))
pascal(num_filas)