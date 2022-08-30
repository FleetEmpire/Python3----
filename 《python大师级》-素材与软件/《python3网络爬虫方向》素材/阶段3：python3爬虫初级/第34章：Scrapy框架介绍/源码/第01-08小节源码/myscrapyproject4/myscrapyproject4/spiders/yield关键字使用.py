def fun1():
    list1 = []
    for i in range(1,20):
        list1.append(i)
    return list1

def fun2():
    for i in range(1, 20):
        yield i

gen = fun2()
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))