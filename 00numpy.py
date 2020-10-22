#Prerequisite 1- Numpy
#Aaklit
import numpy as np
#1. Lists Without Numpy
basic_list = [0,1,2,3,4]
print(basic_list)
print(basic_list[1]) #Print the second element of the list

basic_list_of_lists = [ [1,2,3,4], [5,6,7,8], [9,10,11,12] ]
print("first row:", basic_list_of_lists[0])
print("third row:", basic_list_of_lists[2])
print("whole list:", basic_list_of_lists)
print(type(basic_list_of_lists))

#2. Arrays (importing what we did before but now as an array)
arr1= np.array(basic_list_of_lists)
print(arr1)
print(type(arr1))
#basically stored as a matrix so now i can get individual elements like
print("first row, first column:", arr1[0,0])
print("first row, second column:", arr1[0,1])
print("first row, third column:", arr1[0,2])
print("first row, fourth column:", arr1[0,3])
print("the first row:", arr1[0,:])

#2b. Multidimensional Arrays
my_two_d_array = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
for row in my_two_d_array:
    print("starting new row:")
    for element in row:
        print(element)
#reshaping arrays
arr = np.array([
    [1,2,3],
    [4,5,6]
])
print(np.shape(arr))
reshaped_arr = arr.reshape(3,2)
print(reshaped_arr)
print(np.shape(reshaped_arr)) #Reshape from (2,3) to (3,2) successful


#Using all this to build an array with specified number of rows, columns and a range of numbers
def construction_arr(low,high, n_rows, n_cols):
    basic_range=np.arange(low,high,1)
    perfect = basic_range.reshape(n_rows, n_cols)
    return perfect
construction_arr(1,11,5,2) #remember the high value does not get included so if you want the array to have 5 rows and 2 columns, hence obviously 10 elements and you start at 1, go till 11 and not 10.


#3. Tuples
#Same as lists but immutable - contents cant be changed
#Used in numpy
my_tuple = (1,2,3)
print(type(my_tuple))
print(np.exp(my_tuple)) #print e to the power of elements from the my_tuple tuple
#Constructing arrays
three_zeros = np.zeros(3)
print("print three zeroes", three_zeros)
five_by_six = np.zeros((5,6))
print(five_by_six)
range_arr = np.arange(0,20,2)
print("Print a range", range_arr)

#np.mean() #To take a mean
#np.min()

#Dataframes converted to lists or arrays, generally arrays
