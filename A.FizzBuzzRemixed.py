import sys
input_data = sys.stdin.read().split()
t = int(input_data[0])
results = []
for i in range(1, t + 1):
    n = int(input_data[i])
    count = (n // 15) * 3
    remainder = n % 15
    count += min(2, remainder) + 1
    results.append(str(count))
print("\n".join(results))
