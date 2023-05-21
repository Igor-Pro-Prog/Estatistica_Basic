import math
from statistics import mean

def calcular_media(amostra):
    soma = sum(amostra)
    media = soma / len(amostra)
    return media

def calcular_variancia(amostra):
    media = calcular_media(amostra)
    soma_diferencas_quadrado = sum((x - media) ** 2 for x in amostra)
    variancia = soma_diferencas_quadrado / len(amostra)
    return variancia

def calcular_desvio_padrao(amostra):
    variancia = calcular_variancia(amostra)
    desvio_padrao = math.sqrt(variancia)
    return desvio_padrao

def calcular_estatisticas(amostra):
    media = calcular_media(amostra)
    variancia = calcular_variancia(amostra)
    desvio_padrao = calcular_desvio_padrao(amostra)
    return media, variancia, desvio_padrao

def calcular_regressao_linear(x, y):
    n = len(x)
    soma_x = sum(x)
    soma_y = sum(y)
    soma_xy = sum(x[i] * y[i] for i in range(n))
    soma_x2 = sum(x[i] ** 2 for i in range(n))

    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)
    b = (soma_y - a * soma_x) / n

    return a, b

# Exemplo de uso
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

media_x, variancia_x, desvio_padrao_x = calcular_estatisticas(x)
media_y, variancia_y, desvio_padrao_y = calcular_estatisticas(y)

a, b = calcular_regressao_linear(x, y)

print("Amostra X:", x)
print("Média X:", media_x)
print("Variância X:", variancia_x)
print("Desvio Padrão X:", desvio_padrao_x)

print("\nAmostra Y:", y)
print("Média Y:", media_y)
print("Variância Y:", variancia_y)
print("Desvio Padrão Y:", desvio_padrao_y)

print("\nRegressão Linear:")
print("Coeficiente angular (a):", a)
print("Coeficiente linear (b):", b)
