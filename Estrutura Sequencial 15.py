print ('Estrutura Sequencial 15')
print ('Seja bem-vindo!')
salario_hora = float (input ('Digite quanto você ganha por hora'))
horas = float (input ('Digite quantas horas você trabalha no mês'))

salario = salario_hora * horas
desconto = salario * (0.11)
inss = salario * (0.08)
sindicato = salario * (0.05)
liquido = salario - desconto - inss - sindicato

print ('Salario bruto R$' , salario)
print ('IR (11%) R$', desconto)
print ('INSS (8%) R$', inss)
print ('Sindicato (5%) R$', sindicato)
print ('Salário Líquido R$', liquido)
