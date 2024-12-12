with open('Day 1 Data.txt') as f:
    data=f.readlines()

data=[tuple(int(j) for j in i[:-1].split('   ')) for i in data]

left_list=[]
right_list=[]
print(data)
for i,j in data:
    left_list.append(i)
    right_list.append(j)
left_list.sort()
right_list.sort()

distance_sum=0

for i in range(len(left_list)):
    distance_sum+=abs(left_list[i]-right_list[i])
print(distance_sum)
