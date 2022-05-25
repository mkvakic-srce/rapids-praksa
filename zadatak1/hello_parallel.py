# zvanje potrebnih modula
import os
import random
import multiprocessing

# definirati funkciju hello koja ispisuje "Hello world!"
def hello(i):
    with open('./hello_%s.out' % i, 'w') as f:
        f.write('Hello world!')
        f.close()
    return

# pozvati hello funkciju ovisno o broju dostupnih jezgri
if __name__ == '__main__':

    # nslots - broj poslova koji odgovara varijabli okolisa NSLOTS
    nslots = int(os.getenv('NSLOTS'))

    # kreiraj multiprocessing pool
    pool = multiprocessing.Pool(nslots)

    # mapiraj listu procesa na pool
    results = pool.map(hello, range(nslots))
