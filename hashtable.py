#Hashtable

class Hashtable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _funcao_hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave, valor):
        contador = 0
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]

        for i, (chave_ex, _) in enumerate(bucket):
            contador += 1
            if(chave_ex == chave):
                bucket[i] = (chave, valor)
                print(f"Numero de passos para inserção com chave existente: {contador}")
                return 
            
        bucket.append((chave, valor))
        contador += 1
        print(f"Numero de passos para inserção sem chave existente: {contador}")



    def buscar(self, chave):
        contador = 0
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]

        for chave_ex, valor in bucket:
            contador += 1
            if(chave_ex == chave):
                print(f"Numero de passos para busca bem-sucedida: {contador}")
                return valor

        print(f"Numero de passos para busca que não retornou resultado: {contador}")
        return None

    def remover(self, chave):
        contador = 0
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]

        for i, (chave_ex, valor) in enumerate(bucket):
            contador += 1
            if chave_ex == chave:
                print(f"Numero de passos para remoção bem-sucedida: {contador}")
                del bucket[i]

        print(f"Numero de passos para remoção malssucedida: {contador}")

        return None


hashtable = Hashtable(10)

with open("./saida.txt", "r") as file:
    for i, line in enumerate(file):
        hashtable.inserir(i, line)

print(hashtable.tabela)  
