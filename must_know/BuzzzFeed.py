numbers = len(range(1, 101))

def personal(x):
    new = []
    for i in range(1, x + 1):
        if i % 3 == 0 and i % 5 == 0:
            new.append("BuzzFID")
        elif i % 5 == 0:
            new.append("Fid")
        elif i % 3 == 0:
            new.append("BU")
        else:
            new.append(i)
    return new

print(personal(numbers))
