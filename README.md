# Trading Bot

## Setup

pip install -r requirements.txt

## Configure

Create .env

BINANCE_API_KEY=
BINANCE_API_SECRET=

## Run Market Order

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

## Run Limit Order

python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 120000