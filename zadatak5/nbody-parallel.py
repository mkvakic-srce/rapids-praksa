import chunk
import math
import random
import pickle
from mpi4py import MPI

# seed
random.seed(69)

# konstante
nbodies = 10 # broj N-tijela
gravity  = 6.67e-11 # gravitacijska konstanta
masscale = 6e25 
lenscale = 150e9
velscale = 0*30e3
timestep = 3600
numsteps = 1

def flattenList(list, size):
    n = []
    for i in list:
        for j in i:
            n.append(j)
    return n

# izracunaj sile
# racuna sile između tijela u svakom trenutku
def forces(*args):
    fxout, fyout = [], []
    for i, (xi, yi, mi) in enumerate(zip(*args)): # ovo bi trebala biti podlista
        fx, fy = 0, 0
        for j, (xj, yj, mj) in enumerate(zip(*args)): # za svaki član liste
            if i != j:
                dx = xj-xi
                dy = yj-yi
                r2 = dx**2 + dy**2
                fr = gravity*mi*mj/(r2 + (lenscale/100)**2)
                fx += fr*dx/r2**0.5
                fy += fr*dy/r2**0.5
        fxout.append(fx)
        fyout.append(fy)
    return fxout, fyout

# integriraj (update)
def integrate(*args):
    xout, yout, uout, vout = [], [], [], [] # 4 prazne liste
    for x, y, u, v, m, fx, fy in zip(*args):
        uout.append(u + fx/m*timestep)
        vout.append(v + fy/m*timestep)
        xout.append(x + u*timestep)
        yout.append(y + v*timestep)
    return xout, yout, uout, vout


# ograniči na domenu lenscale x lenscale
def limit(*args):
    xout, yout = [], []
    for x, y in zip(*args):
        if abs(x) > lenscale:
            x -= 2*x
        if abs(y) > lenscale:
            y -= 2*y
        xout.append(x)
        yout.append(y)
    return xout, yout

# sudari
def collisions(x, y, u, v, m):
    xout = x[:] # creating shallow copy of a list
    yout = y[:]
    uout = u[:]
    vout = v[:]
    mout = m[:]
    for i, (xi, yi, ui, vi, mi) in enumerate(zip(x, y, u, v, m)):
        for j, (xj, yj, uj, vj, mj) in enumerate(zip(x, y, u, v, m)):
            if j > i and mout[j] is not math.nan:
                dx = xj-xi
                dy = yj-yi
                r = math.sqrt(dx**2+dy**2)
                if r < lenscale/1000:
                    mM = mi+mj
                    uM = (ui*mi+uj*mj)/mM
                    vM = (vi*mi+vj*mj)/mM
                    mout[i] = mM
                    uout[i] = uM
                    vout[i] = vM
                    mout[j] = math.nan
                    uout[j] = math.nan
                    vout[j] = math.nan
                    xout[j] = math.nan
                    yout[j] = math.nan
    mout = [ m for m in mout if m is not math.nan ] # list comprehension
    uout = [ u for u in uout if u is not math.nan ]
    vout = [ v for v in vout if v is not math.nan ]
    xout = [ x for x in xout if x is not math.nan ] 
    yout = [ y for y in yout if y is not math.nan ]
    return xout, yout, uout, vout, mout

