from random import choice
counter = 0
i=0
while counter <100:
    print(counter)
    counter = counter + choice(range(10))
    i = i+1
print("number of counts = ", i)

pop = 100
year = 0
while 1:
    pop = pop*1.1
    year =year+1
    if pop>1000:
        break
print("Final pop =", pop)
print("Years it takes =", year)
