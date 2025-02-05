from collections import deque


def predictPartyVictory(senate: str) -> str:
    qr = deque()
    qd = deque()
    n = len(senate)
    for i,s in enumerate(senate):
        if s == 'R':
            qr.append(i)
        else:
            qd.append(i)
    while qr and qd:
        r = qr.popleft()
        d = qd.popleft()
        if r<d:
            qr.append(r+n)
        else:
            qd.append(d+n)
    return "Radient" if qr else "Dire"


senate = "RD"
print(predictPartyVictory(senate))