import numpy as np


##create a matrix 6*6 of no. upto 36
a = np.arange(1,37).reshape(6,6)

#print(a.sum(axis = 1)) ## axis = 1 for column and axis = 0 for rows
#x,y = a[2:4,:],a[:,2:4]
#print(x)
#print(y)
#print (np.array(a[2:4, 2:4]))
#print(np.array(a[4:, :]))      ## for last two rows of matrix
#print(np.array(a[0][0]))      ##for first element in matrix
###or
#print(np.array(a.item(0)))    ## for first element in matrix
print(np.array(a))

######create an array of 20 times of value 7
###a = np.empty((4,5),7)
#a = np.full((4,5),7)
#print(a)


## 2 dim matrix using func zeros and random
#a = np.zeros((2,2))
#print(a)
#a = np.random.random((3,2))
#print(a)
#print(a.ndim)

##creating one dim array using arange and rand
#a = np.arange(6)
#print(a)
#b = np.random.rand(4)
#print(b)

## creating a matrix
#a = np.array([('a','b'),('c','d'),(3,3)])
#print(a.dtype)
#a = np.matrix('1,2;3,4')
#print(a)
#print(a.size)
#print(a.shape)
#print(a.ndim)
#print(a)


###matrix operations
#a = np.array([[1,2],[3,4]])
#b = np.array([[7,8],[9,10]])
#c = np.dot(a,b)
#print(c)

#print(a@a)



#first_array = [1,22.4,5,35,4,6.7,3,8,40]
#print(np.dtype (int))
#print(np.size(first_array))
##2###
#print(np.shape(first_array))

## first ###
#first_array  = [1,22.4,5,35,4,6.7,3,8,40]
#print(np.ndim(first_array))
#print(np.array(first_array))
