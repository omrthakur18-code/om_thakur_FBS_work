#wap a program to calculate the percentage of stdents based on marks on any 5 subjcts

sub1=int(input('marks in english: '))
sub2=int(input('marks in maths: '))
sub3=int(input('marks in science: '))
sub4=int(input('marks in marathi: '))
sub5=int(input('marks in history: '))

per=(sub1+sub2+sub3+sub4+sub5)/500*100

# print('total percentage of student in exam is ',per,'%')

print(f'total percentage of student in exam is {per} %')