tamanho_max = 10

def top(pilha):
    return len(pilha)


def adicionar(item, pilha):
    tip = top(pilha)
    if(tip == tamanho_max):
        print("Tamanho máximo atingido.")
        return -1

    pilha.append(item) 
    return 1

def remover(pilha):
    if(top(pilha) == 0):
        print("Pilha vazia.")
        return -1

    removed = pilha.pop()
    return removed

pilha = []
for i in range(0, 10):
    adicionar(i + 1, pilha)

print(pilha)

remover(pilha)
print(pilha)
