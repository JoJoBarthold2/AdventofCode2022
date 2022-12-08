lst = open("input").readlines()
result= []
for elem in lst:
    splt = list(elem.rstrip())
    intsplt = [int(x) for x in splt]
    result.append(intsplt)
print(result)
