def escaped_unicode(f):
    def wrap(*args, **kwargs):
        result = f(*args, **kwargs)
        return ascii(result)
    return wrap


@escaped_unicode
def city():
    return 'Såvio'


print(city())
