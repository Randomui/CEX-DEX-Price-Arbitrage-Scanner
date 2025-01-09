from solana.rpc.api import Client

class SolanaHandler:
    def __init__(self, rpc_url):
        self.client = Client(rpc_url)

    def fetch_token_prices(self, token_address):
        # Logic to fetch token prices (this could involve Solana-specific methods)
        # For example, you can use a public API or fetch directly from the blockchain
        try:
            response = self.client.get_token_account_balance(token_address)
            return response['result']['value']['uiAmount']
        except Exception as e:
            print(f"Error fetching token price: {e}")
            return None
