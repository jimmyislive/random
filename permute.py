'''
find all permutations of a string...

solution via dynamic programming
'''

def permute(s, k, permuted=''):

    #if len(s) == 1:
    if len(permuted) == k:
        #print len(permuted)
        #print permuted + s
        print permuted
        return

    for i in range(len(s)):
        permute(s[:i] + s[i+1:], k, permuted + s[i])
        
if __name__ == '__main__':
    permute('dogs', 4)


