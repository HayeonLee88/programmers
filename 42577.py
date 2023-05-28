# 42577
l = ["123", "112", "1234", "114"]
l.sort()
for i in range(len(l) - 1):
    if l[i] == l[i + 1][:len(l[i])]:
        print('False')
