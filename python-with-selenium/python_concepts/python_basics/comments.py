#jsvej
"""Hello_world"""
# x = """Hello_World"""
# print(x)


num = 1
for i in range(1,5):
    for j in range(1, i+1):
        print(num, end='')
    num = num + 1
    print('\r')