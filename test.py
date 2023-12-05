import time 


# def decor(func):
#     def wrapper(*args, **kwargs):
#         print("test start", time.time())
#         start = time.time()
#         func(*args,**kwargs)
#         stop = time.time()
#         print("test stop", time.time(), "time of operation", stop - start)
#     return wrapper



# @decor
# def schet(chislo):    
#     for i in range(2, (chislo // 2) + 1):
#         if chislo % i == 0:
#             print(i)
            
            
 

#git add .
#git commit -m " aldsjvnfd"
#git push
#git branch 
#git branch "1"
#git checkout "1"
#git checkout main
#git clone 
#git pull origin
           



#schet(int(input()))            


# def decor(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args)
#         except ZeroDivisionError:
#             return "DIVIZION ERROR!!!"     
#         except TypeError:
#             return "TYPE ERROR!!!"
#         finally:
#             print("не печалься")
#     return wrapper

# @decor
# def clone(x):
#     return 100/x

# print(clone(4))
   

# from abc import ABC, abstractmethod
   
# class Ubstract(ABC):
#     @abstractmethod
#     def say(self):
#         pass
#     @abstractmethod
#     def goto(self):
#         pass
    
# class Man(Ubstract):
#     def say(self):
#         print("hello")
#     def goto(self):
#         x = -100
#         for i in range(1,x + 1, -1):
#             try:
#                 if i % 2 == 0:
#                     print("прошел четное колличество метров")   
#             except:
#                 if i % 2 != 0:
#                     print("прошел нечетное число метров")
                          
         
# Ivan = Man()
# Ivan.say()
# Ivan.goto()

            
# fibonachy = int(input())
# f1 = 1
# f2 = 1
# for i in range(1, fibonachy + 1):
#     f1, f2 = f2, f1 + f2    
#     print(f1)
    
def mirror():    
    s = input()
    print(s)   

mirror()