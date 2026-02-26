count_bubble = 0
count_selection = 0
count_insertion = 0


with open("./saida.txt", "r") as file:
    lista = []
    for item in file:
        print(item, end=" ")
        lista.append(item)

#Bubble sort

    done = False
    while(not done):
        done = True
        for i in range(0, len(lista) - 1):
            count_bubble += 1
            if(lista[i] > lista[i + 1]):
                temp = lista[i + 1]
                lista[i + 1] = lista[i]
                lista[i] = temp
                done = False

    print("Bubble sort: ")
    print(lista)
#Selection sort

with open("./saida.txt", "r") as file:
    lista = []
    for line in file:
        lista.append(line)

    for i in range(len(lista)):
        min_index = i

        for j in range(i + 1, len(lista)):
            count_selection += 1
            if(lista[j] < lista[min_index]):
                min_index = j

        temp = lista[i]
        lista[i] = lista[min_index]
        lista[i] = temp

print("Selection sort:")
print(lista)

#Insertion sort

with open("./saida.txt", "r") as file:
    lista = []
    for line in file:
        lista.append(line)

for i in range(1, len(lista)):
    chave = lista[i]
    j = i - 1
    
    while(j >= 0) and (lista[j] > chave):
        count_insertion += 1
        lista[j + 1] = lista[j]
        j -= 1

    lista[j + 1] = chave

print("Insertion sort")
print(lista)
print(f"Bubble: {count_bubble} | Selection: {count_selection} | Insertion: {count_insertion}")
