# Calculo de Desconto com Porcentagem e Valor Definido Pelo User (.py)
print('-_' * 15)
print('Calculo de Descontos')
print('-_' * 15)

valor = float(input('Digite o valor do produto: R$'))
desconto = float(input('Digite o valor do desconto: %'))
desconto1 = desconto / 100
var = valor * desconto1
resultado = valor - var
print('O valor após o desconto será R${}!'.format(resultado))
