#Fila
tamanho_max = 100
contador = 0

def adicionar(fila, item, count):
    if(count >=tamanho_max):
        print("Fila já atingiu seu tamanho máximo.")
        return -1
    
    fila[count] = item
    return 1

def remover(fila):
    if(fila[0] == "\0"):
        print("Fila vazia.")
        return "\0"

    primeiro_elemento = fila[0]

    counter = len(fila)

    for i in range(1, tamanho_max - 1):
        fila[i - 1] = fila[i]
        fila[i] = "\0"

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

