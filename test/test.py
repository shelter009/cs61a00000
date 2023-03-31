def abc():
    yield from[1,2,3,4]
a = abc()
print(next(a))