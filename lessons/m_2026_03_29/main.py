# print('**')
# print('**')
# len_square = int(input('введите длину стороны квадрата: '))
# for i in range(len_square):
#     for j in range(len_square):
#         print('*', end = '')#сделать через создание строчки
#     input()
#     print()
# s = 0
# for i in range(1,11):
#     if i % 2 == 0:
#         s = s + i
#         print(s)
a = int(input())
for i in range(0,a,1):
    print((i - a)*' '+ i * '*')
for i in range(a,0,-1):
    print((a - i)*' '+ i * '*')
# summa = 0
# count = 0
# a = int(input())
# while a != 0:
#     if a % 2 == 0:
#         summa = summa + a
#     count = count + 1
#     a = int(input())
# print(summa,count)
# a = int(input())
# k = 0
# while a != 0:
#     if a % 2 and a % 5:
#         k = k + 1
#     a = int(input())
# print(k)


''