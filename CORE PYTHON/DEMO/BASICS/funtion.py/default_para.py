# to make parameter optional
# assign value to parameter in function defination
# if we pass value to default parameter it takes passed value 
# if we dont pass value to default parameter it takes default value 
# flow from right to left
# flow from right to left because of positinal parameter concept

def emp(id,name=None,sal=20000,dept='it'):
    print('id: ',id)
    print('name: ',name)
    print('salary: ',sal)
    print('department: ',dept)


emp(101,'om',50000,'da')
print('       ')
emp(102,'jayant')