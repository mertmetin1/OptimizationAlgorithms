import random

# Şehir listesi
cities = ['A', 'B', 'C', 'D', 'E']

def generate_parent(city):
    # Rastgele bir şehir sıralaması oluşturma
    city=random.sample(city,len(city))
    return city


parent1=generate_parent(cities)
parent2=generate_parent(cities)
gen_list={}
print(parent1)
print(parent2)
selected='A'
for i in range(len(parent1)):
    gen=parent1[i]
    gen_list[gen]=set()
    if i == 0:
        gen_list[gen].add(parent1[-1])
        gen_list[gen].add(parent1[1])
    elif i == len(parent1) - 1:
        gen_list[gen].add(parent1[i - 1])
        gen_list[gen].add(parent1[0])
    else:
        gen_list[gen].add(parent1[i - 1])
        gen_list[gen].add(parent1[i + 1])
             
    gen2=parent2[i]
    if gen2 not in gen_list:
        gen_list[gen2]=set()
    if i == 0:
        gen_list[gen2].add(parent2[-1])
        gen_list[gen2].add(parent2[1])
    elif i == len(parent2) - 1:
        gen_list[gen2].add(parent2[i - 1])
        gen_list[gen2].add(parent2[0])
    else:
        gen_list[gen2].add(parent2[i - 1])
        gen_list[gen2].add(parent2[i + 1])
    
            
            

print(gen_list)