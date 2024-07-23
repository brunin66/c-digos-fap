print("====================CALCULADORA DE DESCONTOS========================")





produto = float(input("Qual é o valor do seu produto?"))
desconto = float(input("Qual a porcentagem de desconto? (%):  "))

valorfinal = (desconto*produto)/100
valorcomdesconto = produto - valorfinal

print(" valor do seu desconto é de: ", valorfinal)
print("O valor total a pagar será: ", valorcomdesconto)