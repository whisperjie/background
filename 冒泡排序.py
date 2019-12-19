a=int(input())
linqian=[100,25,10,5,1]
b=[]
def greet(a):
    for i in range(len(linqian)):
        if a//linqian[i]>0:
            b.append(linqian[i])
            a=a-linqian[i]
            greet(a)
   

greet(a)
print(str(b))