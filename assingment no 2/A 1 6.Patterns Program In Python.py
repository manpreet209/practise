n = int(input("Enter the number of rows"))

for i in range(0, n):

    for j in range(0, i + 1):

        print("* ", end="")
Leap Year Program
    print()
year = int(input('enter year'))
if year % 400 == 0:
  print('it is a leap year')
elif year % 4 == 0:
  print('it is a leap year')
elif year % 100 == 0:
  print('not a leap year')
else:
  print('not a leap year')
