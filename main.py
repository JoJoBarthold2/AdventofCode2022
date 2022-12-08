lst = open("myInput").read().split("\n\n")

result =[]
for elem in lst:
    elem = elem.split("\n")

    usm = 0
    for ulum in elem:
        usm = usm + int(ulum)
    result.append(usm)
gaming = 0
for i in range(3):

    alpha = max(result)
    beta = result.index(alpha)
    gaming = alpha + gaming
    del result[beta]


print(gaming)