import numpy as np

## first ###
#first_array  = [1,22.4,5,35,4,6.7,3,8,40]
#print(np.ndim(first_array))
#print(np.array(first_array))

#first_array = [1,22.4,5,35,4,6.7,3,8,40]
#print(np.dtype (int))
#print(np.size(first_array))

#print(np.shape(first_array))


##second ###
## creating a matrix
#a = np.array([('a','b'),('c','d'),(3,3)])

#print(a)
#print(a.ndim)
#print(a.size)
#print(a.shape)
#print(a.dtype)

##Third

##creating one dim array using arange and rand
#a = np.arange(6)
#print(a)
#b = np.random.rand(4)
#print(b)

## 4. 2 dim matrix using func zeros and random
#a = np.zeros((2,2))
#print(a)
#a = np.random.random((2,2))
#print(a)
#print(a.ndim)

## 5.######create an array of 20 times of value 7
###a = np.empty((4,5),7)
#a = np.full((4,5),7)
#print(a)

##6 .##Create a 6 x 6 matrix with all numbers up to 36, then print
##create a matrix 6*6 of no. upto 36
a = np.arange(1,37).reshape(6,6)
##
#print(a)

####only the first element on it
#print(np.array(a[0][0]))      ##for first element in matrix
###or
#print(np.array(a.item(0)))    ## for first element in matrix
#print(np.array(a))

##only the last 2 rows for it
#print(np.array(a[4:, :]))      ## for last two rows of matrix

###only the two mid columns and 2 mid rows for it

#x,y = a[2:4,:],a[:,2:4]
#print(x)
#print(y)

##the sum of values for each column

#print(a.sum(axis = 1)) ## axis = 1 for column and axis = 0 for rows



