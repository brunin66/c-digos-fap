print("=========================NOTA FINAL ALUNO======================")




nota1 = float(input("DIGITE A SUA PRIMEIRA NOTA! :"))
nota2 = float(input("DIGITE A SUA SEGUNDA NOTA! :"))
nota3 = float(input("DIGITE A SUA TERCEIRA NOTA! :"))

média = (nota1+nota2+nota3)/3


if média <7:
    print("VOCÊ ESTÁ NA PROVA FINAL, SUA MÉDIA É: ", média)
    recuperação = float(input("QUAL FOI A SUA NOTA NA recuperação?"))
    notafinal = (recuperação+média)/2 
    if notafinal => 7:
        print("VOCÊ ESTÁ APROVADO! PARABÉNS! A SUA MÉDIA FOI: ", notafinal)


else média >= 7:
    print("VOCÊ ESTÁ APROVADO! PARABÉNS! SUA MÉDIA FOI", média)
