lst = open("input").readlines()



pist = 0
for elem in lst:
    a = len(elem) // 2
    fst = set(elem[:a])
    snd = set(elem[a:])
    duble = fst.intersection(snd).pop()
    #print(duble)
    if duble.islower():
        plis = ord(duble) - ord("a") +1
    else:
        plis = ord(duble) - ord("A") +27
    pist = pist + plis
print(pist)


counter = 0
pist = 0
length = len(lst)
while counter < int(length):
    a = set(lst.__getitem__(counter))
    b = set(lst.__getitem__(counter+1))
    c= set(lst.__getitem__(counter+2))
    duble = a.intersection(b).intersection(c)
    duble.discard("\n")
    duble = duble.pop()
    counter = counter+3
    print(duble)
    if duble.islower():
        plis = ord(duble) - ord("a") + 1
    else:
        plis = ord(duble) - ord("A") + 27
    pist = pist + plis
print(pist)