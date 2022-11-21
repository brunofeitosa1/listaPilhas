import random

class structure:

    def __init__(self):
        self.__structure = []

#Adiciona o valor (value) ao final da pilha 
    def push(self, value):       
        self.__structure.append(value)

#Remove o último valor da pilha
    def pop(self):
        return self.__structure.pop()
    
#Remove o último valor da pilha
    def show(self):
        print(f'Lista Carros na rua: {self.__structure}\n')
               
#imprimir os carro que serão retirados na frente
    def RetiradaCarrosDeTras(self):
        Escolha = int(input("Digite a placa do carro: "))
        
        if(Escolha in self.__structure):
            print("Esta estacionado!")
            print(f'Os carro que precisam ser retirados são: {self.__structure[self.__structure.index(Escolha)+1::]}\n')
            
        else:
            print("Carro não está na rua!")
            return 0

#imprimir os carro que serão retirados de trás
    def RetiradaCarrosDaFrente(self):
        Escolha = int(input("Digite a placa do carro: "))
        
        if(Escolha in self.__structure):
            print("Esta estacionado!")
            print(f'Os carro que precisam ser retirados são: {self.__structure[self.__structure.index(Escolha)-1::-1]}\n')
            
        else:
            print("Carro não está na rua!")
            return 0
        
def main():
    
    #Cria uma pilha e utiliza os métodos show, pop e push
    estrutura = structure()
    
    #Gera valores randomicos
    for _ in range(0, 10):
        estrutura.push(random.randint(1000, 9999))
    estrutura.show()
    
    #Teste retirar os carrros da frente
    estrutura.RetiradaCarrosDeTras()
    
    #Teste retirar os carros de trás
    estrutura.RetiradaCarrosDaFrente()

if __name__ == '__main__':
    main()