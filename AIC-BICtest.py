import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Gerar dados sintéticos
np.random.seed(42)
n = 100  # Tamanho da amostra
X1 = np.random.rand(n) * 10  # Variável independente 1
X2 = np.random.rand(n) * 5   # Variável independente 2
X3 = np.random.rand(n) * 3   # Variável independente 3

# Criar variável dependente com ruído
Y = 5 + 2*X1 - 3*X2 + np.random.randn(n) * 2

# Criar DataFrame
df = pd.DataFrame({'Y': Y, 'X1': X1, 'X2': X2, 'X3': X3})

# Definir função para calcular AIC e BIC
def evaluate_model(formula, data):
    model = sm.OLS.from_formula(formula, data).fit()
    return model.aic, model.bic

# Modelos a serem comparados
models = {
    "Modelo 1 (X1 e X2)": "Y ~ X1 + X2",
    "Modelo 2 (X1, X2 e X3)": "Y ~ X1 + X2 + X3",
    "Modelo 3 (Somente X1)": "Y ~ X1"
}

# Calcular AIC e BIC para cada modelo
results = {name: evaluate_model(formula, df) for name, formula in models.items()}

# Criar DataFrame com os resultados
results_df = pd.DataFrame(results, index=["AIC", "BIC"]).T
print(results_df)
