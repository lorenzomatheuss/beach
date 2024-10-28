import ccxt
import pandas as pd
import backtrader as bt
from datetime import datetime

# Inicializar o objeto exchange fora da função
exchange = ccxt.binance()

# Função para obter dados históricos da Binance usando CCXT
def get_binance_data(symbol, timeframe, since):
    """
    Função para buscar dados históricos da Binance.
    """
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=since)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('datetime', inplace=True)
    return df

# Exemplo de estratégia simples para testar
class TestStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        print(f'Preço de fechamento: {self.dataclose[0]}')  # Printar preço de fechamento a cada candle

# Obter dados de BTC/USDT (como exemplo)
data_df = get_binance_data('BTC/USDT', '1d', exchange.parse8601('2020-01-01T00:00:00Z'))

# Verificar os primeiros dados para garantir que foram carregados corretamente
print(data_df.head())  # Mostra as primeiras linhas dos dados baixados

# Converter para o formato de feed do Backtrader
data_feed = bt.feeds.PandasData(dataname=data_df)

# Inicializar o Backtrader com os dados
cerebro = bt.Cerebro()
cerebro.adddata(data_feed)

# Adicionar estratégia
cerebro.addstrategy(TestStrategy)

# Configurar estratégia e iniciar o backtest
print("Iniciando backtest...")
cerebro.run()
print("Backtest finalizado.")
