import collections
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        pattern_dict = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                pattern_dict[pattern].append(word)

        visited_words = set([beginWord])
        q = collections.deque([beginWord])
        result = 1
        while q:
            print(q)
            for _ in range(len(q)):
                popped = q.popleft()
                if popped == endWord:
                    return result

                for j in range(len(popped)):
                    pattern = popped[:j] + '*' + popped[j+1:]

                    for pattern_word in pattern_dict[pattern]:
                        if pattern_word not in visited_words:
                            visited_words.add(pattern_word)
                            q.append(pattern_word)

            result += 1

        return 0


if __name__ == "__main__":
    solution = Solution()

    input = (
        "hit",
        "cog",
        ["hot","dot","dog","lot","log","cog"],
    )
    result = solution.ladderLength(*input)
    print(result)
