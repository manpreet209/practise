class Vehicle:
    def __del__(self):
        print("Vehicle object destroyed")
        print(10/0)
v = Vehicle()
del v

#Vehicle object destroyed
#Exception ignored in: <function Vehicle.__del__ at 0x000001F208B98AF0>
#Traceback (most recent call last):
#  C:\Users\MANPREET\Desktop\assignment no 4
#    print(10/0)
#ZeroDivisionError: division by zero
