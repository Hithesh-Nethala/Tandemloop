n=[1,2,8,9,12,46,76,82,15,20,30]
# Can get from user input
dict1={}

for i in range(1,10):
    count=0
    for j in n:
        if(j%i==0):
            count+=1
        else:
            continue
    dict1[i]=count
print(dict1)