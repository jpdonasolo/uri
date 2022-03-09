from math import ceil, floor

while True:

    N, Q = map(int, input().split())

    if (N == Q == 0):
        break

    songs = {i: song for i, song in enumerate(input().split())}
    queries = map(int, input().split())

    n = len(songs)

    for q in queries:
        k = 1

        letters = []
        while q > 0:
            # Numbers of sequence of songs times number of letters in each one
            q -= k * n ** (k)
            k += 1

        if q == 0:
            print(songs[n-1])
            continue
        else:
            k -= 1
            q += k * n ** k

        if q == 0:
            print(songs[n-1])
            continue

        pos = (q-1) % k
        j = ceil(q / k)
        label = (floor((j - 1) / n ** (k - pos - 1))) % n

        print(songs[label])

    print()
