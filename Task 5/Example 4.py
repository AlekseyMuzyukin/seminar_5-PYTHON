with open('file rle_1.txt', 'r') as data:
    lst = data.read()
print(lst)

str_code = ''
prev_char = ''
count = 1
for char in lst:
    if char != prev_char:
        if prev_char:
            str_code += str(count) + prev_char
        count = 1
        prev_char = char
    else:
        count += 1
print(str_code)

# Не понимаю почему не считывает "f" в конце строки,а считывает в начале...

count = ''
str_decode = ''
for char in str_code:
    if char.isdigit():
        count += char
    else:
        str_decode += char * int(count)
        count = ''
print(str_decode)

data = open('file rle_2.txt', 'w')
data.writelines(f'{str_decode}')
data.closed
