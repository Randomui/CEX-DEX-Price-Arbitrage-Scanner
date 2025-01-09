import ccxt

class BinanceHandler:
    def __init__(self, api_key, api_secret):
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': api_secret,
        })

    def fetch_usdc_pairs(self):
        markets = self.exchange.load_markets()
        return [market for market in markets if market.endswith('/USDC')]

    def fetch_prices(self, symbol):
        ticker = self.exchange.fetch_ticker(symbol)
        return ticker['bid'], ticker['ask']

