import numpy as np


def generateHenon(npoints=10000,a=1.4, b=0.3):
    
    def henon(x, y, a,b):
        return y + 1.0 - a *x*x, b * x
#    def HenonMap(x,y):
#        return y + 1.0 - a *x*x, b * x
    
    # Map dependent parameters
    a = 1.4
    b = 0.3
    iterates = 100000

    # Initial Condition
    xtemp = 0.1
    ytemp = 0.3

    x = [xtemp]
    y = [ytemp]

    for n in xrange(0,iterates):
        xtemp, ytemp = HenonMap(a,b,xtemp,ytemp)
        x.append( xtemp )
        y.append( ytemp )
    
    return x