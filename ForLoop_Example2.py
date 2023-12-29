'''
#Get input for a and b
#Print value between 8 and 15

a=int(input())
b=int(input())
for i in range(a+1,b):
    print(i)
'''
'''
#Print even number between 1 and 10

for i in range(1, 10):
    if(i%2==0):
        print(i)
'''

'''
#Count the number of odd numbers between 1 and 10
a=0
b=0
for i in range(1,10):
    if(i%2==0):
        a=a+1
    else:
        b=b+1
print("Even number total:",a, "Odd number total:",b )
'''

#Count the number which are divisble by 3 and 5 (Range 1 to 100)
count_num=0
for i in range(1,100):
    if(i%3==0 and i%5==0):
        count_num=count_num+1
print(count_num)
        


