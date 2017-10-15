import json
import requests
from brandoncoin import node
from brandoncoin import peer_nodes
from brandoncoin import blockchain


@node.route('/blocks', methods=['GET'])
def get_blocks():
    chain_to_send = blockchain
    # Convert our blocks into dictionaries
    # so we can send them as json objects later
    # must be json so that we can include in the
    # HTTP request body
    for block in chain_to_send:
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = block.hash
        block = {
            "index": block_index,
            "timestamp": block_timestamp,
            "data": block_data,
            "hash": block_hash
        }
    # send our chain to whoever requested it
    chain_to_send = json.dumps(chain_to_send)
    return chain_to_send


def find_new_chains():
    # Get the blockchain of every other node
    other_chains = []
    for node_url in peer_nodes:
        # Get their chains with a GET request
        block = requests.get(node_url + "/blocks").content
        # Convert the JSON object to a python dictionary
        block = json.loads(block)
        # Add it to our list
        other_chains.append(block)
    return other_chains


def consensus():
    # Get the other chains
    other_chains = find_new_chains()
    # Compare the length of our
    # blockchain to the rest of the chains
    # the longest chain is pressumed
    # to be correct
    longest_chain = blockchain
    for chain in other_chains:
        if len(chain) > len(longest_chain):
            longest_chain = chain
    # Incase our chain is not the longest, we
    # set our chain equal to the current longest
    blockchain = longest_chain

