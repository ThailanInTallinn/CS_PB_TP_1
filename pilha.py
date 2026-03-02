tamanho_max = 10

def top(pilha):
    return len(pilha)


def adicionar(item, pilha):
    counter  = 0
    tip = top(pilha)
    counter += 1
    if(tip == tamanho_max):
        counter += 1
        print("Tamanho máximo atingido.")
        print(f"Numero de passos para adição malssucedida: {counter}")
        return -1

    pilha.append(item) 
    counter += 1
    print(f"Numero de passos para adição feita com sucesso: {counter}")
    return 1

def remover(pilha):
    counter = 0
    if(top(pilha) == 0):
        counter += 1
        print("Pilha vazia.")
        print(f"Numero de passos para remoção malssucedida: {counter}")
        return -1

    removed = pilha.pop()
    counter += 1
    print(f"Numero de passos para remoção feita com sucesso: {counter}")
    return removed

pilha = []
for i in range(0, 10):
    adicionar(i + 1, pilha)

print(pilha)

remover(pilha)
print(pilha)
