class TabelaHash:
    def __init__(self):
        self.table = {}

    def add(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key)

    def remove(self, key):
        if key in self.table:
            del self.table[key]

    def keys(self):
        return list(self.table.keys())
