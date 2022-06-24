import math
import random
import pickle
from numba import cuda
import numpy as np

# seed
random.seed(69)

# konstante
nbodies = 10
gravity  = 6.67e-11
masscale = 6e25
lenscale = 150e9
velscale = 0*30e3
timestep = 3600
numsteps = 3


# izracunaj sile
@cuda.jit
def forces_kernel(x, y, m, fxout, fyout):
    pos1 = cuda.grid(1)
    pos2 = cuda.grid(1)
    if pos1 < len(x):
        fx, fy = 0, 0
        if pos2 < len(x):
            if pos1 != pos2:        
                dx = x[pos2] - x[pos1]
                dy = y[pos2] - y[pos1]
                r2 = dx**2 + dy**2
                fr = gravity*m[pos1]*m[pos2]/(r2 + (lenscale/100)**2)
                fx += fr*dx/r2**0.5
                fy += fr*dy/r2**0.5
        fxout[pos1] = fx
        fyout[pos1] = fy

# integriraj
@cuda.jit
def integrate_kernel(x, y, u, v, m, fx, fy, xout, yout, uout, vout):
    pos = cuda.grid(1) # 1D lista
    if pos < len(x):
        uout[pos] = u[pos] + fx[pos]/m[pos]*timestep
        vout[pos] = v[pos] + fy[pos]/m[pos]*timestep
        xout[pos] = x[pos] + u[pos]*timestep
        yout[pos] = y[pos] + v[pos]*timestep

# ograniči na domenu lenscale x lenscale
@cuda.jit
def limit_kernel(x, y, xout, yout):
    pos = cuda.grid(1) # 1D lista
    if pos < len(x):
        if abs(x[pos]) > lenscale:
            xout[pos] = x[pos] - (2*x[pos])
        if abs(y[pos]) > lenscale:
            yout[pos] = y[pos] - (2*y[pos])

# sudari
@cuda.jit
def collisions_kernel(x, y, u, v, m, xout, yout, uout, vout, mout):
    pos1 = cuda.grid(1)
    pos2 = cuda.grid(1)
    if pos1 < len(x):
        if pos2 < len(x): 
            if pos2 > pos1 and mout[pos2] is not math.nan:
                dx = x[pos2] - x[pos1]
                dy = y[pos2] - y[pos1]
                r = math.sqrt(dx**2 + dy**2)
                if r < lenscale/1000:
                    mM = m[pos1] + m[pos2]
                    uM = (u[pos1]*m[pos1]+u[pos2]*m[pos2])/mM
                    vM = (v[pos1]*m[pos1]+v[pos2]*m[pos2])/mM
                    mout[pos1] = mM
                    uout[pos1] = uM
                    vout[pos1] = vM
                    mout[pos2] = math.nan
                    uout[pos2] = math.nan
                    vout[pos2] = math.nan
                    xout[pos2] = math.nan
                    yout[pos2] = math.nan

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
        # fx, fy = forces(x, y, m)

        fx = np.array([0,] * len(x))
        fy = np.array([0,] * len(y))
        forces_kernel[blockspergrid, threadsperblock](x, y, m, fx, fy)

        # integriraj
        xout = np.array([0,] * len(x))
        yout = np.array([0,] * len(y))
        uout = np.array([0,] * len(u))
        vout = np.array([0,] * len(v))

        integrate_kernel[blockspergrid, threadsperblock](x, y, u, v, m, fx, fy, xout, yout, uout, vout)

        x = np.copy(xout)        
        y = np.copy(yout)
        u = np.copy(uout)
        v = np.copy(vout)

        #ograniči
        xout = np.array([0,] * len(x))
        yout = np.array([0,] * len(y))
        
        limit_kernel[blockspergrid, threadsperblock](x, y, xout, yout)
        
        x = np.copy(xout)
        y = np.copy(yout)

        # sudari
        xout = np.copy(x)
        yout = np.copy(y)
        uout = np.copy(u)
        vout = np.copy(v)
        mout = np.copy(m)
        
        collisions_kernel[blockspergrid, threadsperblock](x, y, u, v, m, xout, yout, uout, vout, mout)


        x = np.array([ x for x in xout if x is not math.nan ])
        y = np.array([ y for y in yout if y is not math.nan ])
        u = np.array([ u for u in uout if u is not math.nan ])
        v = np.array([ v for v in vout if v is not math.nan ])
        m = np.array([ m for m in mout if m is not math.nan ])

        print(x)

        # dodaj u vremenski slijed
        # if (i*timestep)%(24*3600) == 0:
        #     print('%6i / %6i' % (i*timestep/3600, numsteps*timestep/3600))
        #     xt.append(x)
        #     yt.append(y)

    # # ispiši
    # with open('nbody.xt', 'wb') as f:
    #     pickle.dump(xt, f)
    #     f.close()

    # with open('nbody.yt', 'wb') as f:
    #     pickle.dump(yt, f)
    #     f.close()