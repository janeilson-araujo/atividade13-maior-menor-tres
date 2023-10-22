# Exercício Python 14: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.

print("descubra qual dos números é maior e qual é o menor")
numero1 = int(input("insira o primeiro número:"))
numero2 = int(input("insira o segundo número:"))
numero3 = int(input("insira o terceiro número:"))

if numero1 > numero2 and numero1 > numero3 :
    print(f"o número {numero1} é o maior")
    if numero2 > numero3:
        print(f"o número {numero3} é o menor")
    else:
        print(f"o número {numero2} é o menor")
if numero1 < numero2 and numero2 > numero3 :
    print(f"o número {numero2} é o maior")
    if numero1 > numero3:
        print(f"o número {numero3} é o menor")
    else:
        print(f"o número {numero1} é o menor")
if numero1 < numero3 and numero2 < numero3 :
    print(f"o número {numero3} é o maior")
    if numero1 > numero2:
        print(f"o número {numero2} é o menor")
    else:
        print(f"o número {numero1} é o menor")