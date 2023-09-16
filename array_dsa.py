from array import array
import numpy as np


def access_elements(arr_name, rindex, colindex):
    if rindex >= len(arr_name) or colindex >= len(arr_name[0]):
        print("Index out of bound\n enter correct number")
    else:
        return arr_name[rindex, colindex]


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

    # Two d aray
    td_array = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print(td_array)
    print("#####################")
    # Two d array deletion
    new_del_array=np.delete(td_array,1,axis=0)
    print(new_del_array)
    print("#####################")


    # insertion in 2 array
    final_2d_array = np.insert(td_array, 1, [6, 7, 8], 0)
    print(final_2d_array)
    print("*******************")
    #print(access_elements(final_2d_array, 1, 2))
    for i in range(len(final_2d_array)):
        for j in range(len(final_2d_array[0])):
            print(final_2d_array[i, j])



    # array with numpy
    # my_num_array = np.array([["a", "b", "c"], ["1", "2", "3"]])
    # print(my_num_array[0, 1])
