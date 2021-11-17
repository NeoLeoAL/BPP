import pdb
pdb.set_trace()

listadoMax = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
listadoPimos = [3, 4, 8, 5, 5, 22, 13]

def numPrimos(n):
    primo = True
    for i in range(2, n):
        if(n % i == 0):
            primo = False
    return primo

def numMax(n):
    aux = 0
    for i in n:
        if i > aux:
            aux = i     
    return aux

if __name__ == '__main__':
    numerosMax = list(map(numMax, listadoMax))
    print(numerosMax)
    
    numerosPrimos = list(filter(numPrimos, listadoPimos))
    print(numerosPrimos)