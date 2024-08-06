from random import shuffle
"""
   first create an empty table of 256 bytes
   shuffle that hash table 
   perform xor operation between the hash value and the  
    """

class PersonHasher:
    def __init__(self):
        """
        docstring
        """
        self._table = [i for i in range(256)]

    def shuffleTable(self):
        """
        _summary_
        """
        shuffle(self._table)

    def pearsonHash(self, data: str):
        if isinstance(data, str):
            data = bytes(data, encoding='utf8')
        hashValue = 0
        for byte in data:
            hashValue = self._table[hashValue ^ byte]
        return hashValue
    
    def verifyMethod(self, data: str, hashValue: str):
        return self.pearsonHash(data) == hashValue
