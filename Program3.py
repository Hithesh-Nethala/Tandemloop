n=int(input())

if n%2==0:
    limit=(n*2)-2
else:
    limit=(n*2)-1
for i in range(1,limit+1):
    if(i%2!=0):
        print(i)