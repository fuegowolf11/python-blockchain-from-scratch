from block import Block
from time import time

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Number of leading zeros required
        self.pending_transactions = []

    def create_genesis_block(self):
        """Create the first block in the chain"""
        return Block(0, "0", ["Genesis Block"])

    def get_latest_block(self):
        """Return the most recent block"""
        return self.chain[-1]

    def add_transaction(self, sender, recipient, amount):
        """Add a new transaction to pending transactions"""
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        self.pending_transactions.append(transaction)
        return self.get_latest_block().index + 1

    def mine_pending_transactions(self, miner_address):
        """Mine a new block with pending transactions"""
        block = Block(
            index=len(self.chain),
            previous_hash=self.get_latest_block().hash,
            transactions=self.pending_transactions
        )
        
        print(f"Mining block {block.index}...")
        block.mine_block(self.difficulty)
        
        self.chain.append(block)
        # Reward the miner
        self.pending_transactions = [{
            "sender": "System",
            "recipient": miner_address,
            "amount": 10  # Mining reward
        }]
        
        print(f"Block {block.index} successfully mined and added to chain!")

    def is_chain_valid(self):
        """Validate the entire blockchain"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if current block hash is correct
            if current_block.hash != current_block.calculate_hash():
                return False

            # Check if previous hash link is correct
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_chain(self):
        """Print the entire blockchain"""
        print("\n=== BLOCKCHAIN ===")
        for block in self.chain:
            print(f"\nBlock #{block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Transactions: {len(block.transactions)}")
            print(f"Nonce: {block.nonce}")
            print("-" * 60)
