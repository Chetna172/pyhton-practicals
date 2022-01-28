K = int(raw_input())
nums = map(int, raw_input().split())

counts = {}
for n in nums:
    if n in counts:
        counts[n] += 1
    else:
        counts[n] = 1
for n in counts:
    if counts[n] == 1:
        print n
        break