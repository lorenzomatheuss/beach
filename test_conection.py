import ccxt

# Testar conexão com a Binance
exchange = ccxt.binance({
    'enableRateLimit': True
})

try:
    # Tentando pegar dados de mercado para BTC/USDT
    ohlcv = exchange.fetch_ohlcv('BTC/USDT', timeframe='1h', limit=100)
    print("Dados recebidos com sucesso:", ohlcv[:5])  # Mostra os 5 primeiros resultados
except Exception as e:
    print(f"Erro ao conectar na API: {str(e)}")
