import random

class Fila:
    def __init__(self):
        self.__Fila = []

    def enFila(self, value):
        self.__Fila.append(value)

    def show(self):
        print(f'Soldados Presentes no Campo de Batalha: {self.__Fila}\n')
        
    def Sorteio(self):
        #Salvar a Lista
        Lista_Soldados = self.__Fila
        #Sorteio do numero
        #contador
        contador = 9
        for i in range(9):
            retirar = random.randint(0,contador)
            print(f"O Numero sorteado foi o {retirar}")
            print(f"O soldado que irar sair sera o: {Lista_Soldados.pop(retirar)}")
            contador = contador -1
            print(f'Sobrou os Sequintes Soldados: {Lista_Soldados}')
            print("------------------------------------------------------------------\n")

def main():
    soldados = Fila()

    #Numeração dos Soldados
    for _ in range(0, 10):
        soldados.enFila(random.randint(10, 99))

    soldados.show()
    
    soldados.Sorteio()


if __name__ == '__main__':
    main()