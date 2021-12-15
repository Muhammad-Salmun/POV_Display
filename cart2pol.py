import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    rho = int(rho)
    theta = np.arctan2(y, x)
    theta = np.rad2deg(theta)
    theta = int(theta)
    print(rho, theta)
    return rho,theta
    

