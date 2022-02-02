import math
number=1
total_sum=0
while number<=11:
    remain=number
    if number%2!=0:
        sum=0
        power=int(math.log10(number))
        while power>=0:
            new_number=remain//(10**power)
            remain=remain-new_number*(10**power)
            sum=sum+new_number
            power=power-1
        total_sum=total_sum+number
    number=number+1
print(total_sum)