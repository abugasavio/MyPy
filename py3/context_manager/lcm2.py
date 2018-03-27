import sys
from contextlib import contextmanager

@contextmanager
def lcm():
    try:
        print('Just entered the context manager')
        yield
        print('LoggingContextManager.__exit__: normal exit detected.")
    except Exception:
        print('LoggingContextManager.__exit__:Exception detected.{}'.format(sys.exc_info()) )
        raise 
