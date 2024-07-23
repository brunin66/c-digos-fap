print("=================CALCULADORA DE JUROS SIMPLES=================")




valorinicial = float(input("Qual o seu montante inicial? :"))
taxa = float(input("Qual é a taxas de juros? (%):  "))
tempo = float(input("Quanto tempo está no contrato? (A): "))


Juros = valorinicial*taxa*tempo
Montante = valorinicial + Juros

print("O SEU VALOR TOTAL SERÁ, : ", Montante)