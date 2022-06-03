from mpi4py import MPI

# pomnozi broj s dva
def double(x):
    return x*2

# pozvati hello funkciju ovisno o broju dostupnih jezgri
if __name__ == '__main__':

    # mpi
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    # scatter
    if rank == 0:
        n = 10**8
        numbers = list(range(n))
        sublists = [ numbers[i*n//size:(i+1)*n//size] for i in range(size) ]
    else:
        numbers = None
        sublists = None
    sublist = comm.scatter(sublists, root=0)

    # map and gather
    sublist_doubled = map(double, sublist)
    sublists_doubled = comm.gather(sublist_doubled, root=0)

    # print
    if comm.rank == 0:
        numbers_doubled = [ doubled_number for sublist_doubled in sublists_doubled for doubled_number in sublist_doubled ]
        print('numbers         : %s' % numbers[:5])
        print('numbers_doubled : %s' % numbers_doubled[:5])
