from mnemonic import Mnemonic
from eth_account import Account
import json

# Function to generate a new seed phrase (BIP-39) offline
Account.enable_unaudited_hdwallet_features()


def generate_seed():
    mnemo = Mnemonic("english")
    # 12-word seed phrase (can also use 256-bit for 24 words)
    seed_phrase = mnemo.generate(strength=128)
    return seed_phrase

# Function to derive private key from seed phrase (BIP-44 Ethereum path)


def derive_private_key(seed_phrase, index=0):
    # Derive the private key for the first account using Ethereum's BIP-44 path
    bip32_root_key = Account.from_mnemonic(seed_phrase)
    return bip32_root_key.privateKey.hex()

# Function to sign the transaction offline using the derived private key


def sign_transaction_offline(unsigned_txn_str, private_key):
    # Load the unsigned transaction string into a Python dict
    unsigned_txn = json.loads(unsigned_txn_str.replace(
        "'", '"'))  # Convert string to dict

    # Sign the transaction using the private key
    signed_txn = Account.sign_transaction(unsigned_txn, private_key)

    # Return signed transaction in hex format
    return signed_txn.rawTransaction.hex()


if __name__ == "__main__":
    # Example usage:
    # 1. Generate a seed phrase (do this offline)
    seed_phrase = generate_seed()
    print(f"Generated Seed Phrase: {seed_phrase}")

    # 2. Derive private key from seed phrase
    private_key = derive_private_key(seed_phrase)
    print(f"Derived Private Key: {private_key}")

    # 3. Load unsigned transaction (from a file or input)
    with open('unsigned_transaction.txt', 'r') as file:
        unsigned_txn_str = file.read()

    # 4. Sign the transaction offline
    signed_txn = sign_transaction_offline(unsigned_txn_str, private_key)
    print(f"Signed Transaction (Hex): {signed_txn}")

    # 5. Save signed transaction to a file for transfer back to online computer
    with open('signed_transaction.txt', 'w') as file:
        file.write(signed_txn)
