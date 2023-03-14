#### Brute Force ####

# A = [1,5,5,5,5,7]
# k=10
# count = 0
# i=0
# while i < len(A):
#     j=i+1
#     while j<len(A):
#         if A[i]+A[j] == k:
#             count+=1
#         j+=1
#     i+=1
# print(count)

#### Optimized ####
    

A = [1,5,5,5,5,7]
count = 0
k=10
dict = {}
i=0
while i<len(A):
    if k-A[i] in dict:
        count+= dict[k-A[i]
    
    if A[i] in dict:
        dict[A[i]] += 1
    else:
        dict[A[i]] = 1
    print(dict)
    i+=1
print(count)