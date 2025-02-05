from typing import List


dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"

# dictionary = ["a","b","c"]
# sentence = "aadsfasf absbs bbab cadsfafs"

def replaceWords(dictionary: List[str], sentence: str) -> str:
    rst = []
    for word in sentence.split():
        for i in range(len(word)):
            if word[:i] in dictionary:
                word = word[:i]
                break
        rst.append(word)
    return " ".join(rst)
print(replaceWords(dictionary, sentence))