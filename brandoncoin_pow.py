import json
import datetime as date
from brandoncoin_block import Block
from brandoncoin import blockchain
from brandoncoin import node
from brandoncoin import this_nodes_transactions

miner_address = "q3nf394hjg-random-miner-address-34nf3i4nflkn3oi"


def proof_of_work(last_proof):
    # Instantiate variable that will be
    # used to find next proof of work
    incrementor = last_proof + 1
    # increment until it is divisible
    # by 9 and the last proof of work
    while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
        incrementor += 1
    # return the number as proof of work
    return incrementor


@node.route('/mine', methods=['GET'])
def mine():
    # Get last proof of work
    last_block = blockchain[-1]
    print last_block.data
    last_proof = last_block.data['proof-of-work']
    # Find the current proof of work
    # Note the program will hang until this is solved
    proof = proof_of_work(last_proof)
    # Once we find the right proof of work,
    # we know a new block can be generated
    # we reward the miner with a transaction
    this_nodes_transactions.append(
        {"from": "network", "to": miner_address, "amount": 1}
    )

    # Now we gather the data needed to generate the new block
    new_block_data = (
        {
            "proof-of-work": proof,
            "transactions": list(this_nodes_transactions)
        }
    )
    new_block_index = last_block.index + 1
    new_block_timestamp = this_timestamp = date.datetime.now()
    last_block_hash = last_block.hash
    # Empty transaction list
    this_nodes_transactions[:] = []
    # Create new block
    mined_block = Block(
        new_block_index,
        new_block_timestamp,
        new_block_data,
        last_block_hash
    )
    blockchain.append(mined_block)
    # Let the client know we mined a block
    return json.dumps({
        "index": mined_block.index,
        "timestamp": str(mined_block.timestamp),
        "data": mined_block.data,
        "hash": mined_block.hash
    }) + "\n"
