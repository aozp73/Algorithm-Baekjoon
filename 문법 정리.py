''' sorted(), sort() '''
# list 반환
li1 = [2,1,3,5,4]
res1 = sorted(li1, reverse=True)
res2 = sorted(li1)
print(res1)
print(res2)
# None 반환
li3 = [2,1,3,5,4]
li4 = [2,1,3,5,4]
res3 = li3.sort(reverse = True)
res4 = li4.sort()
print(res3) # None

# 람다 함수
li5 = [(3,1), (2,3), (4,2), (1,4)]
print(sorted(li5, key=lambda x: x[0]))
li5.sort(key=lambda x: x[0])
print(li5)