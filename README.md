# CEX-DEX-Price-Arbitrage-Scanner
# Arbitrage Opportunity Checker


This project is a Flask web application that checks for arbitrage opportunities between Binance and Solana. It provides an endpoint to fetch profitable arbitrage opportunities.

## Features

- Fetches USDC trading pairs from Binance.
- Fetches token prices from Solana.
- Calculates arbitrage opportunities considering fees.
- Returns profitable arbitrage opportunities as a JSON response.

## Requirements

- Python 3.7+
- Flask
- Requests (or any other HTTP library you are using)

## Installation

1. Clone the repository:

   git clone https://github.com/Randomui/CEX-DEX-Price-Arbitrage-Scanner.git
   cd arbitrage-opportunity-checker

2. Create a virtual environment and activate it:

   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux

3. Install the required packages:

   pip install -r requirements.txt

## Configuration

Update the API credentials and RPC URL in the `app.py` file:

binance = BinanceHandler(api_key="Your-Binance-Api-Key", api_secret="Your-Binance-Api-Secret")
solana = SolanaHandler(rpc_url="https://api.mainnet-beta.solana.com")

## Usage

1. Run the Flask application:

   python app.py

2. Access the arbitrage endpoint:

   Open your web browser and go to `http://127.0.0.1:5000/arbitrage` to see the list of profitable arbitrage opportunities.

## Example Response

[
  {
    "pair": "BTC/USDC",
    "binance_bid": 45000,
    "solana_price": 45500,
    "profit": 200
  },
  {
    "pair": "ETH/USDC",
    "binance_bid": 3000,
    "solana_price": 3100,
    "profit": 50
  }
]

