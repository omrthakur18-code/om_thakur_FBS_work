# 1. to neglect positional parameter 
# 2. assign value to paarmeter in function call
# 3.flow from right to left
# 4. name of parameter in function call and function defination should be same

def emp(id,name,sal,dept):
    data='ID: '+str(id)+'\n'
    data+='NAME: '+name+'\n'
    data+='SALARY: '+str(sal)+'\n'
    data+='DEPATMENT: '+dept+'\n'
    return data

res=emp(name='abc',id=101,dept='IT',sal=20000)
print(res)
