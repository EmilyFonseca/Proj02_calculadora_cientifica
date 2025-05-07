#Passo 1: Importar o modulo math
import math

def adicionar(n1, n2):
    return n1 + n2
def subtrair(n1, n2):
    return n1 - n2
def multiplicar(n1, n2):
    return n1 * n2
def dividir(n1, n2):
    return n1 / n2

# Passo 2: Definir funções para calculos de potenciação, radiciação, trigonometria e logaritmos.
def potencia(base, expoente):
    return math.pow(base, expoente)

def radiciacao(numero, raiz):
    if numero < 0 and raiz % 2 == 0:
        raise ValueError("Raiz par de número negativo não é permitida.")
    return math.pow(numero, 1/raiz)

def seno(angulo_graus):
    return math.sin(math.radians(angulo_graus))

def cosseno(angulo_graus):
    return math.cos(math.radians(angulo_graus))
def tangente(angulo_graus):
    return math.tan(math.radians(angulo_graus))
def logaritmo(numero, base):
    if numero <= 0 or base == 1:
        raise ValueError("Número deve ser positivo e base positiva diferente de 1.")
    return math.log(numero, base)

try:
    num1_str = input("Digite o primeiro número: ")
    operador = input("Digite o operador (+, -, *, /, **, sqrt, sin, cos, tan, log): ")
    num2_str = input("Digite o segundo número (ou raiz/expoente/base para outras operações): ")

    if not num1_str.replace('.', '', 1).isdigit() or not num2_str.replace('.', '', 1).isdigit():
        raise ValueError("Por favor, insira números válidos.")
    else:
        num1=float(num1_str)
        num2=float(num2_str)
        resultado = None

        if operador in ['+', '-', '*', '/', '**', 'rad', 'sen', 'cos', 'tan', 'log']:
            if operador == '+':
                resultado = adicionar(num1, num2)
            elif operador == '-':
                resultado = subtrair(num1, num2)
            elif operador == '*':
                resultado = multiplicar(num1, num2)
            elif operador == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                else:
                    resultado = dividir(num1, num2)
            elif operador == '**':
                resultado = potencia(num1, num2)
            elif operador == 'rad':
                resultado = radiciacao(num1, num2)
            elif operador == 'sen':
                resultado = seno(num1) #Assume que o primeiro número é o ângulo em graus
            elif operador == 'cos':
                resultado = cosseno(num1) #Assume que o primeiro número é o ângulo em graus
            elif operador == 'tan':
                resultado = tangente(num1) #Assume que o primeiro número é o ângulo em graus
            elif operador == 'log':
                resultado = logaritmo(num1, num2)
            #Passo 5: Exibir o resultado.   
            print(f"Resultado: {resultado}")
        else:
            # Passo 3: Exibir mensagens de erro apropriadas.
            raise ValueError("Operador inválido. Use +, -, *, /, **, rad, sen, cos, tan ou log.")
except ValueError as e:
    print(f"Erro: {e}")
except ZeroDivisionError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
            