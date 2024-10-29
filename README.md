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

## Project Structure

crypto-bot/
│
├── config/
├── data/
│   └── logs/
├── strategies/
│   └── trend_following.py  # Trading strategy logic
├── utils/
│   └── helpers.py          # Helper functions
├── .env                    # Environment variables file
├── .gitignore               # Gitignore file for sensitive files
├── README.md                # Project documentation
├── main.py                  # Main file to run the bot
├── backtest.py              # Script for running backtests
├── requirements.txt         # Project dependencies
└── venv/                    # Virtual environment

## License
This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** License. You can view the full license [here](https://creativecommons.org/licenses/by-nc/4.0/).

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
