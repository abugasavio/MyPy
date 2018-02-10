class TestableThing:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return True if self.value else False


# Testing for None

