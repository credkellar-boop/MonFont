from web3 import Web3
import json
import os

class MonadBridge:
    def __init__(self):
        # Connect to the Monad RPC endpoint
        self.w3 = Web3(Web3.HTTPProvider("https://rpc.testnet.monad.xyz"))
        self.account = self.w3.eth.account.from_key(os.getenv("PRIVATE_KEY"))
        
        # Load the contract address and ABI after deployment
        self.contract_address = "0x..." # Your deployed contract address
        with open("out/MonFontsRegistry.sol/MonFontsRegistry.json") as f:
            abi = json.load(f)['abi']
            self.contract = self.w3.eth.contract(address=self.contract_address, abi=abi)

    def register_on_chain(self, font_name: str, ipfs_hash: str):
        """Signs and broadcasts the font registration to the Monad network."""
        nonce = self.w3.eth.get_transaction_count(self.account.address)
        
        # Prepare the contract call
        txn = self.contract.functions.registerFont(font_name, ipfs_hash).build_transaction({
            'chainId': 10143,
            'gas': 200000,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': nonce,
        })
        
        # Sign and send
        signed_txn = self.w3.eth.account.sign_transaction(txn, self.account.key)
        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        
        return self.w3.to_hex(tx_hash)
