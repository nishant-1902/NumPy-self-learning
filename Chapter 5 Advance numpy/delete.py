# np.delete(array,index,axis=None)
import numpy as np

# arr = np.array([1,2,3,4,5,5])
# print(arr)
# new_arr = np.delete(arr,5)
# print(new_arr)


#  Dlete in 2D array

arr_2d = np.array([[1,2,3],[4,5,6]])

new_2d_arr = np.delete(arr_2d,0,axis=0)
print(new_2d_arr)