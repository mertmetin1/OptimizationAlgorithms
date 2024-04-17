

import random



#ai =weight of item i
#xi=number of item i(desicion var) xi=0 or 1
#ci=profit of item i
#maximize profit
#minimize weight

n=10
b=200# capacity of bag
bag=[(random.randint(20,70),random.randint(100,500)) for i in range(n)]# bag=[(ai,ci)]
max_profit=0
max_weight=0
opt_sol=0
opt_comb=[]
for i in range(int(2**n)):
    exist_item=[]
    current_profit=0
    current_weigth=0
    
    for j in range(n):
        if i>>j & 1:
            current_profit+=bag[j][1]
            current_weigth+=bag[j][0]
            exist_item.append(bag[j])
    if current_profit > max_profit and current_weigth < b :
        max_profit=current_profit
        max_weight=current_weigth
        opt_sol=format(i, 'b')
        opt_comb=exist_item
    print(format(i, 'b'))
        
print("max weight : ",max_weight)
print("max profit : ",max_profit)
print("optimal solution matrix : ",opt_sol)
print("optimal solution combination : ",opt_comb)
print("items : " ,bag)
        



