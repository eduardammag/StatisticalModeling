# Enunciado:
# 
# Dado o vetor de observações X = [12, 15, 9, 10, 17, 12, 11, 18, 15, 13], assumimos que os dados seguem uma distribuição normal 
# N(μ, σ^2), onde tanto a média μ quanto a variância σ^2 são desconhecidas. O objetivo é calcular e plotar a função de log-verossimilhança
# l(μ, σ^2) para diferentes valores de μ e σ^2, e encontrar os valores que maximizam a log-verossimilhança.
# 
# Explicação:
# 
# Neste caso, a função de log-verossimilhança inclui tanto μ quanto σ^2 como parâmetros a serem estimados. A função de densidade da 
# normal agora depende de ambos, e a fórmula da log-verossimilhança reflete essa dependência. Ao calcular l(μ, σ^2) para uma gama de 
# valores de μ e σ^2, podemos identificar os valores que maximizam a log-verossimilhança e, portanto, são os estimadores de máxima 
# verossimilhança (MLE) de μ e σ^2.

import numpy as np
import matplotlib.pyplot as plt

# Definindo os dados fornecidos
x = np.array([12, 15, 9, 10, 17, 12, 11, 18, 15, 13])

# Função para a log-verossimilhança com variância desconhecida
def log_likelihood(mu, sigma2, x):
    n = len(x)
    return -n/2 * np.log(2 * np.pi * sigma2) - (1/(2 * sigma2)) * np.sum((x - mu) ** 2)

# Criando intervalos de valores para mu e sigma^2
mu_values = np.linspace(5, 20, 100)
sigma2_values = np.linspace(1, 10, 100)

# Calculando os valores de log-verossimilhança para cada par (mu, sigma^2)
log_likelihood_values = np.zeros((len(mu_values), len(sigma2_values)))

for i, mu in enumerate(mu_values):
    for j, sigma2 in enumerate(sigma2_values):
        log_likelihood_values[i, j] = log_likelihood(mu, sigma2, x)

# Plotando o gráfico de contorno da log-verossimilhança
X, Y = np.meshgrid(mu_values, sigma2_values)
plt.contour(X, Y, log_likelihood_values.T, levels=20)
plt.title('Log-Verossimilhança vs $\mu$ e $\sigma^2$')
plt.xlabel('$\mu$')
plt.ylabel('$\sigma^2$')
plt.colorbar(label='Log-Verossimilhança')
plt.show()
