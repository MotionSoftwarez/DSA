from array import array
import numpy as np

if __name__ == '__main__':
    # array with array module
    my_array = array("i", [1, 2, 3, 4])
    print(my_array[2])

    # inserting value in array
    # first argument is index and second is value
    my_array.insert(0, 8)
    print(my_array)

    # deleting value in array
    # first argument is index and second is value
    my_array.remove(1)
    print(my_array)

    # appending a value in array at the end
    my_array.append(99)
    print(my_array)

    # traversal in an array
    for i in my_array:
        print(i)

    # array with numpy
    # my_num_array = np.array([["a", "b", "c"], ["1", "2", "3"]])
    # print(my_num_array[0, 1])
