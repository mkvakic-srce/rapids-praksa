from mpi4py import MPI
import time
import random

def sum_list(initial_list, part_list):
    t = random.randint(0,5)
    # print('sleeping on rank %i for %i' % (rank, t))
    time.sleep(t)

    sum_list = []

    for i in range(len(part_list)):
        sum = part_list[i]

        for j in range(len(initial_list)):
            sum = sum + initial_list[j]

        sum_list.append(sum)

    return sum_list

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

    n = 10
    if rank == 0:
        initial_list = [1,] * n
    else:
        initial_list = None
        split_list = None

    # Data movement operation. Broadcasts (sends) a message from the 
    # process with rank “root” to all other processes in the group.
    # print("rank: ", rank, "i: ", i, "initial_list:", initial_list)

    # global init
    global_list = comm.bcast(initial_list, root = 0)

    for i in range(2):
                
        num_of_splits = n//numOfProccesses
        split_list = []
        for j in range(num_of_splits):
            split_list.append(global_list[j*num_of_splits:(j+1)*num_of_splits])  

        scattered_list = comm.scatter(split_list, root = 0)
        # print("rank: ",rank, "i: ", i, "scattered_list", scattered_list)

        sum_list_ = sum_list(global_list, scattered_list)
        # print("rank: ",rank, "i: ", i, "sum_list_", sum_list_)
        
        # gather takes elements from each process and gathers them to the root process. 
        # The elements are ordered by the rank of the process from which they were received.
        # The Comm.Gather method takes the same arguments as Comm.Scatter. Howeverm, in the gather operation, 
        # only the root process needs to have a valid receive buffer.
        print(rank, i, sum_list_)
        gathered_list = comm.gather(sum_list_, root = 0)
        # print("rank: ",rank, "i: ", i, "gathered_list",gathered_list)

        # update global with gathered
        if rank == 0:
            global_list = flattenList(gathered_list, numOfProccesses)

        

