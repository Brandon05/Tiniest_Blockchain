
from flask import request
from brandoncoin import node

# Store transactions
# from node in list
this_nodes_transactions = []


@node.route('/txion', methods=['POST'])
def transaction():
    if request.method == 'POST':
        # On each new Post request,
        # we extract the transaction data
        new_txion = request.get_json()
        # Then we append to the
        # transaction list
        this_nodes_transactions.append(new_txion)
        # Since the transaction was successfully,
        # submitted we log it to our console
        print "NEW TRANSACTION"
        print "FROM: {}".format(new_txion['from'])
        print "TO: {}".format(new_txion['to'])
        print "AMOUNT: {}".format(new_txion['amount'])
        # We then let the client know it worked
        return "Transaction submitted successfully\n"
