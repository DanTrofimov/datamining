import random
from collections import Counter

# config
size = 1000000
sequence = []
count = 0


# calculating second moment
def calculateSecondMoment(sequence):
    c = Counter(sequence)
    return sum(v ** 2 for v in c.values())


# calculating 0, 1 moment & estimating 2nd moment
def estimateMoment(sequence, num_samples):
    nums = list(range(len(sequence)))
    random.shuffle(nums)
    # getting the slice of our sequence with num_samples length
    nums = sorted(nums[: num_samples])

    d = {}
    for i, c in enumerate(sequence):
        if i in nums and c not in d:
            d[c] = 0
        if c in d:
            d[c] += 1
    print("0 moment: ", len(d))
    print("1st moment", size)
    # estimating 2nd
    return int(len(sequence) / float(len(d)) * sum((2 * v - 1) for v in d.values()))


# fill our sequence
for x in range(size):
    sequence.append(random.randint(1, 1000))
    count += 1

b = calculateSecondMoment(sequence)
a = estimateMoment(sequence, 100)
print("2nd moment: ", b)
print("2nd moment by ams from 100: ", a)
print(abs(b - a))
c = estimateMoment(sequence, 500)
print("2nd moment: ", b)
print("2nd moment by ams from 500: ", c)
print(abs(c - a))
