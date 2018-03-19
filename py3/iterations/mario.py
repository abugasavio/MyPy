height = 50

for i in range(height + 1):
    stars = i
    spaces = height - stars
    for j in range(spaces):
        print(" ", end="")
    for k in range(stars):
        print("*", end="")
    print(" ", end="")
    for m in range(stars):
        print("#", end="")
    print("")
for r in range(height, 0, -1):
    stars = r
    spaces = height - stars
    for m in range(spaces):
        print(" ", end="")
    for s in range(stars):
        print("*", end="")
    print(" ", end="")
    for _ in range(stars):
        print("#", end="")
    print("")
