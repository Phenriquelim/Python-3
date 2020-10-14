n = int(input())
while n < 1 and n > 4:
    n = int(input())
a = g = d = 0
while n != 4:
    if n == 1:
        a += 1
    elif n == 2:
        g += 1
    elif n == 3:
        d += 1
    n = int(input())
    while n < 1 and n > 4:
        n = int(input())
print("MUITO OBRIGADO")        
print("Alcool: %d"%a)
print("Gasolina: %d"%g)
print("Diesel: %d"%d)

    
