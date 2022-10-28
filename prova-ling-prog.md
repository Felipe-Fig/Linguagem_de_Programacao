# Prova Linguagem de Programação 

## Corrigido pelo AVA

### Não sou o criador de nenhuma destas questões, apenas disponibilizo para fins de estudo. Caso haja algum problem é só mandar via *issue*.

---

### **Questão 1**

Analise o trecho de código em Python abaixo:

```Python
def checa_valor(list):
    elem = list[0]
    for a in list:
        if a > elem:
            elem = a
    return elem
print(checa_valor([4, 10, 18, -7]))
```
Assinale a alternativa correta que apresenta o que será impresso para o usuário:

**Gabarito: 18**

---

### **Questão 2**

Qual é a biblioteca utilizada em Python para realizar a análise de dados? Assinale a alternativa correta.

**Gabarito: Pandas**

---

### **Questão 3**

Python é uma linguagem que permite desenvolver programas utilizando o paradigma de Orientação a objetos. Em OO nós conhecemos os conceitos que nos permite implementar encapsulamento, herança e polimorfismo por exemplo. Dentro da orientação a objetos, existe outros conceitos importantes, totalmente alinhados a esse paradigma. Um deles, é considerado uma forma de organizar dados e seus comportamentos. Desse modo, aponte a alternativa que apresenta a opção correta para a definição mencionada acima:

**Gabarito: classe**

---

### **Questão 4**

Relacione as bibliotecas de Python a seguir com a sua respectiva descrição:

I- Pandas<br>
II- Pillow;<br>
III- Matplotlib;<br>

1- Utilizada para a análise de dados;<br>
2- Esta biblioteca é utilizada para a manipulação de Imagens;<br>
3- Com esta biblioteca é possível realizar plotagem de gráficos diversos.<br>

A seguir, assinale a alternativa que contém a sequência correta da associação:

**Gabarito: I - 1; II - 2; III - 3;**

---

### **Questão 5**

Analise o trecho de código a seguir:
```Python
def fib(n):
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado
```

Agora, analise as afirmativas sobre o código anterior:

I- O resultado que será impresso é: `[1, 1, 2, 3]`;

II- a variável resultado é uma lista e armazena os valores de acordo com as interações do `while`;

III- O comando `resultado.append(b)` adiciona o valor no final da lista denominada resultado.

Agora, assinale a alternativa que apresenta a resposta CORRETA:

**Gabarito: As afirmativas I, II e III estão corretas.**

---

### **Questão 6**

Existem várias ferramentas que facilitam a vida de um programador que escolhe trabalhar com python. Um dos projetos, ____________, apresenta uma série de facilidades que são indispensáveis para reduzir custos na hora de programar. Por exemplo, a ferramenta acima mencionada, é a união de várias ferramentas Python que são repletas de bibliotecas e IDEs.

**Gabarito: Anaconda**

---

### **Questão 7**

Sobre as características da linguagem Python, analise as afirmativas a seguir:

I- Na linguagem Python, o tipo de variável é identificado no momento que se atribui um valor a ela. Portanto, uma variável refere-se a um valor.

II- Em Python não há a necessidade de definir estaticamente o tipo de variável, como em outras linguagens de programação.

III- O modelo de dados do Python adota como paradigma que todo dado em um programa escrito com Python é representado por um objeto.

Agora, assinale a alternativa que apresenta a resposta CORRETA:

**Gabarito: As afirmativas I, II e III estão corretas.**

---

### **Questão 8**

Sobre a modularidade em Python, analise as afirmativas a seguir:

I- A modularidade é importante, pois há a necessidade de objetos, comandos e ferramentas específicas;

II- Um módulo pode conter tanto instruções executáveis quanto definições de funções e classes;

III- Com a modularidade é possível de se realizar o reuso de código.

Agora, assinale a alternativa que apresenta a resposta CORRETA:

**Gabarito: As afirmativas I, II e III estão corretas.**

---

### **Questão 9**

Sobre o escopo de funções, analise as asserções a seguir:

I- Durante a execução de um programa, todos os objetos criados fora de qualquer função são denominadas globais e todos os objetos criados dentro de uma função são denominadas locais. Os objetos locais existem apenas enquanto a função está em execução.

