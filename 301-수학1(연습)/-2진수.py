def nagative_binary(n):
    if n == 0:
        return "0"
    
    res = []
    while n != 0:
        remainder = n % -2
        n //= -2

        if remainder < 0:
            remainder += 2
            n += 1
        
        res.append(str(remainder))
    
    return ''.join(res[::-1])


n = int(input())
print(nagative_binary(n))