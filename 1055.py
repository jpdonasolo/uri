from math import ceil, floor


for T in range(int(input())):

    n, *numbers = map(int, input().split())

    if n == 1:
        print(f"Case {T + 1}: 0")

    numbers = sorted(numbers)

    intervals = []
    k = n - 1
    eps = 0

    for i in range(k):
        intervals.append(abs(numbers[i] - numbers[i+1]))

    for i in range(ceil(k / 2) - 1):
        mlt = i + 1
        eps += 2 * mlt * intervals[i]
        eps += 2 * mlt * intervals[k - i - 1]

    # Next i
    i = ceil(k / 2) - 1
    mlt = i + 1

    if (n - 1) % 2 == 0:

        # Left Middle vs Right Middle
        if intervals[i] > intervals[i + 1]:

            eps += intervals[i] * (2 * mlt)
            eps += intervals[(i + 1)] * (2 * mlt - 1)

        else:
            eps += intervals[i] * (2 * mlt - 1)
            eps += intervals[(i + 1)] * (2 * mlt)

    else:
        # Middle of list
        eps += intervals[i] * (2 * mlt - 1)

    print(f"Case {T + 1}: {eps}")
