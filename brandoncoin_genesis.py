import datetime as date
from brandoncoin_block import *


def create_genesis_block():
    """
    Manually create a block with
    index zero and arbitrary hash
    :return: genesis block
    """
    return Block(0, date.datetime.now(), {
        "proof-of-work": 9,
        "transactions": None
    }, "0")
