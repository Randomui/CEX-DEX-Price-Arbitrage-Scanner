import subprocess
import logging
from flask import Flask, jsonify, render_template
from binance_handler import BinanceHandler
from solana_handler import SolanaHandler
from utils import calculate_arbitrage

app = Flask(__name__)

# Initialize handlers with appropriate credentials and URLs
binance = BinanceHandler(api_key="API-key", api_secret="Secret")
solana = SolanaHandler(rpc_url="https://api.mainnet-beta.solana.com")

# Configure logging to log only required details
logging.basicConfig(level=logging.INFO, format='%(message)s')

def get_token_address(symbol):
    """
    Get the Solana token address for the given symbol using a Node.js script.
    """
    try:
        result = subprocess.run(['node', 'getTokenAddress.js', symbol], capture_output=True, text=True, check=True)
        token_address = result.stdout.strip()
        logging.info(f"Resolved Solana token address for {symbol}: {token_address}")
        return token_address
    except subprocess.CalledProcessError as e:
        logging.error(f"Error fetching token address for {symbol}: {e.stderr.strip()}")
        return None

@app.route('/')
def index():
    """
    Render the home page with the bar chart.
    """
    return render_template('index.html')

@app.route('/arbitrage', methods=['GET'])
def arbitrage():
    """
    Check for arbitrage opportunities between Binance and Solana for SOL/USDC.
    """
    symbol = "SOL"
    pair = f"{symbol}/USDC"
    opportunities = []

    try:
        # Fetch Binance prices
        binance_bid, binance_ask = binance.fetch_prices(pair)

        # Resolve Solana token address
        solana_token_address = get_token_address(symbol)
        if not solana_token_address:
            logging.error(f"Could not resolve token address for {symbol}.")
            return jsonify({"error": f"Token address for {symbol} not found."}), 400

        # Log only the Solana token address
        logging.info(f"Using Solana token address: {solana_token_address}")

        # Fetch Solana price
        solana_price = solana.fetch_token_prices(solana_token_address)
        if solana_price is None:
            logging.error(f"Failed to fetch Solana price for token address: {solana_token_address}")
            return jsonify({"error": f"Failed to fetch Solana price for {symbol}."}), 400

        # Calculate arbitrage
        is_profitable, profit = calculate_arbitrage(binance_bid, solana_price, fees={
            'binance': 0.001,
            'solana': 0.003,
            'transaction_cost': 0.0005
        })

        # Calculate price difference
        price_difference = abs(binance_bid - solana_price)
        opportunities.append({
            'symbol': symbol,
            'binance_bid': binance_bid,
            'solana_price': solana_price,
            'price_difference': price_difference,
            'profit': profit,
            'is_profitable': is_profitable
        })

    except Exception as e:
        logging.error(f"Error processing {pair}: {e}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

    return jsonify(opportunities)

if __name__ == '__main__':
    app.run(debug=True)
