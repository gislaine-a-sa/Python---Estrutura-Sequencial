print ('Estrutura Sequencial 17')
import sys

area = float ( input ('Digite a área que deseja pintar em m2'))
lata_grande = 18 # Litros
lata_pequena = 3.6 # Litros
preço_lata_grande = 80 #Reais
preço_lata_pequena = 25 # Reais
area_litro_tinta = 6 #Metros.sq por litro

tinta_necessaria = float (area) / (area_litro_tinta # Litros de tinta necessarios para a pintura

if tinta_necessaria ==1:                                   
print ('Vai precisar de um litro de tinta')
elif (tinta_necessaria ! == 1) and (tinta_necessaria > 0) :
    print ('Vai precisar de', tinta_necessaria,'litros de tinta')7else:
        print ('Dados errados')
        sys.exit ()
