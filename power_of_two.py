#~/usr/bin/env python

'''
Determine if a number is a power of two.
'''

def main(number):
    num_of_ones_in_bin = 0
    while number:
        if (number & 1):
            num_of_ones_in_bin += 1

        if (num_of_ones_in_bin > 1):
            return False

        number = number >> 1

    if num_of_ones_in_bin:
        return True
    else:
        return False

if __name__ == '__main__':
    assert main(2) == True
    assert main(0) == False
    assert main(1) == True
    assert main(32) == True
    assert main(1024) == True
    assert main(256) == True
    assert main(10) == False
    assert main(236) == False
    assert main(85) == False
    assert main(1056) == False


