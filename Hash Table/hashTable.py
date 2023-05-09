
class HashTable:
    def __init__(self, max_hash_table_size = 4096):
        """
        Initializes a new hash table with the given maximum size.

        """
        self.data_list = [None] * max_hash_table_size
        self.max_hash_table_size = max_hash_table_size
        self.size = 0

    def get_index(self, key) -> int:
        """
        Calculates the hash code for the given key and returns the index in the
        hash table where the corresponding data should be stored or retrieved.

        """
        return hash(key) % self.max_hash_table_size


ht = HashTable()
print(ht.get_index("key") )
