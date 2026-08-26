# 1.to pass multiple values to the function
# 2.mention asterisk(*) symbol before parameter name in function defination
# 3.values stored in tuple format
# 4. use for loop to aceess values indivitually



def add(*num):
    sum=0
    for val in num:
    
        sum+=val

    return sum

res=add(10,20,30,40)
print('addition: ',res)

