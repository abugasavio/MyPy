import threading


def do_some_work(val):
    print('Doing some work')
    print(f'echo: {val} ')
    return 


val = 'text'

t = threading.Thread(target=do_some_work, args=(val,))
t.start()
t.join() # 
