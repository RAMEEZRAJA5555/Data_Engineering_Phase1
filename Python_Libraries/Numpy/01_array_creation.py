import numpy as np

                                  #Array Creation Methods
                                  #This file demonstrates different ways to create NumPy arrays.


                                  #1. Create an array from a Python list
a1 = np.array([1, 2, 3, 4, 5])
print("np.array():")
print(a1)


                                   #2. Create an array filled with zeros
                                   #(3, 4) means 3 rows and 4 columns

a2 = np.zeros((3, 4))
print("\nnp.zeros():")
print(a2)


                                     #3. Create an array filled with ones
                                    #dtype=np.int32 makes the values 32-bit integers
a3 = np.ones((2, 3), dtype=np.int32) #it meand make matrix with all 1 values,with 2 rows and 3 colums
print("\nnp.ones():")
print(a3)


                                     #4. Create a sequence using start, stop, and step
                                     #20 is not included
a4 = np.arange(0, 20, 2)
print("\nnp.arange():")
print(a4)


                                        #5. Create evenly spaced values
                                       #Create 5 values from 0 to 1
a5 = np.linspace(0, 1, 5)
print("\nnp.linspace():")
print(a5)


                                         #6. Create a 3x3 identity matrix
a6 = np.eye(3)
print("\nnp.eye():")
print(a6)


                                      #7. Create random values between 0 and 1 and write in the form of 2 rows and 4 colms matrix
a7 = np.random.rand(2, 4)         #(2,4) means 2 rows and 4 colums 
print("\nnp.random.rand():")
print(a7)