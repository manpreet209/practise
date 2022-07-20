test_str = 'Manpreet Singh'

# printing original string
print("The original string is : " + str(test_str))

#  initializing mid string
mid_str = "love to"

#  splitting string to list
temp = test_str.split()
mid_pos = len(temp) // 2

#  appending in mid
res = temp[:mid_pos] + [mid_str] + temp[mid_pos:]

#  conversion back
res = ' '.join(res)

#  printing result
print("Formulated String : " + str(res))
