word = "Anzor has just solved it!"


class Solution:
    def alternate(self, word: str) -> str:
        new = []
        for i in range(len(word)):
            if i % 2 == 0:
                new.append(word[i].upper())
            else:
                new.append(word[i].lower())
        return("".join(new))



solution = Solution()

print(solution.alternate(word))

