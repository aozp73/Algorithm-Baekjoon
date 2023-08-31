octal_num = input().strip()

# 8진수 -> 10진수
decimal_num = int(octal_num, 8)

# 10진수 -> 2진수
binary_num = bin(decimal_num)[2:]
print(binary_num)
