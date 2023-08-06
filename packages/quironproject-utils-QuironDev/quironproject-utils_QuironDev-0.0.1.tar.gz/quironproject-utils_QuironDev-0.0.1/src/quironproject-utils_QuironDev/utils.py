from random import randint
from datetime import datetime


def timer(function):
    def inner(*args, **kwargs):
        t_init = datetime.now()
        result = function(*args, **kwargs)
        t_end = datetime.now()

        print(f"Inital time: {t_init}")
        print(f" Final time: {t_end}")
        print(f" Total time: {t_end - t_init}")

        return result

    return inner


def catch(function):
    def inner(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as e:
            print(f"ERROR: {e}")
            result = None

        return result
    return inner


@timer
@catch
def secuence(x: int):
    r = randint(0, 10000)
    print(f"r = {r}")
    x = 1
    for i in range(r):
        x = x * r
        print(f"i={i}, x={x}")

        if x % randint(1, 10000) == 0:
            x / 0

    print(f"Final: {x}")


if __name__ == '__main__':
    secuence(10)
