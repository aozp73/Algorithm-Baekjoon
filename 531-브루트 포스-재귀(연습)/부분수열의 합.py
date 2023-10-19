from itertools import chain, combinations

def powerset(iterable):
    # powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def smallest_number(arr):
    possible_sums = set()

    for subset in powerset(arr):
        possible_sums.add(sum(subset))

    answer = 1
    while True:
        if answer not in possible_sums:
            return answer
        answer += 1

# main
n = int(input())
arr = list(map(int, input().split()))   
print(smallest_number(arr))
