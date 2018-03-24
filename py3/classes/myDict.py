class ConfigDict(dict):
    def __init__(self, file):
        self.file = file
        self.data = {}
        with open(self.file, 'r') as conf_file:
            for line in conf_file:
                key, val = line.rstrip().split("=", 1)
                self.data[key] = val


    def write_to_file(self):
        with open(self.file, 'w+') as conf_file:
            for key, val in self.data.items():
                conf_file.write("{}={}\n".format(key,val))

    def __setitem__(self, key, val):
        self.data[key] = val
        self.write_to_file()

    def __getitem__(self, key):
        return self.data[key]

    def __str__(self):
        return "{}".format(self.data)
        
