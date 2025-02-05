def addDigits(num: int) -> int:
    if num < 10:
        return num
    else:
        return addDigits(num // 10 + num % 10)

num = 38
print(addDigits(num))