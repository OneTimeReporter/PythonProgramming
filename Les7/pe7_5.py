dict={}
def namen():
    while True:
        naam = input("Enter a name:\n")
        lst = naam.split()

        for key in lst:
            dict[key] = dict.get(key, 0) + 1

        if not lst:
            for n in dict:
                if dict[n] == 1:
                    print('There is {} student named {}'.format(dict[n],n))
                else:
                    print('There are {} students named {}'.format(dict[n],n))
            break
namen()