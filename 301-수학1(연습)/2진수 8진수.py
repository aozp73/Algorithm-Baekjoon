binary_num = input().strip()

# 2진수 -> 10진수
decimal_num = int(binary_num, 2)

# 10진수 -> 8진수
octal_num = oct(decimal_num)[2:]
print(octal_num)
