import random

# Crear lista de 10 numeros aleatorios
numeros = [random.randint(1, 100) for i in range(100)]

def burbuja(lista):
    a = lista.copy()
    iteraciones = 0

    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            iteraciones += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a, iteraciones

def insercion(lista):
    a = lista.copy()
    iteraciones = 0

    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1

        while j >= 0:
            iteraciones += 1

            if a[j] > clave:
                a[j + 1] = a[j]
                j -= 1
            else:
                break

        a[j + 1] = clave

    return a, iteraciones

while True:
    print("\n--- MENU DE ORDENAMIENTO ---")
    print("1. Mostrar lista")
    print("2. Ordenar por burbuja")
    print("3. Ordenar por insercion")
    print("4. Comparar iteraciones")
    print("5. Salir")

    opcion = input("Elija una opcion: ")

    if opcion == "1":
        print("Lista original:", numeros)

    elif opcion == "2":
        resultado, vueltas = burbuja(numeros)
        print("Lista ordenada:", resultado)
        print("Iteraciones:", vueltas)

    elif opcion == "3":
        resultado, vueltas = insercion(numeros)
        print("Lista ordenada:", resultado)
        print("Iteraciones:", vueltas)

    elif opcion == "4":
        lista1, vueltas1 = burbuja(numeros)
        lista2, vueltas2 = insercion(numeros)

        print("\nLista original:", numeros)
        print("\nBurbuja:", lista1)
        print("Iteraciones burbuja:", vueltas1)

        print("\nInsercion:", lista2)
        print("Iteraciones insercion:", vueltas2)

        if vueltas1 < vueltas2:
            print("\nBurbuja utilizo menos iteraciones.")
        elif vueltas2 < vueltas1:
            print("\nInsercion utilizo menos iteraciones.")
        else:
            print("\nLos dos utilizaron las mismas iteraciones.")

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opcion no valida.")
