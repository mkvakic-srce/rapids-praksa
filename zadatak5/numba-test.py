import math
import random
import pickle
from numba import cuda
import numpy as np

# seed
random.seed(69)

# konstante
nbodies = 50
gravity  = 6.67e-11
masscale = 6e25
lenscale = 150e9
velscale = 0*30e3
timestep = 3600
numsteps = 10000


@cuda.reduce
def reduce(x, y):
    return x + y

@cuda.jit
def forces_kernel(i, x, y, m, xi, yi, mi, fx_array, fy_array):

    pos = cuda.grid(1)

    if pos < len(x):
        if i != pos:

            dx = x[pos] - xi
            dy = y[pos] - yi

            r2 = dx**2 + dy**2
            fr = gravity*mi*m[pos]/(r2 + (lenscale/100)**2)

            fx_array[pos] = fr*dx/r2**0.5
            fy_array[pos] = fr*dy/r2**0.5

# izracunaj sile
def forces(x, y, m):

    n = len(y)

    fxout = np.zeros(n)
    fyout = np.zeros(n)

    for i in range(n):

        fx_array = np.zeros(n)
        fy_array = np.zeros(n)

        # numba params
        threadsperblock = 32
        blockspergrid = (n + (threadsperblock - 1)) // threadsperblock

        forces_kernel[blockspergrid, threadsperblock](i, x, y, m, x[i], y[i], m[i], fx_array, fy_array)

        fx = reduce(fx_array) # suma fx_array pomocu reduce
        fy = reduce(fy_array)

        fxout[i] = fx
        fyout[i] = fy

    return fxout, fyout

# integriraj
@cuda.jit
def integrate_kernel(x, y, u, v, m, fx, fy):
    pos = cuda.grid(1) # 1D lista
    if pos < len(x):
        y[pos] = y[pos] + v[pos]*timestep
        x[pos] = x[pos] + u[pos]*timestep
        v[pos] = v[pos] + fy[pos]/m[pos]*timestep
        u[pos] = u[pos] + fx[pos]/m[pos]*timestep

# ograniči na domenu lenscale x lenscale
@cuda.jit
def limit_kernel(x, y):
    pos = cuda.grid(1) # 1D lista

    if pos < len(x):
        if abs(x[pos]) > lenscale:
            x[pos] = x[pos] - (2*x[pos])
        if abs(y[pos]) > lenscale:
            y[pos] = y[pos] - (2*y[pos])

@cuda.jit
def collisions_kernel(i, x, y, u, v, m, xi, yi, ui, vi, mi, x_array, y_array, u_array, v_array, m_array):

    pos = cuda.grid(1)
    if pos < len(x):
        if pos > i and m_array[pos] is not math.nan:

            dx = x[pos] - xi
            dy = y[pos] - yi
            r = math.sqrt(dx**2+dy**2)

            if r < lenscale/1000:

                mM = mi+m[pos]
                uM = (ui+mi+u[pos]+m[pos])/mM
                vM = (vi*mi*v[pos]*m[pos])/mM

                m_array[i] = mM
                u_array[i] = uM
                v_array[i] = vM

                m_array[pos] = math.nan
                u_array[pos] = math.nan
                v_array[pos] = math.nan
                x_array[pos] = math.nan
                y_array[pos] = math.nan

def collisions(x, y, u, v, m):

    x_array = x[:]
    y_array = y[:]
    u_array = u[:]
    v_array = v[:]
    m_array = m[:]

    for i in range(len(x)):

        # numba params
        threadsperblock = 32
        blockspergrid = (len(x) + (threadsperblock - 1)) // threadsperblock

        collisions_kernel[blockspergrid, threadsperblock](i, x, y, u, v, m, x[i], y[i], u[i], v[i], m[i], x_array, y_array, u_array, v_array, m_array)

    x_array = np.array([ x for x in x_array if x is not math.nan ])
    y_array = np.array([ y for y in y_array if y is not math.nan ])
    u_array = np.array([ u for u in u_array if u is not math.nan ])
    v_array = np.array([ v for v in v_array if v is not math.nan ])
    m_array = np.array([ m for m in m_array if m is not math.nan ])

    return x_array, y_array, u_array, v_array, m_array


if __name__ == "__main__":

    # definiraj sistem
    x = np.array([ random.uniform(-1, 1)*lenscale for i in range(nbodies) ])
    y = np.array([ random.uniform(-1, 1)*lenscale for i in range(nbodies) ])
    u = np.array([ random.uniform(-1, 1)*velscale for i in range(nbodies) ])
    v = np.array([ random.uniform(-1, 1)*velscale for i in range(nbodies) ])
    m = np.array([ masscale for i in range(nbodies) ])

    # numba params
    threadsperblock = 32
    blockspergrid = (len(x) + (threadsperblock - 1)) // threadsperblock

    # simuliraj
    xt, yt = [], []
    for i in range(numsteps):

        # izračunaj sile
        fx, fy = forces(x, y, m)

        # integriraj
        integrate_kernel[blockspergrid, threadsperblock](x, y, u, v, m, fx, fy)

        #ograniči
        limit_kernel[blockspergrid, threadsperblock](x, y)

        # sudari
        x, y, u, v, m = collisions(x, y, u, v, m)

        # dodaj u vremenski slijed
        if (i*timestep)%(24*3600) == 0:
            print('%6i / %6i' % (i*timestep/3600, numsteps*timestep/3600))
            xt.append(x)
            yt.append(y)

    # ispiši
    with open('nbody.xt', 'wb') as f:
        pickle.dump(xt, f)
        f.close()

    with open('nbody.yt', 'wb') as f:
        pickle.dump(yt, f)
        f.close()