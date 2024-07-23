


#começo do programa 
def main():
    print("==============JOGO DE ADIVINHAÇÃO============")
#gerando um número aleatório com o random.randint
import random
numero_aleatorio = random.randint(1,100)
numero = 0
lista_tentativas()
print(numero_aleatorio)
while numero != numero_aleatorio:
#pedindo um número para o usuário adivinhar
        numero = int(input("Digite o número que você deseja entre 1 e 100:  "))
        print("VOCÊ ERROU, NÃO DESANIME, TENTE NOVAMENTE!")

print("VOCÊ ACERTOU! ")








main()