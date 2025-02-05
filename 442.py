arr = [1]
freq = {}
for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]]+=1
    else:
        freq[arr[i]] = 1
store = []
for key,value in freq.items():
    if value == 2:
        store.append(key)
store.sort()
print(store)