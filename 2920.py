while True:

    try:
        N, K = input().split()
        K = int(K)
    except EOFError:
        break

    # Count each digit
    numbers = [0] * 10
    for digit in N:
        numbers[int(digit)] += 1

    highest_number_on_string = 9
    removed = 0

    # Update threshold for digits to be removed 
    while removed < K:
        removed += numbers[highest_number_on_string]
        highest_number_on_string -= 1

    # If surpasses K, return one step
    if removed > K:
        highest_number_on_string += 1

    # Update final string
    removed = 0
    for to_remove in range(9, highest_number_on_string, -1):
        N = N.replace(str(to_remove), "")
        removed += numbers[to_remove]
    
    # If did not remove enough, remove some more
    remaining = K - removed
    N = N.replace(str(highest_number_on_string), "", remaining)

    print(N)
