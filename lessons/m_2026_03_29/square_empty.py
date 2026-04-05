'''len_square = int(input('введите длину стороны квадрата: '))
for row_index in range(len_square): #i - 0,1,2... 
    row_str = ''
    for row_element_index in range(len_square):
        if row_index  == 1 and row_element_index == 1:
            row_str += ' '
        else:
            row_str += '*'
    input()
    print(row_str)'''
len_square = int(input('введите длину стороны квадрата: '))
for row_index in range(len_square): #i - 0,1,2... 
    row_str = ''
    for row_element_index in range(len_square):
        if (row_index > 0 and row_index < len_square - 1) and ( row_element_index > 0 and row_element_index < len_square - 1):
            row_str += ' '
        else:
            row_str += '*'
    input()
    print(row_str)
