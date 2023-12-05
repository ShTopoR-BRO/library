# сортировка списка
# x = [100, 44, -2, -1, -8, 1001, 8, 3, 890, 1000, 2310, 77, -10000]
# for j in range(len(x)):
#     min_ = j
#     for i in range(j, len(x)):
#         if x[i] < x[min_]:
#             min_ = i
    # x[j], x[min_] = x[min_], x[j]

# print(x)    

# сортировка пузырьком
# x = [100, 44, -2, -1, -8, 1001]
# flag = True
# while flag:
#     flag = False
#     for i in range(len(x)-1):
#         if x[i] > x[i +1]:
#             x[i], x[i + 1] = x[i + 1], x[i]
#             flag = True
#             print(x)    
            

# matri =[[1,5,3],
#         [4,2,8],
#         [6,3,2]]

# s = 0
# for i in range(len(matri)):
#     s += matri[i][i]
   
# print(s)

# x = [1,3,1,3,2,5,5,6,7,7,6, 4]
# count = {}
# for i in x:
#     if i not in count:
#         count[i] = 0
#     count[i] += 1
# for key, value in count.items():    
#     if value == 1:
#         print(key)

# найти индексы 2 чисел сумма которых = n     
# n = 30
# x = [1,4,5,7,12,16,18,21,32,34]
# c = 0
# while x[c] != x[-1]:
#     for i in range(len(x)):
#         if x[c] + x[i] == n:
#             print(x[c], x[i], "indexes :", c, i)
#     c += 1    

# left = 0
# right = len(x) - 1
# while left != right:
#     if x[left] + x[right] > n:
#         right -= 1
#     elif x[left] + x[right] < n:
#         left += 1
#     else:
#         print(left,right)
#         break         
    
# n = 30
# x = [1,4,5,7,12,16,18, 2, 43, 21,32,34]    
# slov = {}
# for i in range(len(x)):
#     if n - x[i] not in slov:
#         slov[x[i]] = i    
#     else:
#         print(i, slov[n-x[i]])    

x = [1,4,6,8]

for i in range(len(x)-1):
    
    for j in range(i+1,len(x)):
        print(x[i],x[j])  
    
