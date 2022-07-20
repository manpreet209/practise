str1 = 'i am the best'
str2 = ""
for i in range(len(str1)):
    if (i % 2 == 0):
        str2 = str2 + str1[i]
print('previous string:', str1)
print('new string', str2)

