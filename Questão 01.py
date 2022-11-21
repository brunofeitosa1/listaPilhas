import random

class structure:

    def __init__(self):
        self.__structure = []


    def push(self, value):       
        self.__structure.append(value)


    def pop(self):
        return self.__structure.pop()
    

    def show(self):
        print("Imprimir Ordem ")
        print(f'structure: {self.__structure}\n')
        

    def tras(self):
        print("Imprimir ordem Invera")
        print(f'structure: {self.__structure[::-1]}\n')
        
    def main(self):
    
    
        estrutura = structure()

    for _ in range(0, 10):
        estrutura.push(random.randint(10, 99))
    
    
    estrutura.show()
    
    
    estrutura.pop()
    estrutura.pop()
    
    
    estrutura.tras()

    if __name__ == '__main__':
          main()