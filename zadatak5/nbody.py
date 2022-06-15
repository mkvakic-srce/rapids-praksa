import random
import numpy as np
import matplotlib.pyplot as plt

# konstante
nbodies = 3
gravity = 1e0
timestep = 1e-2
numsteps = 1000
lenscale = 10
velscale = 1

# izracunaj sile
def forces_calc(x, y):
    fsx = []
    fsy = []
    for i, (x0, y0) in enumerate(zip(x, y)):
        fx = 0
        fy = 0
        for j, (xi, yi) in enumerate(zip(x, y)):
            if i == j:
                continue
            else:
                r2 = (x0-xi)**2 + (y0-yi)**2
                fr = gravity/r2
                fx += fr*(xi-x0)/r2**0.5
                fy += fr*(yi-y0)/r2**0.5
        fsx.append(fx)
        fsy.append(fy)
    return fsx, fsy

# integriraj
def integrate(x, y, u, v):
    xt = np.zeros((numsteps, nbodies))
    yt = np.zeros((numsteps, nbodies))
    ut = np.zeros((numsteps, nbodies))
    vt = np.zeros((numsteps, nbodies))
    for step in range(numsteps):
        xt[step] = x
        yt[step] = y
        ut[step] = u
        vt[step] = v
        fsx, fsy = forces_calc(x, y)
        for i in range(nbodies):
            x0 = x[i]
            y0 = y[i]
            u0 = u[i]
            v0 = v[i]
            ui = u0 + fsx[i]*timestep
            vi = v0 + fsy[i]*timestep
            xi = x0 + ui + fsx[i]/2*timestep**2
            yi = y0 + vi + fsy[i]/2*timestep**2
            x[i] = xi
            y[i] = yi
            u[i] = ui
            v[i] = vi
    return xt, yt, ut, vt

# definiraj sistem i integriraj
if __name__ == "__main__":
    x = [ random.random()*lenscale for i in range(nbodies) ]
    y = [ random.random()*lenscale for i in range(nbodies) ]
    u = [ random.random()*velscale for i in range(nbodies) ]
    v = [ random.random()*velscale for i in range(nbodies) ]
    xt, yt, ut, vt = integrate(x, y, u, v)
    plt.plot(xt, yt)
    plt.savefig('nbody.png')
