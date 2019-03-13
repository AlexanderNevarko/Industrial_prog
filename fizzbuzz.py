def is_5(number):
    if number[-1] == '5' or number[-1] == '0':
        return True
    else:
        return False

def is_3(number):
    number = abs(int(number))
    number = str(number)
    summ = 0
    for char in number:
        summ += int(char)
    if summ in (0, 3, 6, 9):
        return True
    elif summ in (1, 2, 4, 5, 7, 8):
        return False
    else:
        return is_3(str(summ))

def is_3_5(number):
    if is_3(number) and is_5(number):
        return True
    else:
        return False
    
seq = [str(i) for i in input().split()]
length = len(seq)
for i in range(length):
    if is_3_5(seq[i]):
        seq[i] = 'fizzbuzz'
    elif is_3(seq[i]):
        seq[i] = 'fizz'
    elif is_5(seq[i]):
        seq[i] = 'buzz'

for i in range(length):
    print(seq[i])
            