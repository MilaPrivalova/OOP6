from datetime import datetime as dt
path = 'log.txt'

def logger_one(first, second, oper, res):
    log = f'{dt.now()} | {first} {oper} {second} = {res}\n'
    with open(path, 'a') as data:
        data.write(log)


def logger_two(math_var, res):
    log = f'{dt.now()} | {math_var} = {res}\n'
    with open(path, 'a') as data:
        data.write(log)
