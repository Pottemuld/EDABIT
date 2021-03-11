def combination(*arguments):
    total = 1;
    for number in arguments:
        total *= number

    print(total)

combination(2, 3)
combination(3, 7, 4)
combination(2, 3, 4, 5)
