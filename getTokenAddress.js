const { TokenListProvider } = require('@solana/spl-token-registry');

async function getTokenAddress(symbol) {
    const tokenListProvider = new TokenListProvider();
    const tokenList = await tokenListProvider.resolve();
    const tokens = tokenList.filterByChainId(101).getList(); // 101 is the chain ID for Solana mainnet

    const token = tokens.find(t => t.symbol === symbol);
    if (token) {
        console.log(token.address);
    } else {
        console.log('Token not found');
    }
}

const symbol = process.argv[2];
getTokenAddress(symbol);