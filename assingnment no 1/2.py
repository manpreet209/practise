str1= input('enter your string:')
d1 = dict()
for c in str1:
    if c in d1:
        d1[c] += 1
    else :d1[c] = 1
print(d1)
