from typing import List
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    # lst = []
    # rst = []
    # linel = 0
    # for i in range(len(words)):
    #     if linel + len(lst) + len(words[i]) <= maxWidth:
    #         lst.append(i)
    #         linel+=len(words[i])
    #     else:
    #         spaces = maxWidth-linel
    #         if len(lst) == 1:
    #             rst.append(lst[0]+' '*spaces)
    #         else:
    #             gap = len(lst) - 1
    #             bases = spaces // gap
    #             extras = spaces % gap
    #             justified_line = ''
    #             for k in range(extras):
    #                 justified_line+=lst[k] + ' ' * (bases + 1)
    #             for k in range(extras, gap):
    #                 justified_line+=lst[k] + ' ' * (bases)
    #             justified_line+=lst[-1]
    #             rst.append(justified_line)
    #         lst = [i]
    #         linel=len(i)
    # last_line = ' '.join(lst)
    # last_line += ' ' * (maxWidth - len(last_line))
    # rst.append(last_line)
    
    # return rst
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            if len(cur) == 1:
                res.append(cur[0] + ' ' * (maxWidth - num_of_letters))
            else:
                num_spaces = maxWidth - num_of_letters
                space_between_words, extra_spaces = divmod(num_spaces, len(cur) - 1)
                for i in range(extra_spaces):
                    cur[i] += ' '
                res.append((' ' * space_between_words).join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    if cur:
        res.append(' '.join(cur) + ' ' * (maxWidth - num_of_letters - len(cur) + 1))
    return res
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(fullJustify(words,maxWidth))