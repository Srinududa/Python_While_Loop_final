a = 4
count=1
second=1
while count<=a:
    while second<=a:
        print("* "*second)
        second=second+1
    print("* "*count)
    count=count+1
result==>>
* 
* * 
* * * 
* * * * 
* 
* * 
* * * 
* * * * 


N = 5 3 6 2 8
total = 0
for i in range(N):
    num = float(input())
    total += num
average = total / N
print(average)

result==>>
4.0



N = 4
square = 0
sum = 0
counter = 1
while counter <= N:
    square = counter**2
    sum = sum + square
    counter += 1
print(sum)

result==>>
30



X = 4
N = 2
product = 1
i = 0
while i < N:
    product *= X+1
    X += 1
    i += 1
print(product)

result == >>
