import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6]])

new_arr_2d = np.insert(arr_2d,1,[7,8,9],axis=0)
print(new_arr_2d)