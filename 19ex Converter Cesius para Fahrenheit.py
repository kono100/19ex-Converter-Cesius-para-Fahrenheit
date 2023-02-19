
'''  Faça um programa que leia uma temperatura em graus Celsius, calcule e escreva o valor 
correspondente em graus Fahrenheit.'''

temperatura = float(input('Qual a temperatura atual em Celsius? '))
conversao = temperatura * 1.8 + 32
print(f'A temperatura atual em Fahrenheit é de {conversao:.1f} graus')
