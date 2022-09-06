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