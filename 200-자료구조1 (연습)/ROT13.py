word = input()

result = ''

for i, alpha in enumerate(word):
    if alpha.isalpha():
        if alpha.isupper():
            result += chr(((ord(alpha) - ord('A') + 13) % 26) + ord('A'))
        else:
            result += chr(((ord(alpha) - ord('a') + 13) % 26) + ord('a'))
    else:
        result += alpha

print(result)