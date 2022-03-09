import string


def go_right(sequenceString):

    newSequenceString = ""

    for caracter in sequenceString:

        if caracter.lower() in string.ascii_letters:
            caracter = chr(ord(caracter) + 3)

        newSequenceString += caracter

    return newSequenceString


def invert(sequenceString):

    return sequenceString[::-1]


def go_left(sequenceString):

    half = int(len(sequenceString) / 2)
    newSequenceString = sequenceString[:half]

    for caracter in sequenceString[half:]:

        newSequenceString += chr(ord(caracter) - 1)

    return newSequenceString


def main():

    N = int(input())

    for _ in range(N):
        sequenceString = input()

        myString = go_right(sequenceString)
        myString = invert(myString)
        myString = go_left(myString)

        print(myString)


if __name__ == "__main__":
    main()
