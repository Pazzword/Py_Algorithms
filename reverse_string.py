# Clean code
def reverse_string(s):
    return s[::-1]

example = "Anzor"

print(reverse_string(example))


#Detailed code
def reverse_string(any_word):
    create_list = list(any_word)
    reversed_list = create_list[::-1]
    reversed_string = "".join(reversed_list)

    return reversed_string


example = "Anzor"

reverse_string = reverse_string(example)

print(reverse_string)
