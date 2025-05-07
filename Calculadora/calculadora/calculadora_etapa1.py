#passo 1: Solicitar ao usuário os números e o operador
numero1=float(input("Digite o primeiro número: "))
operador=input("digite o operador (+,-,*,/): ")
numero2=float(input("Digite o segundo número: "))
 #Passo 2: Realizar a operação com base no operador
if operador=="+":
    resultado=numero1+numero2
elif operador=="-":
    resultado=numero1-numero2
elif operador=="*":
    resultado=numero1*numero2
elif operador=="/":
    resultado=numero1/numero2
else:
    print("Operador inválido!")

#Passo 3: Exibir o resultado
print("Resultado:", resultado)