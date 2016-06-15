T = int(input())
N = []
map_N = {}
for i in range(T):
    map_N[i] = 

def reverse(n):
    return int(str(num)[::-1])
    
def all_digits_are_odd(sum):
    while(sum != 0):
        if (sum % 10) % 2 == 0:
            return False
        else:
            sum = (sum - sum%10) / 10
    return True

for max_num in N:
    counter = 0
    for num in range(max_num):
        reversed_num = reverse(num)
        if (num % 10) != 0:
            if all_digits_are_odd(num + reversed_num):
                counter+=1
    print(counter)


