def yield_fun():
    for i in range(5):
        yield 'test', i * 2, 0.001
        print("*"*20)

def yield_test():
    test = yield_fun()

    for word, *num in test:
        print(word)
        print("*"*5)
        print(*num)

if __name__ == '__main__':
    yield_test()