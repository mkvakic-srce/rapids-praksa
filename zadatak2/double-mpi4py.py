# podignuti mpi4py modul
from mpi4py import MPI
import math # ceil

def splitList(orgList, numOfProccesses):
    n_split_list = []    
    for i in range(0,len(orgList), numOfProccesses):
        n_split_list.append(orgList[i:i+numOfProccesses])    
    return n_split_list

def GetDoubleValues(list):
    n = []
    for i in list:
        n.append(i*2)
    return n

def flattenList(list, size):
    n = []
    for i in list:
        for j in i:
            n.append(j)
    return n

if __name__ == '__main__':

    # inicijaliziraj MPI
    comm = MPI.COMM_WORLD
    numOfProccesses = comm.Get_size() # total number of processes running
    rank = comm.Get_rank() # number of the process running the code (counter of running process)

    # definiraj listu brojeva ovisno o rangu
    if rank == 0:
        n = 10**8
        numbers = list(range(0, n))

            # scatter expects list of lists, divided for every iter
        # split_list = splitList(numbers, len(numbers)//numOfProccesses) # // floor of decimal, should be ceil, screws with odd numOfProccesses
        n_splits = math.ceil(len(numbers)/numOfProccesses)
        split_list = splitList(numbers, n_splits) # // ciel of decimal
    else:
        numbers = None
        split_list = None

    # razdijeli i raspodijeli listu brojeva na ostale jezgre putem scatter
    scattered_list = comm.scatter(split_list, root = 0)
        # runs every iteration, scatteres only in root process

    # izracunaj listu udvostrucenih brojeva i spoji ih nazad pomocu gather
    double_values_list = GetDoubleValues(scattered_list)
        # this should run in each process

        # gathering back in root process
    gathered_list = comm.gather(double_values_list, root = 0)

    # isprintaj prvih pet brojeva u originalnoj i udvostrucenoj listi
    if rank == 0:

            # flattening gathered list (as 1D array)
        flatten_list = flattenList(gathered_list, numOfProccesses)
        print(numbers[:5])
        print(flatten_list[:5])