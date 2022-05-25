# zvanje potrebnih modula
import os
import time
import multiprocessing

# pomnozi broj s dva
def double(x):
    return x*2

# pozvati hello funkciju ovisno o broju dostupnih jezgri
if __name__ == '__main__':

    # nslots - broj poslova koji odgovara varijabli okolisa NSLOTS
    nslots = int(os.getenv('NSLOTS'))

    # kreiraj multiprocessing pool
    pool = multiprocessing.Pool(nslots)

    # lista brojeva
    n = 10**8
    numbers = list(range(n))

    # mapiraj listu procesa na pool
    numbers_doubled = pool.map(double, numbers)

    # print
    print('numbers         : %s' % numbers[:5])
    print('numbers_doubled : %s' % numbers_doubled[:5])
