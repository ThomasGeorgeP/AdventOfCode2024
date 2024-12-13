import re

with open('data.txt') as f:
    data=f.read()
    
pattern=r"mul\([\d]{1,3},[\d]{1,3}\)"
matches=re.findall(pattern,data)
matches=[[int(j) for j in i[4:-1].split(',')] for i in matches]
prod=0
for i in matches:
    prod+=i[0]*i[1]
print(prod)