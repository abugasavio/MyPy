from reader.compressed.bzipped import opener as bz2_openner
from reader.compressed.gzipped import opener as gzip_openner

__all__ = ['bz2_openner', 'gzip_openner']
