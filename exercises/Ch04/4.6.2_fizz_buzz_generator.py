from itertools import count, islice
from toolz import pipe

def fizz_buzz_gen():
    for i in count(start=1):
        if i % 3 == 0 and i % 5 == 0:
            yield 'fizz buzz'
        elif i % 3 == 0:
            yield 'fizz'
        elif i % 5 == 0:
            yield 'buzz'
        else:
            yield i

fizz_buzz_gen = fizz_buzz_gen()
print(list(islice(fizz_buzz_gen, 100)))

## make fizzbuzz a function then pipe with a generator
def fizz_buzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return 'fizzbuzz'
    elif i % 3 == 0:
        return 'fizz'
    elif i % 5 == 0:
        yield 'buzz'
    else:
        return i

print(islice(pipe(i, fizz_buzz)), 1, 101)
