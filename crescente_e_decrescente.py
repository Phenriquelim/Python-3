lista = input().split()
x = int(lista[0])
y = int(lista[1])
while x != y:
    if x > y:
        print("Decrescente")
    else:
        print("Crescente")
    lista = input().split()
    x = int(lista[0])
    y = int(lista[1])
        
