from matplotlib import pyplot as plt
import random
dados1 = random.sample(range(100), k=10)
dados2 = random.sample(range(100), k=10)
x = plt.plot(dados1, dados2)
# pyplot gerencia a figura e o eixo
fig, x = plt.subplots(2)
plt.show() #p/ mostrar gráfico no VS Code
