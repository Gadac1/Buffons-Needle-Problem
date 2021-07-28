import numpy as np
import random as rd
import math as m

gridsize = 1000
sticklength = 5
stripsize = 10

def drop_stick():
    xa = rd.random()*1000
    ya = rd.random()*1000

    theta = rd.random()*2*np.pi
    xb = xa + sticklength * np.cos(theta)
    yb = ya + sticklength * np.sin(theta)

    return [(xa,ya), (xb,yb)]
    
def strip_cross(coord):
    xa_d=m.floor((coord[0][0]/10))
    xb_d=m.floor((coord[1][0]/10))

    if xa_d == xb_d:
        return False
    else:
        return True

def buffon_needle(n):
    p = 0
    for i in range(n):
        if strip_cross(drop_stick()):
            p+=1
    
    p = p/n
    return(print((2 * sticklength)/(stripsize * p)))

buffon_needle(100000)

    


