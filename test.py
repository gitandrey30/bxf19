def sq():
    list1 = []
    for i in range(2,8):
        a= i**2
        list1.append(a)
        yield list1


list = sq()
print(next(list))
print(next(list))
print(next(list))
print(next(list))


a=-5
print(a)
b = int('-6')
c='-7'
print(type(c))
print(type(b))


