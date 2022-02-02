import math
number=int(input())
remain=number
sum=0
if number%2!=0:
    power=int(math.log10(number))
    while power>=0:
        new_number=remain//(10**power)
        remain=remain-new_number*(10**power)
        sum=sum+new_number
        power=power-1
print(sum)
