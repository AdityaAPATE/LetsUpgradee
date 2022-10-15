# importing libraries
import numpy as np

# sort along the first axis
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a)        
print ("Along first axis : \n", arr1)        
  
  
# sort along the last axis
a = np.array([[10, 15], [12, 1]])
arr2 = np.sort(a, axis = -1)        
print ("\nAlong first axis : \n", arr2)
  
  
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = None)        
print ("\nAlong none axis : \n", arr1)

arr = np.arange(3 * 4 * 4).reshape(3, 4, 4)
  
print("Original 3d array:\n", 
      arr)
  
# Create 2D diagonal array
diag_arr = np.diagonal(arr, 
                       axis1 = 1,
                       axis2 = 2)
  
print("2d diagonal array:\n", 
      diag_arr)