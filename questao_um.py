"""
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo 
valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 
3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar 
onde, informado um número, ele calcule a sequência de Fibonacci e
retorne uma mensagem avisando se o número informado pertence ou
não a sequência.
IMPORTANTE: Esse número pode ser informado através de qualquer
entrada de sua preferência ou pode ser previamente definido no código;
"""                                                   

def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    if n in fib_seq:
        print(f"O número {n} pertence à sequência de Fibonacci")
    else:
        print(f"O número {n} NÃO pertence à sequência de Fibonacci")

numero = int(input("Informe um número para verificar se ele pertence à sequência de Fibonacci: "))
fibonacci(numero)