import collections
route = {'id': 271, 'title': 'Fast app'}

new = {}
for k, v in route.items():
    new[v] = k


def print_items(**items):
    print(items)


print_items(**route)


# Accessing data in a dict
data = {
    "year": 2001, "country": "Kenya"
}


data = collections.defaultdict(lambda: "MISSING", data)
print(data["rating"])

 
