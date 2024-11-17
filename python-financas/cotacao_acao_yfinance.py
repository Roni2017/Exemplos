import yfinance as yf
# import matplotlib.pyplot as plt

# Criar um objeto Ticker
ticker = yf.Ticker("BBAS3.SA")

# preco atual
print(ticker.info)
preco_atual = ticker.info['currentPrice']
dividendo_atual = ticker.info['dividendRate']
print("Preço atual BBAS3.SA:", preco_atual)
print("Preço atual BBAS3.SA:", dividendo_atual)

dy = (dividendo_atual/preco_atual )*100
print("Dividendo total no último ano (%):", dy)

# Obter dados históricos
# hist = ticker.history(period="1y")

# Visualizar os dados de dividendos
# print(hist['Dividends'])

# Calcular o dividendo total no período
# dividendo_total = hist['Dividends'].sum()
# dividendo_split = hist['Stock Splits'].sum()

# print("Dividendo total no último ano:", dividendo_total)
# print("Dividendo Split total no último ano:", dividendo_split)

# Plotar gráfico de linha dos dividendos
# hist['Dividends'].plot(title='Dividendos - BBAS3.SA')
# plt.xlabel('Data')
# plt.ylabel('Valor do Dividendo')
# plt.show()