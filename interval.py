
def chiroyli_sonlar(L, R):
    count = 0
    for i in range(L, R + 1):
        if str(i) == str(i)[::-1]:
            count += 1
    return count

L, R = 2,47
print(chiroyli_sonlar(L, R))