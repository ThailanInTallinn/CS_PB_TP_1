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

for item in lista:
    print(item)
