from random import randint
condição = 1
lista = []
ValorDeVenda = 0
while condição != 0:  
    AnoVenda = int(input("Digite o ano da venda: "))
    while AnoVenda < 2016 or AnoVenda > 2019:
        print("Ano invalido")
        AnoVenda = int(input("Digite o ano da venda: "))
    MesVenda = int(input("Digite o mes da venda: "))
    while MesVenda > 12 or MesVenda < 1:
        print("Mes invalido")
        MesVenda = int(input("Digite o mes da venda: "))
    DiaVenda = int(input("Digite o dia da venda: "))
    while DiaVenda > 31 or DiaVenda < 1:
        print("Dia Invalido")
        DiaVenda = int(input("Digite o dia da venda: "))
    QtdeVendasDia = int(input("Digite a quantidade de vendas no dia {:0>2}/{:0>2}/{}: ".format(DiaVenda,MesVenda,AnoVenda)))
    while QtdeVendasDia < 0:
        print("A quantidades de vendas deve ser maior que 0")
        QtdeVendasDia = int(input("Digite a quantidade de vendas no dia {:0>2}/{:0>2}/{}: ".format(DiaVenda,MesVenda,AnoVenda)))
    ContadorVendas = 1
    while ContadorVendas <= QtdeVendasDia:
        CodigoVenda = int(input("Digite o codigo do item vendido:: "))
        ValorDeVenda = 0
        while CodigoVenda < 10000 or CodigoVenda > 99999:
            print("O codigo do item deve estar em um intervalo de [10000-99999]")
            CodigoVenda = int(input("Digite o codigo do item vendido:: "))
        for linha in open("PRODUTOS.txt"):
            linha = linha.rstrip()
            lista = linha.split(";")
            lista[0] = int(lista[0])
            if lista[0] == CodigoVenda:
                ValorDeCusto = float(lista[3])
                MargemDeLucro = float(lista[4])
                ValorDeVenda = ValorDeCusto * ((MargemDeLucro/100)+1) 
                Tipo = lista[1]
                desconto = randint(1, 100)
                print(desconto)
                taxa = 1+ (randint(-8, 8)/100)
                if desconto <= 35:
                    ValorDeVenda = ValorDeVenda * taxa
        if ValorDeVenda == 0:
            print("Codigo não cadastrado")
        else:
            if Tipo == "U":
                QtdeVendasProduto = int(input("Digite a quantidade de itens vendido: "))
            elif Tipo == "P":
                QtdeVendasProduto = float(input("Digite a quantidade vendida em Kg: "))
            arq = open("PRODUTOSVENDIDOS.txt", "a")
            arq.write("{};{:0>2};{:0>2};{};{:.3f};{:.2f}\n".format(AnoVenda,MesVenda,DiaVenda,CodigoVenda,QtdeVendasProduto,ValorDeVenda))
            arq.close()
            ContadorVendas += 1
    condição = int(input("Digite 1 para repetir ou 0 para sair do programa: "))
    while condição != 0 and condição != 1:
        print("Os valores só podem ser 0 ou 1")
        condição = int(input("Digite 1 para repetir ou 0 para sair do programa: "))
