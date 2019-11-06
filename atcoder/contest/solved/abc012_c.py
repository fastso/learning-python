n = int(input())

ans_sum = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans_sum += i * j

ans_sum -= n

for i in range(1, 10):
    if ans_sum % i == 0 and ans_sum / i < 10:
        print(i, end=" x ")
        print(int(ans_sum / i))
