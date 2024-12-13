import re

with open('data.txt') as f:
    data=f.read()
active=True

mul_pattern=r"(?<=mul)\([\d]{1,3},[\d]{1,3}\)"

valid_pairs=[]

while data!='':

    if data[:4]=='do()':
        active=True
        data=data[4:]
        
    elif data[:7]=="don't()":
        active=False
        data=data[7:]

    elif active:

        if re.search(mul_pattern,data)==None:
            break
        
        closest_match=re.search(mul_pattern,data)

        if closest_match.start()==3:

            valid_pairs.append(eval(closest_match.group()))
            data=data[closest_match.end():]
        else:
            data=data[1:]
    else:
        data=data[1:]

sum_products=0
for i,j in valid_pairs:
    sum_products+=i*j
print(sum_products)