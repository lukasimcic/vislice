for i in range(1, 200):
    test = True
    for p in range(2, i - 1):
        if i % p == 0:
            test = False
    if test:
        print(i)