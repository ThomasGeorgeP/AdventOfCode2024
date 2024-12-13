with open('data.txt','r') as f:
    data=f.read()

data=data.split('\n')
data=[[int(j) for j in i.split()] for i in data]

safe=0
for k in data:

    i=k.copy()
    
    if i==sorted(i) or i==sorted(i,reverse=True):
        for j in range(len(i)-1):
            if abs(i[j]-i[j+1])>3 or abs(i[j]-i[j+1])<1:
                break
        else:
            safe+=1
            
print(safe)