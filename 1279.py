def main():

    ano = int(input())

    while True:

        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        huluculu = ano % 15 == 0
        bulukulu = ano % 55 == 0

        if bissexto:
            print("This is leap year.")

        if huluculu:
            print("This is huluculu festival year.")

        if bulukulu and bissexto:
            print("This is bulukulu festival year.")

        if not (bissexto or huluculu):
            print("This is an ordinary year.")

        try:
            ano = int(input())
        except EOFError:
            break

        print("")


if __name__ == "__main__":
    main()
