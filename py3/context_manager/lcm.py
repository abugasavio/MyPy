class LoggingContextManager:
    def __enter__(self):
        print("Just entered the context manager")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('LoggingContextManager.__exit__({}, {}, {})'.format(exc_type, exc_val, exc_tb))
        return   

