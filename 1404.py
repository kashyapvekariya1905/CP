def numSteps(s: str) -> int:
    dec = int(s,2)
    step = 0
    while dec!=1:
        if dec%2==0:
            dec//=2
        else:
            dec+=1
        step+=1
    return step
s = "1111011110000011100000110001011011110010111001010111110001"
print(numSteps(s))