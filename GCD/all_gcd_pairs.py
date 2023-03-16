'''
Given an array of integers A of size N containing GCD of every possible pair of elements of another array
Find and return the original numbers used to calculate the GCD array in any order. For example, 
if original numbers are {2, 8, 10} then the given array will be {2, 2, 2, 2, 8, 2, 2, 2, 10}.   
'''

from math import sqrt

def gcd(a,b):
    if b==0:
        return a
    if b>a:
        a,b = b,a
    return gcd(b,a%b)
def solve(A):
    n=len(A)
    A.sort(reverse = True)
    freq = {}
    for i in A:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    brr = [0 for i in range(len(A))]
    l = 0
    for i in range(n):
        if (freq[A[i]] > 0):
            brr[l] = A[i]
            freq[brr[l]] -= 1
            l += 1
            for j in range(l):
                if (j < i):
                    x = gcd(A[i], brr[j])
                    freq[x] -= 2
    size = int(sqrt(n))
    return brr[0:size]
A = [2, 2, 2, 2, 8, 2, 2, 2, 10]
print(solve(A))

'''
solution approach
1) find the frequency of elements present in A
2) sort A in descending order
3) The highest element is always present in original array. find gcd of highest element and second highest element. Reduce the frequency of the resultant gcd by 2  
'''
