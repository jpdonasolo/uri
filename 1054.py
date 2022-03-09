def input_data():

    n, right = [int(x) for x in input().split()]

    if n == 0:
        return [(0, right)], [tuple()]

    stones_raw = input().split()
    stones_big = []
    stones_small = []

    prev_big = 0

    cur_small_list = []

    for stone in stones_raw:

        cur_stone_dist = int(stone[2:])

        if stone[0] == "B":

            stones_big.append((prev_big, cur_stone_dist))
            prev_big = cur_stone_dist

            stones_small.append(tuple(cur_small_list))
            cur_small_list = []

        else:
            cur_small_list.append(cur_stone_dist)

    stones_big.append((prev_big, right))
    stones_small.append(tuple(cur_small_list))

    return stones_big, stones_small


def find_max_jump(stones_big, stones_small):

    if len(stones_small) in [0, 1]:
        return stones_big[1] - stones_big[0]

    full = [stones_big[0]] + list(stones_small) + [stones_big[1]]

    i = 2
    max_jump_1 = 0
    while i <= len(full) - 1:
        max_jump_1 = max(max_jump_1, full[i] - full[i - 2])
        i += 2

    i = 3
    max_jump_2 = full[1] - full[0]
    while i <= len(full) - 1:
        max_jump_2 = max(max_jump_2, full[i] - full[i - 2])
        i += 2

    return max(max_jump_1, max_jump_2)


def main():

    T = int(input())

    for t in range(1, T + 1):

        stones_big, stones_small = input_data()

        max_jump = 0
        for stones_big_cur, stones_small_cur in zip(stones_big, stones_small):
            max_jump_cur = find_max_jump(stones_big_cur, stones_small_cur)
            max_jump = max(max_jump, max_jump_cur)

        print(f"Case {t}:", max_jump)


if __name__ == "__main__":
    main()
