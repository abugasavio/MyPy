import json

with open("./backup_config.json") as fh:
    data = json.load(fh)

data['test'] = 'testing'

with open("./backup_config.json", "w") as fh:
    json.dump(data, fh, indent=2, separators=(',', ': '))

