'''
Given an array with integers, with each integer being at most n positions away 
from its final position, what would be the best sorting algorithm?

so theoretically, if k is much smaller than log(n) this will give better performance that nlogn - ? (maybe...)
'''


def main(arr, k):

    max_len = len(arr)
    for i in range(max_len):
        #first look left
        current = i
        for j in range(1,k + 1):
            if current - j >= 0 and arr[current] < arr[current - j]:
                #swap them
                arr[current], arr[current - j] = arr[current - j], arr[current]

        #now look right
        for j in range(1,k + 1):
            if current + j <= (len(arr) - 1) and arr[current] > arr[current + j]:
                #swap them
                arr[current], arr[current + j] = arr[current + j], arr[current]

    return arr

if __name__ == '__main__':
    assert main([1,8,6,9,3,5,7], 4) == [1, 3, 5, 6, 7, 8, 9]
    assert main([5,1,4,2,8], 3) == [1, 2, 4, 5, 8]
    #look, works with duplicates too !
    assert main([116, 14, 130, 67, 31, 22, 69, 22, 78, 19, 167, 57, 63, 2, 95, 16, 36, 23, 110, 183], 15) == [2, 14, 16, 19, 22, 22, 23, 31, 36, 57, 63, 67, 69, 78, 95, 110, 116, 130, 167, 183]
