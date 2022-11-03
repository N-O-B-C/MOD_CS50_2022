tally = {}
while True:
    try:
        item = input("item:")
        if item in tally:
            tally[item] += 1
        if item == "break":
                break
        else:
            tally[item] = 1
        for key in sorted(tally.keys()):
            print(tally[key],key.upper())
    except NameError:
        pass