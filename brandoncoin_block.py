import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """

        :param index: index of the block in the blockchain (this is optional)
        :param timestamp: creation time
        :param data: ideally any data, usually transactions
        :param previous_hash: the hash of preceding block in the blockchain, the link in the chain :)
        the hash is a cryptographic hash (in this case using sha256) of the blocks index,
        timestamp, data, and the previous hash

        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index)
                   + str(self.timestamp)
                   + str(self.data)
                   + str(self.previous_hash)
                   )
        return sha.hexdigest()
