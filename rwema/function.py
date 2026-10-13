def number(a,b):
    if (a>b):
        return a
    else:
        return b 
m=4
n=3
result= number(m,n)
print(result)

def summation(list):
    sum=0
    for i in list:
        sum+=i
    print(sum)

    
list_1=[8,2,3,0,7]
summation(list_1)

def multiple(num):
    sum=0
    limit=int(input("Enter the limit: "))
    for i in range(0,limit):
        if i%3==0 or i%5==0:
            sum+=i
        return sum
num=int(input("Enter the number: "))
result=multiple(num)
print(result)