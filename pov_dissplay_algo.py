import math
import numpy as np

def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi)

def led_state_data(x1,y1,x2,y2,num_of_leds):
        
        #values for easy calc
        X = x2 - x1
        Y = y2 - y1
        m = Y/X if X != 0 else 1
        y_intercept = y1 - x1*(Y/X) if X != 0 else 0
        a = 1 + m**2
        b = 2*m*y_intercept
        print(X,Y,a,b)

        data = []


        #calculating the determinant for each radii to find the leds affected by the line
        for i in range(num_of_leds):
                c = y_intercept**2 - i**2
                D = b**2 - 4*a*c
                print('c,D is {0},{1}'.format(c,D))
                
                #for two roots or two intersection points
                if D > 0:
                        xn1 = -b-math.sqrt(D)/(2*a)
                        xn2 = -b+math.sqrt(D)/(2*a)

                        yn1 = m*x1 + y_intercept
                        yn2 = m*x2 + y_intercept
                        
                        print('(xn1,yn1,radius)')
                        print(xn1,yn1,i)
                        print(xn2,yn2)

                        r1,theta1 = cart2pol(xn1,yn1)
                        theta1 = np.rad2deg(theta1)
                        if theta1 < 0:
                                theta1 = 360-theta1
                        print('radius and angle are: {0} and {1}'.format(r1,theta1))
                        r2,theta2 = cart2pol(xn2,yn2)
                        theta2 = np.rad2deg(theta2)
                        if theta1 < 0:
                                theta2 = 360-theta2
                        print('radius and angle are: {0} and {1}'.format(r2,theta2))

                        data.append((int(r1),int(theta1)))
                        data.append((int(r2),int(theta2)))
                
                #for tangential line
                elif D == 0:
                        xn1 = -b-math.sqrt(D)/(2*a)
                        yn1 = i**2 - xn1**2
                        r1,theta1 = cart2pol(xn1,yn1)
                        theta1 = np.rad2deg(theta1)
                        if theta1 < 0:
                                theta1 = 360-theta1
                        print('radius and angle are: {0} and {1}'.format(r1,theta1))                        
                        data.append((int(r1),int(theta1)))

        print(data)
        return data                        

