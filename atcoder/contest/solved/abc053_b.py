s = input()

start = 0
end = 0
for i in range(len(s)):
    if s[i] == 'A':
        start = i
        break
for i in reversed(range(len(s))):
    if s[i] == 'Z':
        end = i
        break
print(end - start + 1)
