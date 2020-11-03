self_num = set(i for i in range(1,10001))

generated_num = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = self_num - generated_num

for i in sorted(self_num):
    print(i)