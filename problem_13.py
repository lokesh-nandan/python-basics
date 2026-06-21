l = [1, 9, 2, 8, 3, 7]
lcopy=l.copy()
t=10 #target value
for i in lcopy:
    for j in lcopy:
        if i==j:
            continue
        if i+j==10:
            lcopy.remove(i)
            print(i, j)