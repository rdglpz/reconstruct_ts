import numpy as np


def generateLorenz(npoints=10000,dt=0.02,s=10, r=28, b=2.667):
    
    def lorenz(x, y, z, s=s, r=r, b=b):
        x_dot = s*(y - x)
        y_dot = r*x - y - x*z
        z_dot = x*y - b*z
        return x_dot,y_dot,z_dot
    

    stepCnt = npoints

    # Need one more for the initial values
    xs = np.empty((stepCnt ,))
    ys = np.empty((stepCnt ,))
    zs = np.empty((stepCnt ,))

    # Setting initial values
    xs[0], ys[0], zs[0] = (0., 1., 1.05)

    # Stepping through "time".
    for i in range(0,stepCnt-10):
        # Derivatives of the X, Y, Z state
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt)+np.random.normal(0,0.0)
        ys[i + 1] = ys[i] + (y_dot * dt)+np.random.normal(0,0.0)
        zs[i + 1] = zs[i] + (z_dot * dt)+np.random.normal(0,0.0)
        
    return xs

def generateMackey(npoints=10000,gamma=1, beta=2, tau=2, n = 9.65):
    
    def mackey(x, gamma, beta, tau, n):
        x_dot = (beta*(x)/(1+x**n))-gamma*x
        return x_dot
    
    dt = 0.01
    stepCnt = npoints

    # Need one more for the initial values
    xs = np.empty((stepCnt ,))
    ys = np.empty((stepCnt ,))
    zs = np.empty((stepCnt ,))

    # Setting initial values
    xs[0]= (1)

    # Stepping through "time".
    for i in range(0,stepCnt-10):
        # Derivatives of the X, Y, Z state
        x_dot = mackey(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + (x_dot * dt)+np.random.normal(0,0.0)
 #       ys[i + 1] = ys[i] + (y_dot * dt)+np.random.normal(0,0.0)
  #      zs[i + 1] = zs[i] + (z_dot * dt)+np.random.normal(0,0.0)
        
    return xs
