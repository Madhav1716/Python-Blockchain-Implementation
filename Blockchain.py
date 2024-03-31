import hashlib

# Function to generate SHA-256 hash
def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()

# Block class representing a single block in the blockchain
class Block:
    def __init__(self, data, hash, prevhash):
        self.data = data         # Data stored in the block
        self.hash = hash         # Hash of the current block
        self.prevhash = prevhash # Hash of the previous block

# Blockchain class representing the entire blockchain
class Blockchain:
    def __init__(self):
        # Create the genesis block
        hashStart = hashGenerator('gen_hash')
        genesis = Block('gen-data', hashStart, '')
        self.chain = [genesis]  # Initialize the chain with the genesis block

    # Method to add a new block to the blockchain
    def add_Block(self, data):
        prev_hash = self.chain[-1].hash  # Get the hash of the previous block
        hash = hashGenerator(data + prev_hash)  # Generate hash for the new block
        block = Block(data, hash, prev_hash)    # Create a new block
        self.chain.append(block)                # Append the new block to the chain

# Create a new blockchain
bc = Blockchain()

# Add some blocks to the blockchain
bc.add_Block('1')
bc.add_Block('2')
bc.add_Block('3')
bc.add_Block('4')
bc.add_Block('5')

# Print details of each block in the blockchain
for block in bc.chain:
    print(block.__dict__)
