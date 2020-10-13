lista = input().split()
m = int(lista[0])
n = int(lista[1])
while m > 0 and n > 0:
    if m > n:
        i = 0
        soma = 0
        while i <= m-n:
            print(n+i,end=" ")
            soma += n+i
            i += 1   
        print("Sum=%d"%(soma))
    else:
        i = 0
        soma = 0
        while i <= n-m:
            print(m+i,end=" ")
            soma += m+i
            i += 1   
        print("Sum=%d"%(soma))
    lista = input().split()
    m = int(lista[0])
    n = int(lista[1])    