if __name__ == "__main__":

    # inicijaliziraj MPI
    comm = MPI.COMM_WORLD
    numOfProccesses = comm.Get_size() # total number of processes running
    rank = comm.Get_rank() # number of the process running the code (counter of running process)

    if rank == 0:

        # definiraj sistem
        x = [ random.uniform(-1, 1)*lenscale for i in range(nbodies) ] # x-os
        y = [ random.uniform(-1, 1)*lenscale for i in range(nbodies) ] # y-os
        u = [ random.uniform(-1, 1)*velscale for i in range(nbodies) ] # brzina u x
        v = [ random.uniform(-1, 1)*velscale for i in range(nbodies) ] # brzina u y osi
        m = [ masscale for i in range(nbodies) ] # masa - za svaki objekt ista

    else: 

        x, y, u, v, m = None, None, None, None, None

    split_len = nbodies//numOfProccesses

    # simuliraj
    xt, yt = [], []
    for i in range(numsteps): # numsteps = 10**5

        x = comm.bcast(x, root = 0)
        y = comm.bcast(y, root = 0)
        u = comm.bcast(u, root = 0)
        v = comm.bcast(v, root = 0)
        m = comm.bcast(m, root = 0)

        if rank == 0:

            # print("forces")
            # izračunaj sile
            fx, fy = forces(x, y, m)

            # integriraj (update)
            x, y, u, v = integrate(x, y, u, v, m, fx, fy)

        split_list_y = []
        for j in range(numOfProccesses):
            split_list_y.append(y[j*split_len:(j+1)*split_len])  

        split_list_x = []
        for j in range(numOfProccesses):
            split_list_x.append(x[j*split_len:(j+1)*split_len]) 

        sc_list_x = comm.scatter(split_list_x, root = 0)
        sc_list_y = comm.scatter(split_list_y, root = 0)

        # ograniči     
        x, y = limit(sc_list_x, sc_list_y)

        gathered_list_x = comm.gather(x, root = 0)
        gathered_list_y = comm.gather(y, root = 0)

        if rank == 0:
            x = flattenList(gathered_list_x, numOfProccesses)
            y = flattenList(gathered_list_y, numOfProccesses)

            # sudari
            x, y, u, v, m = collisions(x, y, u, v, m)

            # dodaj u vremenski slijed
            if (i*timestep)%(24*3600) == 0:
                print('%6i / %6i' % (i*timestep/3600, numsteps*timestep/3600))
                xt.append(x)
                yt.append(y)

    if rank == 0:

        print(x)
        print(y)
        
        # ispiši
        with open('nbody.xt', 'wb') as f:
            pickle.dump(xt, f)
            f.close()

        with open('nbody.yt', 'wb') as f:
            pickle.dump(yt, f)
            f.close()

# advanced for loops
# x = [(1,2), (3,4), (5,6)]
# for a, b in x:
#     print(a, "plus", b, "equals", a+b)
# 1 plus 2 equals 3
# 3 plus 4 equals 7
# 5 plus 6 equals 11



# enumerate()
# The enumerate function in Python converts a data collection object into an enumerate object. 
# Enumerate returns an object that contains a counter as a key for each value within an object, 
# making items within the collection easier to access.

# Looping through objects is useful but we often need the means to track loops, 
# and the items accessed within that iteration of the loop. Enumerate helps with this 
# need by assigning a counter to each item in the object, allowing us to track the accessed items.



# zip() 
# Using zip() in Python
# Python’s zip() function is defined as zip(*iterables). 
# The function takes in iterables as arguments and returns an iterator. 
# This iterator generates a series of tuples containing elements from each iterable. 
# zip() can accept any type of iterable, such as files, lists, tuples, dictionaries, sets, and so on.

# Here, you use zip(numbers, letters) to create an iterator that produces tuples of the form (x, y). 
# In this case, the x values are taken from numbers and the y values are taken from letters. 
# Notice how the Python zip() function returns an iterator. To retrieve the final list object, 
# you need to use list() to consume the iterator.

# numbers = [2, 1, 3]
# letters = ['a', 'b', 'c']
# zipped = zip(numbers, letters)
# print(list(zipped))
# [(2, 'a'), (1, 'b'), (3, 'c')]



# shallow copy of a list
# Shallow copy is a bit-wise copy of an object. 
# A new object is created that has an exact copy of the values in the original object

# a_list = [1, 2, 3]
# b_list = a_list[:]
# a_list[0] = 100
# b_list[1] = 200

# print(b_list)
# print(id(b_list))

# print(a_list)
# print(id(a_list))

# brojevi nisu reference pa se zato razlikuju
# [1, 200, 3]
# 24783048
# [100, 2, 3]
# 24782008



# list comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# print(newlist)

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(h_letters)
# ['h', 'u', 'm', 'a', 'n']

# With list comprehension you can do all that with only one line of code:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)
# ['h', 'u', 'm', 'a', 'n']



# “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, 
# and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) 
# is converted back into an object hierarchy.

# Then use pickle.dump() function to store the object data to the file. pickle.dump() function takes 3 arguments. 
# The first argument is the object that you want to store. The second argument is the file object you get by opening the desired file 
# in write-binary (wb) mode. And the third argument is the key-value argument. This argument defines the protocol. There are two type of 
# protocol - pickle.HIGHEST_PROTOCOL and pickle.DEFAULT_PROTOCOL. 



# results = [expression for x in range(10)]
# expression can include anything you like - a string, a calculation, a function - whatever you choose. 
# If the expression happens to be just x then it looks unusual if you are not used to it, but it's the same as the following:

# results = []
# for x in range(10):
#     results.append(expression)