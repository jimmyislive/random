'''
find all permutations of a string...

solution via dynamic programming
'''

def permute(s, permuted=''):

    if len(s) == 1:
        print permuted + s
        return


    for i in range(len(s)):
        permute(s[:i] + s[i+1:], permuted + s[i])
        
if __name__ == '__main__':
    permute('dogs')


