# Faça um programa que receba uma hora formada por hora e minutos (um número real), calcule e mostre a hora digitada apenas em minutos. Lembre-se de que:
# * para quatro e meia, deve-se digitar 4.30;
# * os minutos vão de 0 a 59.
#       LEIA hora
#       h = pegar a parte inteira da variável hora
#       minutos = hora − h
#       conversao = (h * 60) + (minutos * 100)
#       ESCREVA conversao

hora = float(input("Insira o horário (horas.minutos): "))
h = int(input("Insira apenas a hora: "))

minutos = hora - h
conversao = (h * 60) + (minutos * 100)

print(conversao)