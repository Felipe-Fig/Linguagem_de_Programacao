import random
x = str(input("Digite uma palavra "))
y = ''.join(random.sample(x, len(x)))
print(y)