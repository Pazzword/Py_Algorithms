word = "Anzor just solved it!"

new = []

def alternate(word):
    for i in range(len(word)):
        if i % 2 == 0:
            new.append(word[i].upper())
        else:
            new.append(word[i].lower())
    return("".join(new))

print(alternate(word))