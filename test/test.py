def abc():
    i  = 0
    while(i < 10):
        yield i
        i += 1
a = abc()
for i in a:
    print(i)