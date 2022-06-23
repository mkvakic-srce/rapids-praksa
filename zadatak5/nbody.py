import math
import random
import pickle

# seed
random.seed(69)

# konstante
nbodies = 10
gravity  = 6.67e-11
masscale = 6e25
lenscale = 150e9
velscale = 0*30e3
timestep = 3600
numsteps = 2

# izracunaj sile
def forces(*args):
    fxout, fyout = [], []
    for i, (xi, yi, mi) in enumerate(zip(*args)):
        fx, fy = 0, 0
        for j, (xj, yj, mj) in enumerate(zip(*args)):
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

# integriraj
def integrate(*args):
    xout, yout, uout, vout = [], [], [], []
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
    xout = x[:]
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
    xout = [ x for x in xout if x is not math.nan ]
    yout = [ y for y in yout if y is not math.nan ]
    uout = [ u for u in uout if u is not math.nan ]
    vout = [ v for v in vout if v is not math.nan ]
    mout = [ m for m in mout if m is not math.nan ]
    return xout, yout, uout, vout, mout

if __name__ == "__main__":

    # definiraj sistem
    x = [ random.uniform(-1, 1)*lenscale for i in range(nbodies) ]
    y = [ random.uniform(-1, 1)*lenscale for i in range(nbodies) ]
    u = [ random.uniform(-1, 1)*velscale for i in range(nbodies) ]
    v = [ random.uniform(-1, 1)*velscale for i in range(nbodies) ]
    m = [ masscale for i in range(nbodies) ]

    # simuliraj
    xt, yt = [], []
    for i in range(numsteps):

        # izračunaj sile
        fx, fy = forces(x, y, m)

        # integriraj
        x, y, u, v = integrate(x, y, u, v, m, fx, fy)

        # ograniči
        x, y = limit(x, y)

        # sudari
        x, y, u, v, m = collisions(x, y, u, v, m)

        # dodaj u vremenski slijed
        if (i*timestep)%(24*3600) == 0:
            print('%6i / %6i' % (i*timestep/3600, numsteps*timestep/3600))
            xt.append(x)
            yt.append(y)

    print(x)
    # print(y)
    
    # ispiši
    with open('nbody.xt', 'wb') as f:
        pickle.dump(xt, f)
        f.close()

    with open('nbody.yt', 'wb') as f:
        pickle.dump(yt, f)
        f.close()