import numpy

def arrays(arr):
    x = numpy.array(arr, float)
    return numpy.flip(x)

arr = input().strip('')

result = arrays(arr)

print(result)