import ccxt
import time
import pandas as pd
from dotenv import load_dotenv
import os
from strategies.trend_following import trend_following_strategy
from utils.helpers import log_to_file

# Carregar variáveis do arquivo .env
load_dotenv()

# Obter as configurações do .env
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
BASE_SYMBOL = os.getenv('BASE_SYMBOL')
TIMEFRAME = os.getenv('TIMEFRAME')
QUANTITY = float(os.getenv('QUANTITY'))

# Conectar à Binance
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True
})

def get_ohlcv(symbol, timeframe='1h', limit=100):
    """
    Função para buscar dados de mercado (OHLCV) da Binance.
    """
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# Função para executar uma ordem de compra
def buy_order(symbol, quantity):
    try:
        order = exchange.create_market_buy_order(symbol, quantity)
        log_to_file(f"Ordem de COMPRA executada: {order}")
    except Exception as e:
        log_to_file(f"Erro ao executar ordem de COMPRA: {str(e)}")

# Função para executar uma ordem de venda
def sell_order(symbol, quantity):
    try:
        order = exchange.create_market_sell_order(symbol, quantity)
        log_to_file(f"Ordem de VENDA executada: {order}")
    except Exception as e:
        log_to_file(f"Erro ao executar ordem de VENDA: {str(e)}")

def main():
    """
    Função principal que executa o bot.
    """
    try:
        while True:
            # Obter dados de mercado
            df = get_ohlcv(BASE_SYMBOL, TIMEFRAME)
            # Aplicar a estratégia de "Trend Following"
            df = trend_following_strategy(df)

            # Verificar sinais de compra/venda
            if df['buy_signal'].iloc[-1]:
                log_to_file("Sinal de COMPRA detectado!")
                buy_order(BASE_SYMBOL, QUANTITY)  # Chama a função de compra

            elif df['sell_signal'].iloc[-1]:
                log_to_file("Sinal de VENDA detectado!")
                sell_order(BASE_SYMBOL, QUANTITY)  # Chama a função de venda

            time.sleep(60)  # Esperar 60 segundos antes de buscar novos dados

    except KeyboardInterrupt:
        # Captura o encerramento manual do bot (Ctrl+C)
        log_to_file("Bot interrompido manualmente.")
        print(" Bot interrompido pelo usuário.")

    except Exception as e:
        log_to_file(f"Erro: {str(e)}")
        time.sleep(60)

if __name__ == "__main__":
    main()
