print ('Estrutura Sequencial 14')

peso = int(input("Entre com o peso: "))

if peso > 50:
	excesso = peso - 50
	multa   = excesso * 4
else:
	excesso = "ZERO"
	multa = "ZERO"

print ('O excesso de peso foi de ',str(excesso),'kg, portanto, a multa é de R$', str(multa) )   
