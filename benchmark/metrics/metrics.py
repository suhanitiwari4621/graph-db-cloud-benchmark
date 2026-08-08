import time


def measure(func):
    start = time.perf_counter()

    func()

    end = time.perf_counter()

    return round(end - start, 6)