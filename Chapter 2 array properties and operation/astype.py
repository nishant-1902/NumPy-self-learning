# astype = change the datatype in array
# syntax = astype(new type)

import numpy as np
arr = np.array([1.2,3.2,3.4,4.5])
print(arr.dtype)
int_arr = arr.astype(int)

print(int_arr)
print(int_arr.dtype)