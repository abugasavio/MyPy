class Connection:
    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        print('starting a transaction', self.xid)
        rslt = self.xid
        self.xid = self.xid + 1
        return rslt

    def _commit_transaction(self, xid):
        print('commiting a transaction', xid)

    def _rollback_transaction(self, xid):
        print('Rolling back transaction', xid)


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)

    def rollback(self):
        self.conn._rollback_transaction(self.xid)


# using above
conn = Connection()
xact = Transaction(conn)
xact.commit()


# using a context manager
from contextlib import contextmanager

@contextmanager
def start_transaction(connection):
    tx = Transaction(connection)

    try:
        yield tx
    except:
        tx.rollback()
        raise
        
    tx.commit()


# using context manager

conn = Connection()

try:
    with start_transaction(conn) as tx:
        x = 1 + 1
        raise ValueError
        y = x + 1
        print('transaction 0', x, y)
except ValueError:
    print('Opps! transaction 0 failed')
