'''
CONSISTÊNCIA DE ESTIMADORES
Iremos ilustrar a propriedade de consistência dos estimadores, usando como exemplo a média amostral de uma distribuição normal. 
A consistência indica que, à medida que o tamanho da amostra aumenta, a estimativa do parâmetro populacional (neste caso, a média) tende a se aproximar do valor verdadeiro.

O código começa definindo os parâmetros da distribuição normal.
A distribuição normal é usada para gerar as amostras de dados, onde cada amostra será usada para calcular uma estimativa da média.
São selecionados diferentes tamanhos de amostra. A escolha de tamanhos variados permite observar o comportamento da estimativa da média à medida que mais dados são incluídos.

Para cada tamanho de amostra, o código:
- Gera uma amostra aleatória de uma distribuição normal com média 10 e desvio padrão 2.
- Calcula a média amostral dessa amostra.
O processo é repetido para cada tamanho de amostra especificado.
'''
import numpy as np
import matplotlib.pyplot as plt

# Definir a semente para reprodutibilidade
np.random.seed(42)

# Parâmetros da distribuição normal
media = 10
desvio_padrao = np.sqrt(4)

# Definir os tamanhos das amostras
tamanhos_amostra = [2, 5, 10, 15, 20, 1000, 1010, 1020, 5000]

# Função para calcular a média amostral
def calcular_estimativa(n):
    amostra = np.random.normal(loc=media, scale=desvio_padrao, size=n)
    return np.mean(amostra)

# Calcular as estimativas para cada tamanho de amostra
estimativas = [calcular_estimativa(n) for n in tamanhos_amostra]

# Plotar os resultados
plt.plot(tamanhos_amostra, estimativas, marker='o', linestyle='-', color='b', label='Estimativas')
plt.axhline(y=media, color='r', linestyle='--', label='Média verdadeira')
plt.title('Estimativas da Média em Função do Tamanho da Amostra')
plt.xlabel('Tamanho da Amostra')
plt.ylabel('Estimativa da Média')
plt.legend()
plt.grid(True)
plt.show()

5. Conclusão: Ilustração da consistência
O gráfico gerado pelo código demonstra que, para amostras pequenas, a estimativa da média pode variar bastante em relação ao valor verdadeiro. No entanto, à medida que o tamanho da amostra aumenta, a estimativa da média se estabiliza e converge para o valor real da média (10), ilustrando a consistência do estimador da média amostral.

Esse comportamento reforça uma das principais características dos estimadores consistentes: quando o tamanho da amostra cresce indefinidamente, a estimativa se aproxima do parâmetro populacional que ela pretende estimar.
