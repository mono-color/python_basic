import numpy as np
list1 = [1, 2, 3, 4]
print('list1:', list1)
print('list1:', type(list1))

array1 = np.array(list1)
print('array1:', array1)
print('array1:', type(array1))

print('데이터타입:', array1.dtype)
print('구조:', array1.shape)
print('차원:', array1.ndim)

arr2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])
print('차원:', arr2.ndim, arr2.shape, arr2.dtype)
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 5, 6]]])
print('차원:', arr3.ndim, arr3.shape, arr3.dtype)
arr4 = np.array([[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 5, 6]]], [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [3, 5, 6]]]])

#
test_arr = np.arange(10)  # 0~9
print('='*100)
print(test_arr)
print('2X5\n', test_arr.reshape(2, 5))
print('2X5\n', test_arr.reshape(5, 2))

