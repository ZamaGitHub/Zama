def gen(n):
    i = 0
    while i < n:
        print('a')
        yield i ** 2
        print('b')
        i += 1


for i in gen(int(input())):
    print(i)