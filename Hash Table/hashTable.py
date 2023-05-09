
class HashTable:
    def __init__(self, max_hash_table_size = 1024):
        """
        Initializes a new hash table with the given maximum size.

        """
        self.data_list = [None] * max_hash_table_size
        self.max_hash_table_size = max_hash_table_size
        self.size = 0
        self.treshold = 0.5

    def get_index(self, key) -> int:
        """
        Calculates the hash code for the given key and returns the index in the
        hash table where the corresponding data should be stored or retrieved.

        """
        return hash(key) % self.max_hash_table_size

    def __len__(self):
        """
        Returns the number of key-value pairs in the hash table.

        """
        return self.size

    def __iter__(self):
        """
        Returns an iterator over the key-value pairs in the hash table.

        """
        return (key for key in self.data_list if key is not None)

    def __setitem__(self, key, value):
        """
        Sets the value associated with the given key in the hash table.

        """
        if self.size / self.max_hash_table_size >= self.treshold:
            self._resize()

        idx = self.get_index(key)
        self.data_list[idx] = (key, value)
        self.size += 1

    def __getitem__(self, key):
        """
        Returns the value associated with the given key in the hash table.

        """
        idx = self.get_index(key)
        if self.data_list[idx] is None:
            raise KeyError(f'Key not found: {key}')
        return self.data_list[idx][1]

    def __delitem__(self, key):
        """
        Deletes the key-value pair associated with the given key from the hash table.

        """
        idx = self.get_index(key)
        if self.data_list[idx] is None:
            raise KeyError(f'Key not found: {key}')

        self.data_list[idx] = None
        self.size -= 1

    def _resize(self):
        """
        Resizes the hash table to accommodate more key-value pairs.

        """
        self.max_hash_table_size *= 2
        old_data_list = self.data_list
        self.data_list = [None] * self.max_hash_table_size

        for item in old_data_list:
            if item:
                idx = hash(item[0])
                self.data_list[idx] = item


