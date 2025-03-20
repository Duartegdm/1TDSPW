#Algotitmo: Conversao_Reais_dDolares
'''Este programa foi desenvolvido para...
...'''

reais = 0
cotacao_dolar = 0
conversao = 0

print('Bem vindos ao Programa para converter reais em dolares!!!\n')
reais = float(input("Digite o valor que você quer converter (Em reais): "))
cotacao_dolar = float(input("Digite o valor da cotação do dólar hoje: \n"))

conversao = reais/cotacao_dolar

print("Com esta quantia é possível comprar? ")
print(round(conversao,2))
print(' dolares')

print('Obrigado por usar nosso programa!!')
