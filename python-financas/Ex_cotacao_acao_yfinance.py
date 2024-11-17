import yfinance as yf

#Docs: https://pypi.org/project/yfinance/

##Analise da Tesla


#One Ticker
msft = yf.Ticker("MSFT")

type(msft) #Ticker object com multiplos atributos

# get stock info
msft.info
print(msft.info)

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
msft.actions

# show dividends
msft.dividends
print(msft.dividends)

# show splits
msft.splits

# show financials
#msft.financials
#msft.quarterly_financials

# show major holders
#msft.major_holders

# show institutional holders
msft.institutional_holders

# show balance sheet
#msft.balance_sheet
#msft.quarterly_balance_sheet

# show cashflow
#msft.cashflow
#msft.quarterly_cashflow

# show earnings
#msft.earnings
#msft.quarterly_earnings

# show sustainability
msft.sustainability

# show analysts recommendations - o que são estas recomendações?!?!?
msft.recommendations

# show next event (earnings, etc)
#msft.calendar

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
#msft.isin

# show options expirations
#msft.options

# get option chain for specific expiration
#opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts
     
start = '2019-01-01'
end = '2020-12-31'

#Metodo 2 (Mais Eficiente)
tickers = ' '.join(df['Symbol'].to_list())
data = yf.download(tickers,start,end,group_by='ticker')
#data['Adj Close'].reset_index().columns
data['ABT'].head()
##data.columns