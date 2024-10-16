from web3 import Web3

# Function to create an unsigned Ethereum transaction (Online)


def create_unsigned_transaction(provider_url, from_address, to_address, value_in_eth, gas_price_in_gwei):
    w3 = Web3(Web3.HTTPProvider(provider_url))

    # Prepare the transaction
    transaction = {
        'to': to_address,
        'value': w3.toWei(value_in_eth, 'ether'),         # Value to send
        'gas': 21000,                                     # Standard gas for ETH transfer
        'gasPrice': w3.toWei(gas_price_in_gwei, 'gwei'),  # Gas price
        # Transaction nonce
        'nonce': w3.eth.get_transaction_count(from_address),
        # Mainnet Chain ID (1 for Ethereum Mainnet)
        'chainId': 1
    }

    return transaction

# Function to broadcast a signed transaction (Online)


def broadcast_signed_transaction(provider_url, signed_txn_hex):
    w3 = Web3(Web3.HTTPProvider(provider_url))

    # Broadcast signed transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn_hex)
    return w3.toHex(tx_hash)

# Example usage:


# Create an unsigned transaction
provider_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
from_address = '0xYourAddress'
to_address = '0xRecipientAddress'
value_in_eth = 0.01
gas_price_in_gwei = 50

unsigned_txn = create_unsigned_transaction(
    provider_url, from_address, to_address, value_in_eth, gas_price_in_gwei)
print(f"Unsigned Transaction: {unsigned_txn}")

# Save unsigned transaction to a file (for transfer to offline computer)
with open('unsigned_transaction.txt', 'w') as file:
    file.write(str(unsigned_txn))

# Later, after signing offline, broadcast the signed transaction
# signed_txn_hex = '0xSignedTransactionHexFromOffline'
# tx_hash = broadcast_signed_transaction(provider_url, signed_txn_hex)
# print(f"Broadcasted Transaction Hash: {tx_hash}")
