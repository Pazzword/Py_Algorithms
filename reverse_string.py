class Solution:
    def __init__(self, string):
        self.string = string

    def reverse_string(self):
        return self.string[::-1]

if __name__ == "__main__":
    string = "Anzor solved it?!"
    print(Solution(string).reverse_string())