import datetime as date
from brandoncoin_block import *


def generate_block(last_block):
    """

    :param last_block: the last block on the blockchain,
    needed to calculate index and hash
    :return: a new block using: the current index, timestamp, data, and the previous hash
    """
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hello World! I am Block number " + str(this_index) + "!"
    return Block(this_index, this_timestamp, this_data, last_block.hash)