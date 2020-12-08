digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

user_input = int(input())
user_input = str(user_input)

for i in user_input:
    i = int(i)
    if i == 0:
        print(digits[0])
    elif i == 1:
        print(digits[1])
    elif i == 2:
        print(digits[2])
    elif i == 3:
        print(digits[3])
    elif i == 4:
        print(digits[4])
    elif i == 5:
        print(digits[5])
    elif i == 6:
        print(digits[6])
    elif i == 7:
        print(digits[7])
    elif i == 8:
        print(digits[8])
    elif i == 9:
        print(digits[9])
