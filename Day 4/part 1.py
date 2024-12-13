with open("Data.txt") as f:
    data=f.read()
    data=data.split('\n')
count=0

for i in data:
    count+=i.count('XMAS')+i.count('SAMX')

data_normal=[list(j) for j in data]

#transposing data to count vertically.

transposed=[''.join([i[index] for i in data]) for index in range(len(i))]
for i in transposed:
    count+=i.count('XMAS')+i.count('SAMX')

#for diagonal

for i in range(len(data)-3): # to prevent out of index error.
    for j in range(len(data[0])-3):# to prevent out of index error.
        diag=''.join([data[i+k][j+k] for k in range(4)])
        if diag=='XMAS' or diag=='SAMX':
            count+=1
for i in range(len(data)-1,2,-1):
    for j in range(len(data[0])-3):# to prevent out of index error.
        diag=''.join([data[i-k][j+k] for k in range(4)])
        if diag=='XMAS' or diag=='SAMX':
            count+=1
print(count)