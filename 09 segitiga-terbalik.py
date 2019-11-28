x = 5
y = 0
for i in range(0, x):
    for j in range(0, y):
        print(' ',end='')
    y += 1
    for k in range(0, x):
        print('* ' , end='')
    x -= 1
    print()
