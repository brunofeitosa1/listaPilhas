import random
import time
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
    
    #retorna Elementos na fila
    def Tamanho(self):
        return len(self.itens)
    
    #adiciona elemento no final da fila
    def Adicionar_na_Fila(self, item,prioridade):
        elemento = Elemento_da_Fila(item, prioridade)
        self.itens.insert(0, elemento)
        print(f"O Avião: {elemento} entrou na fila")
    
    #Decolagem do AVIÃO    
    def decolagem(self):
        Aviao_Decolagem = self.itens.pop(-1)
        
        print(f"Autorizado a decolagem do Avião {Aviao_Decolagem.item}\n")
        
        print(f"O Avião {Aviao_Decolagem.item} Decolou!!\n")
       
    #Imprimir fila
    def imprimir_queue(self):
        Lista = []
        for x in self.itens:
            Lista.append(x.item)
        print(f"Aviôes na Fila = {Lista}") 
    
    #Caracteristicas do Primeiro Avião
    def caracteristicas(self):
        Primeiro_aviao = self.itens[-1]
        print(f"Nome do Primeiro: Avião da Fila {Primeiro_aviao.item},Com a Numeração {Primeiro_aviao.prioridade}\n")
              
def main():
    Fila = Fila_de_Prioridade()
    
    Fila.imprimir_queue()
    Fila.Adicionar_na_Fila("AviãoGol",67)
    time.sleep(2)
    Fila.Adicionar_na_Fila("AviãoTelas",12)
    time.sleep(2)
    Fila.Adicionar_na_Fila("AviãoHidro",9)
    time.sleep(2)
    Fila.imprimir_queue()
    time.sleep(2)
    Fila.decolagem()
    time.sleep(2)
    Fila.caracteristicas()

if __name__ == '__main__':
    main()