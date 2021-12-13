import math
import numpy as np
from cart2pol import cart2pol

collisionPoints = []

class circles:
        def __init__(self, p, r):
                self.p = np.array(p)
                self.r = r

class lines:
        def __init__(self, point1, point2):
                self.point1 = np.array(point1)
                self.point2 = np.array(point2)


def Collision(circle, line):

        Q = circle.p            # Centre of circle
        r = circle.r            # Radius of circle
        P1 = line.point1        # Start of line segment
        P2 = line.point2        # End of line segment
        V = line.point2 - P1    # Vector along line segment

                                #coefficients of quadratic equation
        a = V.dot(V)
        b = 2 * V.dot(P1 - Q)
        c = P1.dot(P1) + Q.dot(Q) - 2 * P1.dot(Q) - r**2

        disc = b**2 - 4 * a * c #calculating discriminant
        
        if disc < 0:                                                    #collides in 3D sapce only
                return 0,0

        else:
                if disc==0:                                             #condition for one collision point                        
                        t2 = t1 = (-b) / (2 * a)                        #to avoid error in future while checking for t2
                        print(t1)                
                
                elif disc > 0:                                          #condition for two collision point   
                        sqrt_disc = math.sqrt(disc)
                        t1 = (-b + sqrt_disc) / (2 * a)
                        t2 = (-b - sqrt_disc) / (2 * a)

                if not (0 <= t1 <= 1 or 0 <= t2 <= 1):                  #conditions for collision
                        print('does not collide')
                        return 0,0
                
                else:
                        x1 = P1 + t1*(P2-P1)
                        x1 = x1.tolist()                                #converts num array or vector array to list
                        point1InCartesian = cart2pol(x1[0],x1[1])       #converts coodinates of point vector x1 to cartesian 
                        x2 = P1 + t2*(P2-P1)
                        x2 = x2.tolist()                                #converts num array or vector array to list
                        point2InCartesian = cart2pol(x2[0],x2[1])       #converts coodinates of point vector x1 to cartesian
                        print('x1 is {0} and x2 is {1}'.format(x1,x2))  
                        return point1InCartesian,point2InCartesian


def allCollisionPoints(startPoint,endPoint,numOfLeds):
        for i in range(numOfLeds):
                collisionPoints.append(Collision(circles((0,0),i),lines(startPoint,endPoint)))
        print(collisionPoints)
        return collisionPoints
        

