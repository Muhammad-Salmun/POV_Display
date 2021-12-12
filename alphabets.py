import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    phi = np.rad2deg(phi)
    print(rho, phi)

cart2pol(-5,-5)
