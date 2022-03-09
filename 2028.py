def main():

    n = int(input())
    T = 1

    while True:

        digits = int((n * (n + 1)) / 2 + 1)
        print(f"Caso {T}: {digits} numero{'s' if (digits - 1) else ''}")

        for i in range(0, n+1):

            if i == 0:
                print("0", end="")

            else:
                print((" " + str(i)) * i, end="")

        print("\n")

        try:
            n = int(input())
            T += 1
        except EOFError:
            break


if __name__ == "__main__":
    main()
