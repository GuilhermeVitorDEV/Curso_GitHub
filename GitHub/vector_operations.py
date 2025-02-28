import math as mt

class Vector:
    def __init__(self,x,y):
        self.x =  x
        self.y = y

    def __abs__(self):
        return mt.hypot(self.x,self.y)
    
