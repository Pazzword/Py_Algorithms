import re

def count_words(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read().lower()

    # Split the text into words
    words = re.findall(r'\b\w+\b', text)

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Sort the words by count (descending) and then alphabetically
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    # Write the results to the output file
    with open(output_file, 'w') as file:
        for word, count in sorted_words:
            file.write(f"{word}: {count}\n")

    print(f"Word counts have been written to {output_file}")

# Example usage
input_file = "input.txt"
output_file = "word_counts.txt"
count_words(input_file, output_file)