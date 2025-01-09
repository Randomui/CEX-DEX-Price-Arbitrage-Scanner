def calculate_arbitrage(binance_price, solana_price, fees):
    # Example fees: {'binance': 0.001, 'solana': 0.003, 'transaction_cost': 0.0005}
    if binance_price is None:
        print("binance_price is None")
        raise ValueError("binance_price must not be None")
    if solana_price is None:
        print("solana_price is None")
        raise ValueError("solana_price must not be None")

    adjusted_binance_price = binance_price * (1 - fees['binance'])
    adjusted_solana_price = solana_price * (1 - fees['solana']) - fees['transaction_cost']

    profit = adjusted_binance_price - adjusted_solana_price
    return profit > 0, profit