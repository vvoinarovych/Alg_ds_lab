def recursion(n):
    if n==1:
        return 1
    else:
        return recursion(n-1)*n

def reverse_array(array):
    if len(array) == 0:
        return []
    else:
        return [array[-1]] + reverse_array(array[:-1])

array = [1,2,3,4,5]
array1 = [1,289,20,20,1]
print(recursion(5))
print(recursion(10))
print(reverse_array(array))
print(reverse_array(array1))

