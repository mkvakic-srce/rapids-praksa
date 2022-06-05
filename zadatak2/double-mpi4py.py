# podignuti mpi4py modul
from mpi4py import MPI

# pomnozi listu brojeva s dva
def double(numbers):
    doubled = []
    for number in numbers:
        double = number*2
        doubled.append(double)
    return doubled

# pozvati hello funkciju ovisno o broju dostupnih jezgri
if __name__ == '__main__':

    # inicijaliziraj MPI
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    # definiraj listu brojeva ovisno o rangu
    if rank == 0:
        n = 10**8
        numbers = list(range(n))
    else:
        numbers = None

    # razdijeli i raspodijeli listu brojeva na ostale jezgre putem scatter
    if rank == 0:
        sublists = []
        for i in range(size):
            stride = n//size
            start = i*stride
            end = start + stride
            sublists.append(numbers[start:end])
    else:
        sublists = None
    sublist = comm.scatter(sublists, root=0)

    # izracunaj listu udvostrucenih brojeva i spoji ih nazad pomocu gather
    sublist_doubled = double(sublist)
    sublists_doubled = comm.gather(sublist_doubled, root=0)

    # print
    if comm.rank == 0:
        doubled = [ doubled_number for sublist_doubled in sublists_doubled for doubled_number in sublist_doubled ]
        print('numbers : %s' % numbers[:5])
        print('doubled : %s' % doubled[:5])
