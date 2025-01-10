from solders.pubkey import Pubkey
from solana.rpc.api import Client

class SolanaHandler:
    def __init__(self, rpc_url):
        self.client = Client(rpc_url)

    def fetch_token_prices(self, token_address):
        """
        Fetch the token price from the Solana blockchain using the token address.
        """
        try:
            # Convert the token address to a Pubkey object
            token_pubkey = Pubkey.from_string(token_address)

            # Fetch the account balance
            response = self.client.get_token_account_balance(token_pubkey)

            # Check if the response contains 'result' and 'value'
            if 'result' in response and 'value' in response['result']:
                # Extract and return the balance in uiAmount
                return response['result']['value']['uiAmount']
            else:
                print(f"Error fetching token price: {response}")
                return None
        except Exception as e:
            print(f"Error fetching token price: {e}")
            return None