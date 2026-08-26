# with passing parameter with returning value 

def addition(num1,num2):
    #sum=num1+num2
    #return sum
    return num1+num2

num1=int(input('enter number 1: '))
num2=int(input('enter number 2: '))
res=addition(num1, num2)

print('addition: ',res)