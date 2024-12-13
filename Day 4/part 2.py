import re

with open("Data.txt") as f:
    data=f.read()
    data=data.split('\n')

data=[list(j) for j in data]

count=0
pattern='((MAS)|(SAM))((MS)|(SM))'


for i in range(len(data)-2): # to prevent out of index error.
    for j in range(len(data[0])-2):# to prevent out of index error.
        diag=''.join([data[i+k][j+k] for k in range(3)])
        diag=diag+data[i+2][j]+data[i][j+2]
        if re.match(pattern,diag):
            count+=1
print(count)