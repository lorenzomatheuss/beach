# Crypto Trading Bot

An automated cryptocurrency trading bot built in Python that implements a trend-following strategy for trading on the Binance exchange.

## Technologies Used

- **Python 3.11**: Main programming language used.
- **Backtrader**: Framework for backtesting trading strategies.
- **CCXT**: Library for integrating with cryptocurrency exchanges, like Binance.
- **TA-Lib**: Technical analysis and indicators library.
- **Python-dotenv**: For managing environment variables.

## Key Features

- **Automated cryptocurrency trading**: The bot automatically executes buy/sell orders based on predefined strategies.
- **Trend-following strategy**: Implements a trend-following strategy to perform buy/sell operations.
- **Binance Integration**: Connected to Binance using the CCXT library.
- **Backtesting**: Test your strategies using historical market data.
- **Logging**: Logs all buy/sell operations and errors to log files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crypto-bot.git


## Configure your Binance credentials: Create a .env file in the project root directory and add your Binance API credentials:

**API_KEY**=your_api_key_here
**API_SECRET**=your_api_secret_here
**BASE_SYMBOL**=BTC/USDT
**TIMEFRAME**=1h
**QUANTITY**=0.001