def necha_marta(N):
    count = 0
    while N > 1:
        N //= 2
        count += 1
    return count

N = int(input("Butun son kiriting: "))
print("Qizaloqning dugonasi eng kamida", necha_marta(N), "marta savol berishi kerak.")
