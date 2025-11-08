
import os
from mnemonic import Mnemonic
from eth_account import Account
from web3 import Web3
import requests
Account.enable_unaudited_hdwallet_features()


def generate_seed_phrase():
    """Generate a random 12-word BIP-39 seed phrase."""
    mnemo = Mnemonic("english")
    return mnemo.generate(strength=128)  # 128 bits for 12 words


def derive_eth_address(seed_phrase):
    """Derive Ethereum private key and address from seed phrase using BIP-44."""
    try:
        # Derive account using BIP-44 path: m/44'/60'/0'/0/0 (Ethereum standard)
        account = Account.from_mnemonic(
            seed_phrase, account_path="m/44'/60'/0'/0/0")
        return account.privateKey.hex(), account.address
    except Exception as e:
        return None, f"Error deriving account: {str(e)}"


if __name__ == "__main__":
    seed_phrase = generate_seed_phrase()
    print(f"Generated Seed Phrase: {seed_phrase}")
    print(derive_eth_address(seed_phrase))
