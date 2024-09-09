"""
 Escreva um programa que verifique, em uma string, a existência da
letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade
de vezes em que ela ocorre.
IMPORTANTE: Essa string pode ser informada através de qualquer 
entrada de sua preferência ou pode ser previamente definida no código;
"""

def verificar_letra_a(string):
    count_a = string.lower().count('a')
    
    if count_a > 0:
        print(f"A letra 'a' aparece {count_a} vezes na string")
    else:
        print("A letra 'a' não aparece na string")

texto = input("Informe uma string para verificar a quantidade de vezes que a letra 'a' aparece: ")
verificar_letra_a(texto)