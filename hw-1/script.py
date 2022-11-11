import math
import numpy as np


def share_bread(n, k):
    return math.floor(k/n), math.fmod(k, n)


assert share_bread(n=3, k=14) == (4, 2)


# -----------------------------------------------


def leap_year(year):
    # your code here
    result = 'YOU SHALL NOT PASS'
    if (math.fmod(year, 4) == 0 and math.fmod(year, 100) != 0) or math.fmod(year, 400) == 0:
        result = 'YOU SHALL PASS'
    return result


assert leap_year(5) == 'YOU SHALL NOT PASS'


# -----------------------------------------------


def amulet_area(a, b, c):
    p = (a + b + c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))


assert amulet_area(3, 4, 5) == 6


# -----------------------------------------------


def cal_euclidean(a, b):
    if a.size != b.size:
        return
    result = 0
    for i in range(0, a.size):
        result += np.power(a[i]-b[i], 2)
    return np.sqrt(result)


def cal_manhattan(a, b):
    if a.size != b.size:
        return
    result = 0
    for i in range(0, a.size):
        result += np.abs(a[i]-b[i])
    return result


def cal_cosine(a, b):
    if a.size != b.size:
        return
    ab = 0
    ascalar = 0
    bscalar = 0
    for i in range(0, a.size):
        ab += a[i]*b[i]
        ascalar += np.power(a[i], 2)
        bscalar += np.power(b[i], 2)
    return 1 - ab/(np.sqrt(ascalar)*np.sqrt(bscalar))


a = np.random.randint(-10, 10, size=10)
b = np.random.randint(-10, 10, size=10)
print(cal_euclidean(a, b))
print(cal_manhattan(a, b))
print(cal_cosine(a, b))


print('-----------------------------------------------')


def convert(array):
    min_value = np.min(array)
    max_value = np.max(array)
    factor = 1 / (max_value - min_value)
    for i in range(0, array.size):
        array[i] = (array[i] - min_value) * factor
    return array


my_array = convert(np.random.rand(100))
print(np.max(my_array), np.min(my_array))
print(my_array)


print('-----------------------------------------------')


def find_min_column(array):
    shape = my_array.shape
    if len(shape) != 2 or shape[0] == 0 or shape[1] == 0:
        raise Exception("Incorrect array dimensions")
    min_value = array[0][0]
    min_j = 0
    result = [0]*shape[0]
    for i in range(0, shape[0]):
        for j in range(0, shape[1]):
            if array[i][j] < min_value:
                min_value = array[i][j]
                min_j = j
    for i in range(0, shape[0]):
        result[i] = array[i][min_j]
    return result


my_array = np.random.randint(50, size=(6, 5))
selected_column = find_min_column(my_array)
print('Shape: ', my_array.shape)
print('Array: \n', my_array)
print('Min values: ', np.min(my_array, axis=1))
print('Result: ', selected_column)


print('-----------------------------------------------')


def get_unique_rows(X):
    shape = X.shape
    if len(shape) != 2 or shape[0] == 0 or shape[1] < 2:
        raise Exception("Incorrect array dimensions")
    result = X.copy()
    unique = 0
    while unique < len(result):
        index = unique + 1
        while index < len(result):
            if np.array_equal(result[unique], result[index]):
                result = np.delete(result, index, 0)
            index += 1
        unique += 1
    return result


X = np.random.randint(4, 6, size=(10, 3))
print("Matrix: \n", X)
print("Result: \n", get_unique_rows(X))
