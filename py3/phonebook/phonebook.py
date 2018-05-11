from pathlib import Path


class Phonebook:
    def __init__(self):
        self.entries = {}
        self.filename = 'filename.txt'
        self.file_cache = open(self.filename, 'w')

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def clear(self):
        self.entries = {}
        self.file_cache.close()
        f = Path(self.filename)
        f.unlink()
