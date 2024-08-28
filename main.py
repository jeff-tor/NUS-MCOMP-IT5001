import test_3

def runMatch():
    num = int(input("Enter a number: "))

    # match case
    match num:
        # pattern 1
        case num if num > 0:
            print("Positive")
        # pattern 2
        case num if num < 0:
            print("Negative")
        # default pattern
        case _:
            print("Zero")


def test_matcH():
    age = input(f'what is your age?')
    stay_in_us = input(f'do you stay in US? Y/N')

    match age:
        case age if age >= 18:
            print(f'as you are more than age {age}, you can drive in SG')
        case stay_in_us if stay_in_us == Y:
            print(f'you can drive in US')

def counter_():
    n = 5
    for i in range(1, n):
        product = 1 * i
        i += 1
        print(i)


if __name__ == "__main__":
    counter_()