print ('Estrutua Sequencia 18')
tamanho = float (input ('Digite o tamanho do arquivo em MB'))
velocidade = float ( input('Digite a velocidade d eum link de internet em Mbps'))

print ('O tempo aproximado de download: %.2f Minutos' %(( tamanho / velocidade )* 60 ))
