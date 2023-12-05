# x = [-1000,4,-2,-1,-8,-1000]
# c = 0
# for i in range(len(x)): 
#     if x[c] < x[i]:
#         c = i
               
# print(c, x[c])
        
#minio

# two max number O(n)
x = [-1000,44,-2,-1,-8,1001, 8, 3, 890, 1000, 2310, 77, -10000]
c = 1
e = 0
for i in range(len(x)):
    if x[i] > x[c]:
        e,c = c,i
    elif x[i] > x[e] and x[i] != x[c]:    
        e = i
   
print(x[c], x[e])        
    
# two min number O(n)   
# x = [-1000,44,-2,-1,-8,1001, 8, 3, 890, 1000, 2310, 77, -10000]
# c = 1
# e = 0
# for i in range(len(x)):
#     if x[i] < x[c]:
#         e,c = c,i
#     elif x[i] < x[e] and x[i] != x[c]:    
#         e = i
   
# print(x[c], x[e]) 
print(1, 2, 3)
    
    
    
