class LoggingContextManager:
    def __enter__(self):
        print("Just entered the context manager")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('LoggingContextManager.__exit__: normal exit detexted.")
        else:
            print('LoggingContextManager.__exit__:Exception detected.'.format(exc_type, exc_val, exc_tb))
        return   

