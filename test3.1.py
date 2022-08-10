class Complex:
    x = int(input("enter real part for no1: "))
    y = int(input("enter imaginary part for no1: "))
    z = complex(x,y)
    p = int(input("enter real part for no2: "))
    q = int(input("enter imaginary part for no2: "))
    r = complex(p,q)
    print("first no is:",z)
    print("second no is:",r)

    def add(self):
        t = self.z+self.r
        print("Sum:",t)
        return t

    def diff(self):
        i = self.z-self.r
        print("Difference:",i)
        return i

    def  prod(self):
        l =self.z*self.r
        print("Product:",l)
        return l

ob1 = Complex()

ob1.add()
ob1.diff()
ob1.prod()