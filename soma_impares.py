x = int(input())
i = 0
while i < x:
    lista = input().split()
    m = int(lista[0])
    n = int(lista[1])
    if m > n:
        cont = 0
        soma = 0
        while cont < m-n-1:
            if (n+cont+1)%2 != 0:
                soma += n+cont+1
            cont += 1   
        print(soma)
    else:
        cont = 0
        soma = 0
        while cont < n-m-1:
            if (m+cont+1)%2 != 0:
                soma += m+cont+1
            cont += 1   
        print(soma)
    i += 1    
