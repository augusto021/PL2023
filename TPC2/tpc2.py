import sys


"""
TPC2: Somador on/off

Crie um programa em Python que tenha o seguinte comportamento:

  * Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
  * Prepare o programa para ler o texto do canal de entrada: stdin;
  * Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
  * Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
  * Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.
"""


on = 1
total = 0
in_number = 0
number = ""
word = ""
for line in sys.stdin:
    for c in line.lower():

        if c.isnumeric():
            number = number + c
            word = ""

        elif c == '=':
            if on and number != '':
                total = total + int(number)
            print(total)
            number = ""

        elif c.isalpha():
            if on and number != "":
                total = total + int(number)

            if c == 'o' or c =='n' or c == 'f':
                word = word + c
                if word == "on":
                    on = 1
                    word = ""
                elif word == "off":
                    on = 0
                    word = ""
            else:
                word = ""
            number = ""