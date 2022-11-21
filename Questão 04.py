import random
import time

#Funçaõ cria Pessoas
class Elemento_da_Fila:
    def __init__(self, valor, prioridade):
        self.item = valor
        self.prioridade = prioridade
    
    def __str__(self):
        return str(self.item) + ' ' + str(self.prioridade)

class Fila_de_Prioridade:
    #inicia a fila vazia
    def __init__(self):
        self.itens = []
    
    #Verifica se a fila está vazia
    def Fila_Vazia(self):
        return self.itens == []
    
    #retorna Elementos da fila
    def Tamanho(self):
        return len(self.itens)
    
    #adiciona elemento no final da fila
    def Adicionar_na_Fila(self, item,prioridade):
        elemento = Elemento_da_Fila(item, prioridade)
        self.itens.insert(0, elemento)
        print(f"Entrou na fila: {elemento.item} com idade = {elemento.prioridade}")

    #Remove elemento com maior prioridade
    def Remover_Elemento_de_Baixa_Prioridade(self):
        if self.Fila_Vazia():
            print("Fila Vazia")
            
        else:
            posicao = 0
            maior = self.itens[posicao].prioridade
            
            for i in range(self.Tamanho()):
                if self.itens[i].prioridade > maior:
                    posicao = i
                    maior = self.itens[i].prioridade
            
            removido = self.itens.pop(posicao)
            print(f"Pessoa {removido.item} foi removida da Fila")
            
            return removido.item
        
    #Imprimir fila
    def imprimir_queue(self):
        Lista = []
        for x in self.itens:
            Lista.append(x.item)
        print(f"Pessoas na Fila = {Lista}")
              
def main():
    Fila = Fila_de_Prioridade()
    
    Fila.imprimir_queue()
    Fila.Adicionar_na_Fila("Senhor",67)
    time.sleep(2)
    Fila.Adicionar_na_Fila("joven",12)
    time.sleep(2)
    Fila.Adicionar_na_Fila("criança",9)
    time.sleep(2)
    Fila.imprimir_queue()
    Fila.Remover_Elemento_de_Baixa_Prioridade()
    Fila.imprimir_queue()

if __name__ == '__main__':
    main()