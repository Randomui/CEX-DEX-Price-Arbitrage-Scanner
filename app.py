from flask import Flask, jsonify, render_template
from binance_handler import BinanceHandler
from solana_handler import SolanaHandler
from utils import calculate_arbitrage

app = Flask(__name__)

# Initialize handlers with appropriate credentials and URLs
binance = BinanceHandler(api_key="Api-key", api_secret="API-secret")
solana = SolanaHandler(rpc_url="https://api.testnet.solana.com")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/arbitrage', methods=['GET'])
def arbitrage():
    usdc_pairs = binance.fetch_usdc_pairs()
    opportunities = []

    for pair in usdc_pairs:
        binance_bid, binance_ask = binance.fetch_prices(pair)
        solana_price = solana.fetch_token_prices("token-Adress")  # Test token address

        is_profitable, profit = calculate_arbitrage(binance_bid, solana_price, fees={
            'binance': 0.001,
            'solana': 0.003,
            'transaction_cost': 0.0005
        })

        if is_profitable:
            opportunities.append({
                'pair': pair,
                'profit': profit
            })

    return jsonify(opportunities)

if __name__ == '__main__':
    app.run(debug=True)