Portanto,

II- os valores de retorno da função também deixam de existir, porém, antes de serem descartados são atribuídos aos objetos que os recebem na chamada da função.

Analisando-se as asserções apresentadas, conclui-se que:

**Gabarito: As duas afirmações são verdadeiras, e a segunda justifica a primeira.**

---

### **Questão 10**

O algoritmo de ordenação tem o objetivo de produzir uma nova sequência em que os elementos aparecem em ordem crescente ou descrescente. Analise as afirmativas a seguir sobre a ordenação:

I- O bubble sorte é um algoritmo de ordenação que que utiliza o método de divisão e conquista para criar a nova sequência de elementos;

II- O quick sort percorrer o vetor várias vezes, a cada passagem fazer a troca para o topo o maior/menor elemento da sequência.

III- O selection sort seleciona em cada iteração um elemento para ser inserido na sequência ordenada produzida.

Agora, assinale a alternativa que apresenta a resposta CORRETA:

**Gabarito: Apenas a afirmativa III está correta;**

---

### **Questão 11**

Analise o trecho de código a seguir:
```Python
for i in range(6, 0, -1):
    print(i)
```
Assinale a alternativa que apresenta a resposta correta sobre o trecho de código anterior:

**Gabarito: Neste caso, será apresentado a seguinte sequência para o usuário: 6, 5, 4, 3, 2, 1**

---

### **Questão 12**

Sobre as funções nativas do Python, analise as afirmativas a seguir e marque V para verdadeiro e F para falso:

( ) A função `print()` é utilizada para imprimir os argumentos passados;

( ) A função `input()` é utilizada para a entrada de dados;

( ) A função `type()` mostra o tipo de dados;

Agora, assinale a alternativa que apresenta a sequência CORRETA:

**Gabarito: V-V-V**

---

### **Questão 13**

Sobre a linguagem Python, analise as asserções a seguir:

I- Todo objeto em Python possui um identificador (o nome), um tipo e o conteúdo.

Portanto,

II- diferentes tipos de objetos vão suportar diferentes operações. Cada uma destas deve ser escolhida de acordo com o problema a ser resolvido.

Analisando-se as asserções apresentadas, conclui-se que:

**Gabarito: As duas afirmações são verdadeiras, e a segunda justifica a primeira.**

---

### **Questão 14**

Relacione as funções built-in com suas respectivas descrições:

I- `enumerate()`;

II- `input()`;

III- `range()`;

1- entrada de dados;

2- usada para retornar à posição de um valor em uma sequência;

3- retorna uma série numérica no intervalo enviado como argumento.

A seguir, assinale a alternativa que contém a sequência correta da associação:

**Gabarito: I-2; II-1; III-3**

---

### **Questão 15**

Sobre o escopo de funções, analise as asserções a seguir:

I- Durante a execução de um programa, todos os objetos criados fora de qualquer função são denominadas globais e todos os objetos criados dentro de uma função são denominadas locais.

Portanto,

II- os objetos locais existem apenas enquanto a função está em execução. Quando uma função é chamada, seus objetos internos são criados, passam a existir, ocupando parte da memória do computador, e podem ser utilizados plenamente. Quando a função termina, esses objetos são removidos da memória, deixam de existir e os dados que continham são descartados.

Analisando-se as asserções apresentadas, conclui-se que:

**Gabarito: As duas afirmações são verdadeiras, e a segunda justifica a primeira.**

---

### **Questão 16**

Analise o trecho de código a seguir:

```Python
class Conta:
    def __init__(self, nome, numero):
        self.cliente = nome
        self.num = numero
        self.saldo = 0.0
    
    def Saldo(self):
        return self.saldo
    
    def getClient(self):
        return self.cliente
    
    def Depositar(self, valor):
        self.saldo += valor
```
Agora, analise as afirmativas relacionadas ao trecho de código:

I- O construtor é um método reservado chamado `_init_` ;

II- parâmetro `self` é obrigatório e os demais são definidos pelo programador;

III- Na função `_init_` as variáveis são inicializadas.

Agora, assinale a alternativa que apresenta a resposta CORRETA:

**Gabarito: As afirmativas I, II e III estão corretas.**