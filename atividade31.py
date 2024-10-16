# Crie uma função chamada verificar_paridade que receba um número inteiro
# como argumento e retorne uma mensagem indicando se o número é par ou ímpar.

def verificar_paridade():
    num = int(input("Digite um numero:"))
    if num % 2 == 0:
        return "Par"
    else:
        return "Impar"

b = verificar_paridade()
print(b)