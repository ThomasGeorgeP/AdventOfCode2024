with open('data.txt') as f:
    data=f.read()
    data=data.split('\n\n')

priority_list=[tuple(int(j) for j in i.split('|')) for i in data[0].split('\n')]
check_list=[[int(j) for j in i.split(',')] for i in data[1].split('\n')]

num_rules_dict={}
for i,j in priority_list:

    if j not in num_rules_dict:
        num_rules_dict[j]=set()
    
    num_rules_dict[j].add(i)

count=0

for i in check_list:
    # for j in range(len(i)-1,-1,-1):
    #     if set(i[:j]) - num_rules_dict[i[j]] !=set():
    #         break
    # else:
    #     count+=i[len(i)//2]
    order_len=[True for j in range(len(i)-1,-1,-1) if set(i[:j]) - num_rules_dict[i[j]] ==set()]
    if len(order_len)==len(i):
        count+=i[len(i)//2]

print(count)