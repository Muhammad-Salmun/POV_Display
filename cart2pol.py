import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    rho = int(rho)
    phi = np.arctan2(y, x)
    phi = np.rad2deg(phi)
    phi = int(phi)
    print(rho, phi)
    return rho,phi
    

