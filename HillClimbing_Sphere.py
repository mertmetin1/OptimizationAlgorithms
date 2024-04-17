"""
    EN 344 OPTİMİZATİON ALGORİTHMS WEEK-3 TASK
Q1. Code the given Algorithm-I in any programming language you know. Each x
value in the equation is a random value generated between [-100,100].
𝑿 = {𝒙𝟏 , 𝒙𝟐 , 𝒙𝟑 , 𝒙𝟒 , 𝒙𝟓 , 𝒙𝟔 , 𝒙𝟕 , 𝒙𝟖 , 𝒙𝟗 , 𝒙𝟏𝟎 } , ∀𝒙 ∈ [−𝟏𝟎𝟎, 𝟏𝟎𝟎]
                             𝒏
𝑭𝒊𝒕𝒏𝒆𝒔𝒔 𝑭𝒖𝒏𝒄𝒕𝒊𝒐𝒏(𝑺𝒑𝒉𝒆𝒓𝒆) ∶ 𝒇(𝑿) = ∑ 𝒙𝟐𝒊
                            𝒊=𝟏
Algorithm-I : Hil Climbing with Sphere Function
MaxIt=1000, T=0; Fitness(X), Movement(X)
Create an array called name X that has 10 dimension with a random values
between -100 and 100
while(t< MaxIt)
n= Movement(X)
if(Fitness(X)>Fitness(n))
Replace value x with n
end if
Print iteration and current fitness
end while
Hint:
Movement Function(X)
The Movement Function(X) function takes an array X as a parameter. The value
at the randomly selected index is added to a random value generated between
[-2,2]. If the value in the index is more than 100, it should be equal to 100, and
if it is less than -100, it should be equal to -100. This function should return the
new neighbor value produced.
    
    """
    
import random

def fitness(array):
    return sum([i**2 for i in array])

def movement(array):
    index = random.randint(0, len(array) - 1)
    add2 = random.randint(-2, 2)
    array[index] += add2
    if array[index] > 100:
        array[index] = 100
    elif array[index] < -100:
        array[index] = -100

x1 = [random.randint(-100, 100) for i in range(10)]
initial_fitness = fitness(x1)
max_iteration = 1000
t = 0

while t < max_iteration:
    n = x1.copy()
    movement(n)
    if fitness(x1) >= fitness(n):
        x1 = n
    if t % 100 == 0:
        print("Iteration:", t, "Fitness:", fitness(x1))
    t += 1

print("Initial fitness:", initial_fitness)



