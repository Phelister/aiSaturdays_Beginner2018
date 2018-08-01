#phelister code changes
import random 

ourList = list()
count = 0 
while (count < 11):
    ourList.append(random.randint(1,10))
    count += 1
    
ourList
belowFive =[rand for rand in ourList if rand<5]

print(belowFive)
