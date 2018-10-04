def busqueda_cuaternaria(lista, izq, der, numero):
    #Comprobacion del primer y ultimo indice de la lista
    if der >= izq:
        #Definicion de la ubicacion de los dos puntos que dividen la lista en 3
        cuarto1 = izq + (der - izq)/4
        mitad = izq + (der - izq)/2
        cuarto2 = izq + 3*(der - izq)/4

        #Comprobaciones, si el numero a buscar se encuentra en alguna de las divisiones, regresa el indice
        if lista[cuarto1] == numero:
            return cuarto1
        if lista[mitad] == numero:
            return medio
        if lista[cuarto2] == numero:
            return cuarto2

        #Si no se encuentra el numero dentro de alguno de los puntos, hace una llamada recursiva, 
        #modificando los extremos izquierdo o derecho, segun sea el caso
        #izq < numero < derecho
        if lista[cuarto1] > numero:
            return busqueda_cuaternaria(lista, izq, cuarto1-1, numero)
        elif lista[mitad] > numero:
            return busqueda_cuaternaria(lista, cuarto1+1, mitad-1, numero)
        elif lista[cuarto2] > numero and numero > lista[mitad]:
            return busqueda_cuaternaria(lista, mitad+1, cuarto2-1, numero)
        else:
            return busqueda_cuaternaria(lista, cuarto2+1, der, numero)
        
    return -1

print("Busqueda cuaternaria")
print("Para dejar de ingresar valores, escribir -1000")
valor = input("Valor: ")

lista = []

#Recibe valores hasta que se ingresa -1000
while valor != -1000:
    if valor not in lista:
        lista.append(valor)
    else:
        print("Valor repetido")
    
    valor = input("Valor: ")

#print("Lista: ", lista)
#Ordenamiento de la lista
lista.sort()
print(lista)

#Comprobacion de lista, si esta vacia o no
if lista:
    #Indice final e inicial de la lista
    izq = 0
    der = len(lista)-1

    print(izq, der)
    #Recibe numero a buscar
    numero = input("Numero a buscar: ")
    #Llamada a la funcion, regresa la posicion del numero que se busca o -1 si no lo encuentra
    posicion = busqueda_cuaternaria(lista, izq, der, numero)
    #imprime el resultado de la busqueda
    if posicion == -1:
        print("El numero no se encuentra en la lista")
    else:
        print("El numero "+ str(numero) + " se encuentra en la posicion "+ str(posicion))
else:
    print("Lista vacia")