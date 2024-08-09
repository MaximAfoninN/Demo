import math
import cProfile
from multiprocessing import Pool
#import io
#import pstats

def get_divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

def process_number(number):
    divisors = get_divisors(number)
    print(f"Divisors of {number}: {divisors}")
    return divisors


def main(numbers):
    with Pool() as pool:
        results = pool.map(process_number, numbers)
    return results

#def main(numbers):
#    profiler = cProfile.Profile()
#    profiler.enable()
#
#    with Pool() as pool:
#        results = pool.map(process_number, numbers)
#
#    profiler.disable()
#    s = io.StringIO()
#    sortby = 'cumulative'
#    ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
#    ps.print_stats()
#    print(s.getvalue())
#
#    return results


if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()  # Это требуется для совместимости с Windows
    numbers = [1500000, 2000000, 1234567, 20000000]  # Замените числами в диапазоне от 1_000_000 до 20_000_000
    results = main(numbers)
    print("All divisors calculated.")


