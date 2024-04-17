import random

def fitnes(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i][1]
    return sum

def w(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i][0]
    return sum

initial_parent = [(7,10),(5,15),(10,5),(15,8),(5,20),(3,10),(8,7),(4,17),(9,5),(12,3)]

def generate_random_parents(fromarr,num,lower,higher):
    parents = []   
    for i in range(num):
        k =random.randint(lower,higher)
        parents.append(random.sample(fromarr,k))
    return parents
parents=generate_random_parents(initial_parent,10,3,9)
   




def move(parents):
    childs = []
    for i in range(0, len(parents), 2):
        rindex = random.randint(2, len(parents)-2)
        parent1 = parents[i]
        parent2 = parents[i+1]
        sub1 = parent1[rindex:]
        sub2 = parent2[:1+rindex]
        childs.append(sub1 + sub2)
    return childs

k=0
childs = move(parents)
for child in childs:
    k+=1
    fit = fitnes(child)
    weight = w(child)
    if weight <=50:
        print("fitness:", fit, "w:",weight,"child",k," :",child)
    else:
        print("fitness:", 1000, "w:",weight,"child ",k,":",child)
print()
i=0        
for parent in parents:
    i+=1
    print("parent(",i,") : ",parent)
    
