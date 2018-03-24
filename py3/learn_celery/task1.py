from celery import Celery

app = Celery('task1', broker='')
app.conf.update(
    result_backend="cache+memcached://127.0.0.1:11211/"
)


@app.task
def add(x, y):
    return x + y
