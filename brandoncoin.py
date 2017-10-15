from flask import Flask
import brandoncoin_genesis

# Instantiate Variables
node = Flask(__name__)
blockchain = [brandoncoin_genesis.create_genesis_block()]
this_nodes_transactions = []
peer_nodes = []

import brandoncoin_transaction_submission
import brandoncoin_pow

node.run()
