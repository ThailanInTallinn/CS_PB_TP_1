lista = []
with open("./saida.txt", "r") as file:
    for item in file:
        print(item, end=" ")
        lista.append(item)

#Bubble sort

    done = False
    while(not done):
        done = True
        for i in range(0, len(lista) - 1):
            if(lista[i] > lista[i + 1]):
                temp = lista[i + 1]
                lista[i + 1] = lista[i]
                lista[i] = temp
                done = False

    print("Bubble sort: ")
    for item in lista:
        print(item)

#Selection sort

with open("./saida.txt", "r") as file:
    lista = []
    for line in file:
        lista.append(line)

    for i in range(len(lista)):
        min_index = i

        for j in range(i + 1, len(lista)):
            if(lista[j] < lista[min_index]):
                min_index = j

        temp = lista[i]
        lista[i] = lista[min_index]
        lista[i] = temp

print(lista)
