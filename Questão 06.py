import random

lista = []

#Inseri item
def inserir_lista(chave, lista):
    lista.append(chave)
    i, p = 0, 0
    while lista[i] < chave:
        i += 1
    p = len(lista) - 2
    while p >= i:
        lista[p + 1] = lista[p]
        p -= 1
    lista[i] = chave

#Busca Elemento
def busca_sentinela(chave, lista):
    """ Algoritmo de busca sentinela """
    lista.append(chave)
    i = 0
    while lista[i] != chave:
        i += 1
    if i == len(lista) - 1:
        lista.pop()
        return -1
    lista.pop()
    return i

#Deleta Elemento
def deleta_valor(chave, lista):
    """ Deleta uma chave na lista """
    posicao = busca_sentinela(chave, lista)
    if posicao >= 0:
        lista.pop(posicao)
        return True
    return False

#MostraLista
def mostra_lista(lista):
    """ Imprime a lista """
    print(lista)
def main():
    for _ in range(0, 10):
        inserir_lista(random.randint(10, 99), lista)

    mostra_lista(lista)
    print("\n")
    deleta_valor(5, lista)
    print("\n")
    mostra_lista(lista)
    
if __name__ == '__main__':
    main()