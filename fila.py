#Fila
tamanho_max = 100
contador = 0

def adicionar(fila, item, count):
    counter = 0
    if(count >=tamanho_max):
        counter += 1
        print("Fila já atingiu seu tamanho máximo.")
        print(f"Numero de passos para adição malssucedida: {counter}")
        return -1
    
    fila[count] = item
    counter += 1
    print(f"Numero de passos para adicao feita com sucesso: {counter}")
    return 1

def remover(fila):
    counter = 0
    if(fila[0] == "\0"):
        counter += 1
        print("Fila vazia.")
        print(f"Numero de passos para remoçao malssucedida: {counter}")
        return "\0"

    primeiro_elemento = fila[0]
    counter += 1

    for i in range(1, tamanho_max - 1):
        fila[i - 1] = fila[i]
        counter += 1
        fila[i] = "\0"
        counter += 1
        
    print(f"Numero de passos para remoção feita com sucesso: {counter}")
    return primeiro_elemento


def preencher():
    fila = [] 
    for i in range(0, tamanho_max):
        fila.append("\0")

    return fila



with open("saida.txt", "r") as file:
    fila = preencher()
    added = 0
    for line in file:
        added = adicionar(fila, line, contador)
        if(added > 0):
            contador += 1

print(fila)

remover(fila)
print(fila)

