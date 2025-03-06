'''
Enunciado:

Dado o vetor de observações \( X = [12, 15, 9, 10, 17, 12, 11, 18, 15, 13] \), assumimos que os dados seguem uma distribuição normal \( N(\mu, 4) \), onde a média \( \mu \) é desconhecida e a variância é conhecida e igual a 4. O objetivo é calcular e plotar a função de log-verossimilhança \( l(\mu) \) em função de diferentes valores de \( \mu \) e encontrar o valor de \( \mu \) que maximiza a log-verossimilhança.

Explicação:

A função de log-verossimilhança \( l(\mu) \) é derivada da função de verossimilhança de uma normal com variância conhecida. Neste caso, o cálculo leva em consideração as observações \( X \), e é uma função de \( \mu \) que nos diz o quão bem os diferentes valores de \( \mu \) explicam os dados observados. Ao calcular a log-verossimilhança para uma gama de valores de \( \mu \) entre 5 e 20, podemos visualizar como ela varia e identificar o valor que a maximiza, o que corresponderia ao estimador de máxima verossimilhança (MLE).
'''

import numpy as np
import matplotlib.pyplot as plt

# Definindo os dados fornecidos
x = np.array([12, 15, 9, 10, 17, 12, 11, 18, 15, 13])

# Função para a log-verossimilhança
def log_likelihood(mu, x):
    n = len(x)
    sigma2 = 4  # variância conhecida (4)
    return -5 * np.log(8 * np.pi * sigma2) - (1/(2 * sigma2)) * (np.sum(x**2) - 2 * mu * np.sum(x) + n * mu**2)

# Criando um intervalo de valores para mu
mu_values = np.linspace(5, 20, 1000)

# Calculando os valores de log-verossimilhança
log_likelihood_values = [log_likelihood(mu, x) for mu in mu_values]

# Plotando o gráfico
plt.plot(mu_values, log_likelihood_values, label='Log-Verossimilhança')
plt.title('Log-Verossimilhança vs $\mu$')
plt.xlabel('$\mu$')
plt.ylabel('Log-Verossimilhança')
plt.grid(True)
plt.legend()
plt.show()
