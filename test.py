

def test():
    foo = [i for i in range(5)]
    for i, _ in enumerate(foo[:-2]):
        for j, _ in enumerate(foo[i+1:-1], i+1):
            for k, _ in enumerate(foo[j+1:], j+1):
                print(f'i:{i}, j:{j}, k:{k}')


if __name__ == '__main__':
    test()
