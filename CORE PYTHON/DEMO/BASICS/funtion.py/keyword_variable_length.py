# 1.to pass multiple value with meaning to function
# 2.mention 2 asterisk(**) symbols before parameter name in function defination
# 3.data stored in dictionary format
# 4.use for loop on dict.items() to accesss indivituality


def emp(**data):
    for key,val in data.items():
        print(key,':',val)

emp(id=101,name='om',age=21,add='amravati')