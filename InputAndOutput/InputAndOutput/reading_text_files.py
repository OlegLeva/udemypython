# # Input
# x = input('Input something')
#
# # Output
# print('Output something' + x)

# print(1, 2, 3, sep=':', end='\n')
# print(1, 2, 3, sep=',', end=' ')
# print(1, 2, 3, sep=';', end='')

# lorem_ipsum_text = open('/Users/yuriyallakhverdov/Desktop/sample.txt', 'r')
# for line in lorem_ipsum_text:
#     print(line,end='')
# lorem_ipsum_text.close()

# lorem_ipsum_text = open('/Users/yuriyallakhverdov/Desktop/sample.txt', 'r')
# for line in lorem_ipsum_text:
#     if 'mary' in line.lower():
#         print(line,end='')
# lorem_ipsum_text.close()

# with open('/Users/yuriyallakhverdov/Desktop/sample.txt', 'r') as lorem_ipsum_text:
#     for line in lorem_ipsum_text:
#         if 'mary' in line.lower():
#             print(line,end='')

# with open('/Users/yuriyallakhverdov/Desktop/sample.txt', 'r') as lorem_ipsum_text:
#     line = lorem_ipsum_text.readline()
#     while line:
#         print(line, end='')
#         line = lorem_ipsum_text.readline()

# with open('/Users/yuriyallakhverdov/Desktop/sample.txt', 'r') as lorem_ipsum_text:
#     lines = lorem_ipsum_text.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line)

with open('/Users/yuriyallakhverdov/Desktop/sample.txt', 'r') as lorem_ipsum_text:
    text = lorem_ipsum_text.read()
print(text)


