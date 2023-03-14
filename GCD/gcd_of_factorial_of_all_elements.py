### if A = [4,3,8,6] then find GCD of [24,6,40320,720] ###
### Answer is 6
def factorial(A):
    ans = 1
    while A > 1:
        ans = ans * A
        A -= 1
    return ans
def solve(A):
    min = float('inf')
    for i in A:
        if i < min:
            min = i
    return factorial(min)
     
A = [4,7,8,6]
result = solve(A)
print(result)

## Solution approach ##
''' we need to find the greater common divisor 
for input A = [4,3,8,6]
4! = 1 x 2 x 3 x 4
3! = 1 x 2 x 3
8! = 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8
6! = 1 x 2 x 3 x 4 x 5 x 6
So find the minimum number from the list and find the factorial of it that will be the answer. Here smallest number is 3 and factorial of 3 is '6'. 
Final answer is '6'     
Time complexity = O(n)
Space Complexity = O(1)
 '''

