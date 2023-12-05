# бинарный поиск
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9,15,17,19]

print(binary_search(my_list, 14)) # => 1
#binary_search(my_list, -1) # => None

# git init 
# git add .
# git commit -m "dhskd"
# git push
# git branch 
# git checkout trd
# git pull origin main
