from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def count_multiples(L, R, k):
    return (R // k) - ((L - 1) // k)

def count_valid_numbers(L, R, N):
    total_count = R - L + 1
    divisors = list(range(2, N + 1))
    m = len(divisors)
    excluded_count = 0

    # Sử dụng nguyên lý bao hàm và loại trừ
    for i in range(1, 1 << m):
        lcm_value = 1
        bits = bin(i).count('1')
        for j in range(m):
            if i & (1 << j):
                lcm_value = lcm(lcm_value, divisors[j])
                if lcm_value > R:  # Nếu LCM lớn hơn R, không cần kiểm tra nữa
                    break
        else:
            count = count_multiples(L, R, lcm_value)
            if bits % 2 == 1:  # Nếu số lượng số chia hết là lẻ
                excluded_count += count
            else:  # Nếu số lượng số chia hết là chẵn
                excluded_count -= count

    return total_count - excluded_count

while True:
    line = input().strip()
    if line == "-1":
        break
    L, R = map(int, line.split())
    N = int(input().strip())
    result = count_valid_numbers(L, R, N)
    print(result)