chars = ["a","a","b","b","c","c","c"]
def compress(chars):
    if not chars:
        return 0
    rst = ""
    write_ptr = 0
    read_ptr = 0
    
    while read_ptr < len(chars):
        char = chars[read_ptr]
        count = 0
        
        while read_ptr < len(chars) and chars[read_ptr] == char:
            read_ptr += 1
            count += 1
        
        chars[write_ptr] = char
        write_ptr += 1
        rst += char
        if count > 1:
            rst += str(count)
            for digit in str(count):
                chars[write_ptr] = digit
                write_ptr += 1
    return write_ptr

chars1 = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(chars1))

chars2 = ["a"]
print(compress(chars2))

chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(compress(chars3))
