import math
import random

# seed
random.seed(69)

# konstante
nbodies = 10
gravity  = 6.671e-11
masscale = 6e29
lenscale = 150e9
velscale = 30e3
timestep = 3600
numsteps = 10

# izracunaj sile
def forces(x, y, m):
    fxout, fyout = [], []
    for i, (x0, y0) in enumerate(zip(x, y)):
        fx, fy = 0, 0
        for j, (xi, yi) in enumerate(zip(x, y)):
            if i == j:
                continue
            else:
                dx = xi-x0
                dy = yi-y0
                r2 = dx**2 + dy**2
                fr = gravity*m[i]*m[j]/( r2 + (lenscale/10)**2 )
                fx += fr*dx/r2**0.5
                fy += fr*dy/r2**0.5
        fxout.append(fx)
        fyout.append(fy)
    return fxout, fyout

# integriraj
def integrate(xin, yin, uin, vin, m, fx, fy):
    xout, yout, uout, vout = [], [], [], []
    for i, _ in enumerate(xin):
        x0, y0, u0, v0 = xin[i], yin[i], uin[i], vin[i]
        ui = u0 + fx[i]/m[i]*timestep
        vi = v0 + fy[i]/m[i]*timestep
        xi = x0 + u0*timestep
        yi = y0 + v0*timestep
        xout.append(xi)
        yout.append(yi)
        uout.append(ui)
        vout.append(vi)
    return xout, yout, uout, vout

# ograniči na domenu lenscale x lenscale
def limit(xin, yin):
    xout, yout = [], []
    for i, (x, y) in enumerate(zip(xin, yin)):
        if abs(x) > lenscale:
            x -= 2*x
        if abs(y) > lenscale:
            y -= 2*y
        xout.append(x)
        yout.append(y)
    return xout, yout

if __name__ == "__main__":

    # definiraj sistem
    x = [ random.uniform(-1, 1)*lenscale for i in range(nbodies) ]
    y = [ random.uniform(-1, 1)*lenscale for i in range(nbodies) ]
    u = [ random.uniform(-1, 1)*velscale for i in range(nbodies) ]
    v = [ random.uniform(-1, 1)*velscale for i in range(nbodies) ]
    m = [ masscale for i in range(nbodies) ]

    # simuliraj
    xt, yt, ut, vt = [], [], [], []
    for i in range(numsteps):

        # izračunaj sile
        fx, fy = forces(x, y, m)

        # integriraj
        x, y, u, v = integrate(x, y, u, v, m, fx, fy)

        # ograniči
        x, y = limit(x, y)

        # dodaj u vremenski slijed
        xt.append(x)
        yt.append(y)
        ut.append(u)
        vt.append(v)

    # ispiši
    with open('nbody.csv', 'w') as f:
        for i, (x, y, u, v) in enumerate(zip(xt, yt, ut, vt)):
            f.write('x, %i,' % i + ' %e,' * len(x) % tuple(x) + '\n')
            f.write('y, %i,' % i + ' %e,' * len(y) % tuple(y) + '\n')
            f.write('u, %i,' % i + ' %e,' * len(u) % tuple(u) + '\n')
            f.write('v, %i,' % i + ' %e,' * len(v) % tuple(v) + '\n')
        f.close()
