import random
import time

#introdução
print("Seja bem vindo ao cálculo de IMC!")
time.sleep (1)
print("Vou precisar de uns dados, por favor me responda...")

#pegando os dados do usuário
try:    
    peso = (float(input("Qual o seu peso atual (em kilogramas)? ")))
except ValueError:
    print("Por favor digite apenas um número válido")

try:
    altura_cm = (int(input("Digite sua altura em centímetros: ")))
except ValueError:
    print("Digite um número válido")
#cálculo dos valores
altura_m = altura_cm / 100
imc = peso / (altura_m*altura_m)
#printando os outputs
print(f"\nO seu IMC é {imc:.2f}. Agora vamos à interpretação deste valor...")
time.sleep (2)
# IMC entre 18,5 e 24,9 = Normal
if 18.5 > imc > 24.9:
    print("\nDe acordo com o parâmetro IMC seu peso está normal!\n")
# IMC entre 25,0 e 29,9 = Sobrepeso
elif 25 > imc > 29.9:
    print("\nDe acordo com o parâmetro IMC você está em sobrepeso.\n")
# IMC entre 30,0 e 39,9 = Obesidade
elif 30 > imc > 39.9:
    print("\nDe acordo com o parâmetro IMC você está obeso.\n")
# IMC maior que 40,0 = Obesidade grave
else:
    print("\nDe acordo com o parâmetro IMC você está gravemente obeso.\n")