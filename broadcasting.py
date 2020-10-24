import numpy as np

A=np.array([[56.00,20.00,5.00,12.00],[50.00,34.00,2.00,18.9],[2.50,7.60,21.00,4.00]])
c = A.sum(axis=0)
print(c)

d = 100*(A/c.reshape(1,4))
print(d)

print(d.sum(axis=0))

x = np.random.rand(3,4)
y = np.random.rand(3,1)
 
print((x.T,y))

print(x+y)

#Do not use the following to create single dimensions array, this creates a single rank array
t = np.random.rand(5)
print(np.dot(t,t.T))#Gives inner product

#Instead use this
t = np.random.rand(5,1)
print(np.dot(t,t.T))#Gives outer product