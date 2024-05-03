def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes_between(start, end):
    count = 0
    for number in range(start, end + 1):
        if is_prime(number):
            count += 1
    return count


# Sonlarni kiritish
L = int(input("Birinchi sonni kiriting: "))
R = int(input("Ikkinchi sonni kiriting: "))

# Tub sonlar sonini hisoblash
tub_sonlar_soni = count_primes_between(L, R)
print(f"{L} va {R} oralig'idagi deyarli tub sonlar: {tub_sonlar_soni} ta")






