from blockchain import Blockchain
from time import sleep

def main():
    print("🚀 Starting Blockchain from Scratch Demo...\n")
    
    # Create the blockchain
    my_blockchain = Blockchain()
    
    print("Genesis block created!")
    my_blockchain.print_chain()
    
    input("\nPress Enter to add some transactions...")
    
    # Add some transactions
    print("\nAdding transactions...")
    my_blockchain.add_transaction("Alice", "Bob", 50)
    my_blockchain.add_transaction("Bob", "Charlie", 25)
    my_blockchain.add_transaction("Charlie", "Alice", 10)
    
    print("Transactions added to pending list.")
    
    input("\nPress Enter to mine a new block...")
    
    # Mine the block (this may take a few seconds depending on difficulty)
    my_blockchain.mine_pending_transactions("Miner1")
    
    # Add more transactions
    print("\nAdding more transactions...")
    my_blockchain.add_transaction("Dave", "Eve", 100)
    my_blockchain.add_transaction("Eve", "Frank", 30)
    
    input("\nPress Enter to mine second block...")
    my_blockchain.mine_pending_transactions("Miner2")
    
    # Show the full chain
    print("\n" + "="*60)
    print("FINAL BLOCKCHAIN")
    print("="*60)
    my_blockchain.print_chain()
    
    # Validate the chain
    print("\nValidating blockchain...")
    if my_blockchain.is_chain_valid():
        print("✅ Blockchain is valid!")
    else:
        print("❌ Blockchain has been tampered with!")
    
    # Demonstrate tampering (optional)
    print("\nDemonstrating tamper detection...")
    my_blockchain.chain[1].transactions = ["Tampered transaction"]
    if my_blockchain.is_chain_valid():
        print("❌ Tamper detection failed!")
    else:
        print("✅ Tamper detection working! Blockchain correctly identified tampering.")

if __name__ == "__main__":
    main()
