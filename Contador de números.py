print("===================CONTADOR DE NÚMEROS=======================")




numero1 = int(input("DIGITE O SEU NÚMERO:  "))
numero2 = int(input("DIGITE O SEU SEGUNDO NÚMERO:  "))


soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1/numero2

def menu():
    print("OPÇÃO 1: SOMAR:   ")
    print("OPÇÃO 2 SUBTRAIR:  ")
    print("OPÇÃO 3 MULTIPLIQUE:  ")
    print("OPÇÃO 4 DIVISÃO:  ")
    opcao = int(input("DIGITE O  NÚMERO DA SUA OPÇÃO:  "))
    if opcao == 1:
        print(f"O VALOR DA SUA SOMA É: {soma}")
        resultado = soma
    elif opcao == 2:
        print(f"O VALOR DA SUA SUBTRAÇÃO É:  {subtracao}")    
        resultado = subtracao
    elif opcao == 3: 
        print(f"O VALOR DA SUA MULTIPLICAÇÃO É:  {multiplicacao}")
        resultado = multiplicacao
    elif opcao == 4:
        print(f"O VALOR DA SUA DIVISÃO FOI:  {divisao}")
        resultado = divisao
    else:
        print("VALOR INVÁLIDO")

    return resultado

if resultado % 2 == 0:
        print(f"o numero {resultado} é par")

else:
        print(f"o numero {resultado} é impar")

      
menu()




def main():
    menu()








main()
  












