from collections import Counter
def max_score_words(words, letters, score):
    letter_count = Counter(letters)
    letter_score = {chr(i + 97): score[i] for i in range(26)}
    def get_score(word):
        word_count = Counter(word)
        score = 0
        for char, count in word_count.items():
            if letter_count[char] >= count:
                score += letter_score[char] * count
            else:
                return 0
        for char, count in word_count.items():
            letter_count[char] -= count
        return score
    def backtrack(start, curr_score):
        nonlocal max_score
        max_score = max(max_score, curr_score)
        for i in range(start, len(words)):
            word_score = get_score(words[i])
            if word_score:
                backtrack(i + 1, curr_score + word_score)
                for char, count in Counter(words[i]).items():
                    letter_count[char] += count
    
    max_score = 0
    backtrack(0, 0)
    return max_score

# Example usage
words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
print(max_score_words(words, letters, score))  # Output: 23

words = ["xxxz","ax","bx","cx"]
letters = ["z","a","b","c","x","x","x"]
score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
print(max_score_words(words, letters, score))  # Output: 27

words = ["leetcode"]
letters = ["l","e","t","c","o","d"]
score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
print(max_score_words(words, letters, score))  # Output: 0