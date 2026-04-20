x=input()
x=x.lower()
res=[]
vowel=["a", "o", "y", "e", "u", "i",]
for i in range(len(x)):
    if x[i] not in vowel:
        res.append(".")
        res.append(x[i])
print("".join(res))
