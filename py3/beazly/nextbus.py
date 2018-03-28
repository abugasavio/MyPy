import sys

if len(sys.argv) != 3:
    raise SystemExit("Usage: nextbus route stopid")

print("Command arguments: ", sys.argv)
