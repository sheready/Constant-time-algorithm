import time

#create a function to return first number in an array

def first_number(array):
  return array[0]

#run time for array where n = 10
start = time.time()
first_number([85,49,14,11,33,94,30,20,25,33])
print("Execution time for 1st array: {}".format(time.time() - start))

# run time for array where n = 25
start = time.time()
first_number([92,14,67,52,77,65,88,27,84,94,35,70,89,80,35,55,74,32,25,6,17,25,70,72,14])
print("Execution time for 2nd array: {}".format(time.time() - start))