import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor

# Verificar a estrutura dos dados
print(daily_dataframe.head())
print(daily_dataframe.dtypes)

# Converter timestamp para features numéricos
daily_dataframe['year'] = daily_dataframe['date'].dt.year
daily_dataframe['month'] = daily_dataframe['date'].dt.month
daily_dataframe['day'] = daily_dataframe['date'].dt.day
daily_dataframe['dayofweek'] = daily_dataframe['date'].dt.dayofweek

# Manter a coluna do tempo para a plotagem e ordenar cronologicamente
daily_dataframe.set_index('date', inplace=True)
daily_dataframe = daily_dataframe.sort_index()

# so comentar cada um desses para diminuir os parâmetros
#daily_dataframe = daily_dataframe.drop("wind_speed_10m_max", axis=1)
#daily_dataframe = daily_dataframe.drop("rain_sum", axis=1)
#daily_dataframe = daily_dataframe.drop("temperature_2m_min", axis=1)

# Separar a variável alvo (temperature_2m_max) das features/'regressores exógenos'
X = daily_dataframe.drop('temperature_2m_max', axis=1)
y = daily_dataframe['temperature_2m_max']

# Configurar a validação cruzada K-Fold
kf = KFold(n_splits=5)

# Variáveis para armazenar os resultados
predictions = np.zeros(len(y))
rmse_list = []

# Executar o K-Fold
for train_index, test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    # Ajustar o modelo GradientBoostingRegressor
    model = GradientBoostingRegressor()
    model.fit(X_train, y_train)

    # Fazer previsões
    y_pred = model.predict(X_test)
    predictions[test_index] = y_pred

    # Calcular o RMSE
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    rmse_list.append(rmse)

# Avaliar o modelo com a média do k-fold
mean_rmse = np.mean(rmse_list)
print(f'Mean RMSE: {mean_rmse}')

# Plots
plt.figure(figsize=(14, 7))

# Plotar dados reais
plt.plot(daily_dataframe.index, y, label='Treino')

# plot das predições
plt.plot(daily_dataframe.index, predictions, label='Predição GradientBoostingRegressor', color='red')

# Plotar banda de erro
upper_bound = predictions + mean_rmse
lower_bound = predictions - mean_rmse
plt.fill_between(daily_dataframe.index, lower_bound, upper_bound, color='pink', alpha=0.3, label='Banda de Erro')

# detalhes do gráfico
plt.xlabel('Data')
plt.ylabel('Temperatura')
plt.title('Comparação entre Temperatura Real e Previsão GradientBoostingRegressor')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
