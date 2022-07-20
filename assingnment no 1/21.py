a = 'Manpreet'
num = 0
for x in a[:4]:
    if (x.upper() == x):
        num += 1
if (num >= 2):
    print(a.upper())
else:
    print(a)
