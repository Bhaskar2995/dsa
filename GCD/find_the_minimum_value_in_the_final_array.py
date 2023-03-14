''' Given N positive distinct elements in an array, choose arr[i] and arr[j], such that i!=j.
 if absolute value of arr[i] and arr[j] is not present keep repeating the steps until no more insertions are possible. 
 find the minimum value in the final array '''
 # Question explanation
''' if the given input is [6,2,12,8] then answer would be [6,2,12,8,4,10]
 now minimum value in the list is 2'''

def GCD(a,b):
    if b == 0:
        return a
    if b>a:
        a,b = b,a
    return GCD(b,a%b)

A = [6,2,12,8]
i=0
ans = GCD(A[i],A[i+1])
i=2
while i < len(A):
    ans = GCD(ans,A[i])
    i+=1
print(ans)

#Solution approach

''' 
If you find GCD of all the numbers then you will get the minimum number 
Time Complexity : O(nlogn)
Space Complexity : O(1)
'''

